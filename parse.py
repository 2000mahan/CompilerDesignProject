from ply import yacc
from lexer import Lexer
from code_generation.nonTerminal import NonTerminal
from code_generation.codeGenerator import CodeGenerator


class Parser:
    tokens = Lexer().tokens

    precedence = (
        ('right', "ASSIGN"),
        ('left', "IF"),
        ('left', "OR"),
        ('left', "AND"),
        ('left', "NOT"),
        ('left', "GT", "LT", "NE", "EQ", "LE", "GE"),
        ('left', "MOD"),
        ('left', "SUM", "SUB"),
        ('left', "MUL", "DIV"),
        ("nonassoc", "p1"),
        ("nonassoc", "ELSE", "ELSEIF"),

    )

    def __init__(self):
        self.tempVariableCount = 0
        self.tempLabelCount = 0
        self.codeGenerator = CodeGenerator(self)

    def new_temp(self):
        temp = "T" + str(self.tempVariableCount)
        self.tempVariableCount += 1
        return temp

    def new_label(self):
        temp = "L" + str(self.tempLabelCount)
        self.tempLabelCount += 1
        return temp, False

    def p_program(self, p):
        """program : declist MAIN LRB RRB block
                    | MAIN LRB RRB block"""
        self.codeGenerator.generate_program(p)

    def p_declist(self, p):
        """declist : dec
                   | declist dec"""
        self.codeGenerator.generate_declist(p)

    def p_dec_vardec(self, p):
        """dec : vardec"""
        self.codeGenerator.generate_dec_from_vardec(p)

    def p_dec_funcdec(self, p):
        """dec : funcdec"""
        pass

    def p_type(self, p):
        """type : INTEGER
                | FLOAT
                | BOOLEAN"""
        p[0] = NonTerminal()
        p[0].type = p[1]
        pass

    def p_iddec(self, p):
        """iddec : lvalue"""
        self.codeGenerator.generate_iddec_lvalue(p)

    def p_iddec_assign(self, p):
        """iddec : lvalue ASSIGN exp"""
        self.codeGenerator.generate_assign(p, True, self.new_label, self.new_temp)

    def p_idlist(self, p):
        """idlist : iddec
                  | idlist COMMA iddec"""
        self.codeGenerator.generate_id_list(p)

    def p_vardec(self, p):
        """vardec : idlist COLON type SEMICOLON"""
        self.codeGenerator.generate_vardec(p)

    # TODO: Function decleration
    def p_funcdec(self, p):
        """funcdec : FUNCTION ID LRB paramdecs RRB COLON type block
                   | FUNCTION ID LRB paramdecs RRB block"""
        # print("FUNCTION ID LRB paramdecs RRB COLON type block| FUNCTION ID LRB paramdecs RRB block")
        pass

    # TODO: Function parameters decleration
    def p_paramdecs(self, p):
        """paramdecs : paramdecslist
                     | empty"""
        # print("paramdecslist| empty")
        pass

    # TODO: Function parameter list decleration
    def p_paramdecslist(self, p):
        """paramdecslist : paramdec
                         | paramdecslist COMMA paramdec"""
        # print("paramdec| paramdecslist COMMA paramdec")
        pass

    # TODO: Function parameter decleration
    def p_paramdec(self, p):
        """ paramdec : ID COLON type
                     | ID LSB RSB COLON type"""
        # print("ID COLON type| ID LSB RSB COLON type")
        pass

    def p_block(self, p):
        """block : LCB stmtlist RCB"""
        self.codeGenerator.generate_from_block(p)

    def p_stmtlist(self, p):
        """stmtlist : stmtlist stmt
                    | empty"""
        p[0] = NonTerminal()
        if p[1] is None:
            self.codeGenerator.generate_empty_statement_list(p, self.new_label())
        else:
            self.codeGenerator.generate_statement_list(p)

    def p_lvalue(self, p):
        """lvalue : ID"""
        self.codeGenerator.generate_lvalue_from_id(p)

    def p_lvalue_arr(self, p):
        """lvalue : ID LSB exp RSB"""
        self.codeGenerator.generate_lvalue_from_array(p, self.new_temp())

    def p_case(self, p):
        """case : WHERE const COLON stmtlist"""
        self.codeGenerator.generate_case(p, self.new_label(), self.new_label())

    def p_cases(self, p):
        """cases : cases case
                | empty"""
        if len(p) == 2:
            self.codeGenerator.generate_cases_empty(p, self.new_label())
        else:
            self.codeGenerator.generate_cases(p)

    # TODO: Loops and conditionals
    def p_stmt_return(self, p):
        """stmt : RETURN exp SEMICOLON"""
        pass

    def p_stmt_from_on(self, p):
        """stmt : ON LRB exp RRB LCB cases RCB SEMICOLON"""
        self.codeGenerator.generate_statement_from_on(p, self.new_label)

    def p_stmt_for_in(self, p):
        """stmt : FOR LRB ID IN ID RRB stmt"""
        if p[7].begin == '':
            p[7].begin = self.new_label()
        self.codeGenerator.generate_statement_from_for_in(p, self.new_label(), self.new_label(), self.new_label(),
                                                          self.new_label(), self.new_label(), self.new_label(),
                                                          self.new_label(),
                                                          self.new_temp(), self.new_temp(), self.new_temp())

    def p_stmt_for_i(self, p):
        """stmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt"""
        self.ensure_true_false(p[5])
        if p[9].begin == "":
            p[9].begin = self.new_label()
        if p[5].begin == '':
            p[5].begin = self.new_label()
        if p[3].begin == '':
            p[3].begin = self.new_label()
        if p[7].begin == '':
            p[7].begin = self.new_label()
        self.codeGenerator.generate_statement_from_for(p, self.new_label(), self.new_label(), self.new_label(),
                                                       self.new_label())

    def p_stmt_while(self, p):
        """stmt : WHILE LRB exp RRB stmt"""
        self.ensure_true_false(p[3])
        if p[5].begin == "":
            p[5].begin = self.new_label()
        if p[3].begin == '':
            p[3].begin = self.new_label()
        self.codeGenerator.generate_statement_from_while(p, self.new_label(), self.new_label(), self.new_label())

    def p_stmt_vardec(self, p):
        """stmt : vardec"""
        p[0] = NonTerminal()
        p[0].next = self.new_label()
        p[0].code += p[1].code + ";\n"
        p[0].code += p[1].exp + ';\n'
        p[0].symbols.extend(p[1].symbols)

    def p_stmt_print(self, p):
        """stmt : PRINT LRB ID RRB SEMICOLON"""
        self.codeGenerator.generate_print(p, self.new_label())

    def p_stmt_from_block(self, p):
        """stmt : block"""
        p[0] = NonTerminal()
        p[0].next = p[1].next
        p[0].begin = p[1].begin
        p[0].code = p[1].code
        p[0].symbols = [p[1].symbols]

    def p_stmt_from_exp(self, p):
        """stmt : exp SEMICOLON"""
        self.codeGenerator.generate_statement_from_exp(p, self.new_label())

    def p_stmt_if(self, p):
        """stmt : IF LRB exp RRB stmt elseiflist %prec p1
                | IF LRB exp RRB stmt elseiflist ELSE stmt"""
        p[0] = NonTerminal()
        p[0].symbols.extend(p[5].symbols)
        p[0].symbols.extend(p[6].symbols)
        self.ensure_true_false(p[3])
        if p[5].begin == '':
            p[5].begin = self.new_label()
        if len(p) == 9:
            p[0].symbols.extend(p[8].symbols)
        if len(p) == 9 and p[8].begin == '':
            p[8].begin = self.new_label()
        p[0].begin = self.new_label()
        self.codeGenerator.generate_if(p, self.new_label(), 3, 5, False, self.new_label(), self.new_label())

    def p_elseiflist(self, p):
        """elseiflist : elseiflist ELSEIF LRB exp RRB stmt
                      | empty"""
        p[0] = NonTerminal()
        if p[1] is None:
            self.codeGenerator.generate_empty_elseif_list(p, self.new_label(), self.new_label(), self.new_label())
        else:
            if p[6].begin == '':
                p[6].begin = self.new_label()
            if p[4].begin == '':
                p[4].begin = self.new_label()
            self.ensure_true_false(p[4])
            self.codeGenerator.generate_elseif_list(p, self.new_label(), self.new_label(), self.new_label())

    def p_exp_relop(self, p):
        """exp : exp GT exp
               | exp LT exp
               | exp NE exp
               | exp EQ exp
               | exp LE exp
               | exp GE exp"""
        self.codeGenerator.generate_boolean_relop_code(p, self.new_temp(), self.new_label(), self.new_label(),
                                                       self.new_label(), self.new_label(), self.new_label(),
                                                       self.new_label(), self.new_label(), self.new_label())

    def p_exp_or(self, p):
        """exp : exp OR exp"""
        self.ensure_true_false(p[3])
        self.ensure_true_false(p[1])
        if p[3].begin == "":
            p[3].begin = self.new_label()
        self.codeGenerator.generate_or(p, self.new_label)

    def p_exp_and(self, p):
        """exp : exp AND exp"""
        self.ensure_true_false(p[1])
        self.ensure_true_false(p[3])
        if p[3].begin == "":
            p[3].begin = self.new_label()
        self.codeGenerator.generate_and(p, self.new_label)

    def p_exp_not(self, p):
        """exp : NOT exp"""
        self.ensure_true_false(p[2])
        self.codeGenerator.generate_not(p, self.new_label)

    # TODO: Function call
    def p_exp(self, p):
        """exp : lvalue LRB explist RRB
               | lvalue LRB RRB"""
        pass

    def p_exp_lvalue(self, p):
        """exp : lvalue"""
        self.codeGenerator.generate_lvalue_exp(p)

    def p_exp_paran(self, p):
        """exp : LRB exp RRB"""
        self.codeGenerator.generate_paran_exp(p, self.new_temp(), self.new_label())

    def p_exp_assign(self, p):
        """exp : lvalue ASSIGN exp"""
        self.codeGenerator.generate_assign(p, False, self.new_label, self.new_temp)

    def p_exp_neg(self, p):
        """exp : SUB exp"""
        self.codeGenerator.generate_negation_code(p, self.new_temp(), self.new_label())

    def p_exp_sum(self, p):
        """exp : exp SUM exp"""
        self.codeGenerator.generate_arithmetic_code(p, self.new_temp(), self.new_label())

    def p_exp_sub(self, p):
        "exp : exp SUB exp"
        self.codeGenerator.generate_arithmetic_code(p, self.new_temp(), self.new_label())

    def p_exp_mul(self, p):
        "exp : exp MUL exp"
        self.codeGenerator.generate_arithmetic_code(p, self.new_temp(), self.new_label())

    def p_exp_div(self, p):
        "exp : exp DIV exp"
        self.codeGenerator.generate_arithmetic_code(p, self.new_temp(), self.new_label())

    def p_exp_mod(self, p):
        "exp : exp MOD exp"
        self.codeGenerator.generate_arithmetic_code(p, self.new_temp(), self.new_label())

    def p_const(self, p):
        """exp : const"""
        p[0] = NonTerminal()
        if p[1].value == "False":
            p[0].value = '0'
            p[0].exp = '1 == 0'
        elif p[1].value == "True":
            p[0].value = '1'
            p[0].exp = '1 == 1'
        else:
            p[0].value = p[1].value

    def p_const_integer(self, p):
        """const : INTEGERNUMBER"""
        p[0] = NonTerminal()
        p[0].value = p[1]

    def p_const_float(self, p):
        """const : FLOATNUMBER"""
        p[0] = NonTerminal()
        p[0].value = int(float(p[1])).__str__()

    def p_const_trueAndFalse(self, p):
        """const : TRUE
        | FALSE"""
        p[0] = NonTerminal()
        p[0].value = p[1]

    # TODO: Expression list for function
    def p_explist(self, p):
        """explist : exp
                   | explist COMMA exp"""

    # print("exp| explist COMMA exp")

    def p_empty(self, p):
        """empty :"""
        # print("empty")
        pass

    def p_error(self, p):
        print("Error", p.type, p.lexpos)

    # raise Exception('ParsingError: invalid grammar at ', p)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser

    def ensure_true_false(self, p):
        if p.true == '' and len(p.quad) == 0:
            p.true = self.new_label()
        if p.false == '' and len(p.quad) == 0:
            p.false = self.new_label()
