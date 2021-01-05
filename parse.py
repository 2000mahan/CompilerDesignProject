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
        self.codeGenerator = CodeGenerator()

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
        """d : funcdec"""
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
        self.codeGenerator.generate_assign(p, True)

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
        #print("FUNCTION ID LRB paramdecs RRB COLON type block| FUNCTION ID LRB paramdecs RRB block")
        pass

    # TODO: Function parameters decleration
    def p_paramdecs(self, p):
        """paramdecs : paramdecslist
                     | empty"""
        #print("paramdecslist| empty")
        pass

    # TODO: Function parameter list decleration
    def p_paramdecslist(self, p):
        """paramdecslist : paramdec
                         | paramdecslist COMMA paramdec"""
        #print("paramdec| paramdecslist COMMA paramdec")
        pass

    # TODO: Function parameter decleration
    def p_paramdec(self, p):
        """ paramdec : ID COLON type
                     | ID LSB RSB COLON type"""
        #print("ID COLON type| ID LSB RSB COLON type")
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
        self.codeGenerator.generatelvalue_from_array(p, self.new_temp())

    def p_case(self, p):
        """case : WHERE const COLON stmtlist"""
        #print("WHERE const COLON stmtlist")
        pass

    def p_cases(self, p):
        """cases : cases case
                | empty"""
        #print("cases case| empty")
        pass

    # TODO: Loops and conditionals
    def p_stmt(self, p):
        """stmt : RETURN exp SEMICOLON
                | WHILE LRB exp RRB stmt
                | ON LRB exp RRB LCB cases RCB SEMICOLON
                | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt
                | FOR LRB ID IN ID RRB stmt"""
        pass

    def p_stmt_vardec(self, p):
        """stmt : vardec"""
        p[0] = NonTerminal()
        p[0].next = self.new_label()
        p[0].code = p[1].code + ";\n"

    def p_stmt_print(self, p):
        """stmt : PRINT LRB ID RRB SEMICOLON"""
        self.codeGenerator.generate_print(p, self.new_label())

    def p_stmt_from_block(self, p):
        """stmt : block"""
        p[0] = NonTerminal()
        p[0].next = p[1].next
        p[0].begin = p[1].begin
        p[0].code = p[1].code

    def p_stmt_from_exp(self, p):
        """stmt : exp SEMICOLON"""
        self.codeGenerator.generate_statement_from_exp(p, self.new_label())

    def p_stmt_if(self, p):
        """stmt : IF LRB exp RRB stmt elseiflist %prec p1
                | IF LRB exp RRB stmt elseiflist ELSE stmt"""
        p[0] = NonTerminal()
        if len(p) == 9:
            if p[8].begin == '':
                p[8].begin = self.new_label()
            self.codeGenerator.generate_if(p, p[8].begin, 3, 5, False)
        else:
            if p[5].begin == '':
                p[5].begin = self.new_label()
            self.codeGenerator.generate_if(p, self.new_label(), 3, 5, False)

    def p_elseiflist(self, p):
        """elseiflist : elseiflist ELSEIF LRB exp RRB stmt
                      | empty"""
        p[0] = NonTerminal()
        if p[1] is None:
            self.codeGenerator.generate_empty_elseif_list(p, self.new_label())
        else:
            self.codeGenerator.generate_elseif_list(p, self.new_label())

    def p_exp_relop(self, p):
        """exp : exp GT exp
               | exp LT exp
               | exp NE exp
               | exp EQ exp
               | exp LE exp
               | exp GE exp"""
        self.codeGenerator.generate_boolean_relop_code(p, self.new_temp(), self.new_label(), self.new_label(), self.new_label())

    def p_exp_or(self, p):
        """exp : exp OR exp"""
        p[0] = NonTerminal()
        p[3].begin = p[1].false
        p[0].false = p[3].false
        p[0].quad.extend([p[1], p[2], p[3]])
        p[1].generate_boolean_code()
        p[3].generate_boolean_code()
        print(p[1].code)
        print(p[3].code)

    def p_exp_and(self, p):
        """exp : exp AND exp"""
        p[0] = NonTerminal()
        p[3].begin = p[1].true
        p[0].true = p[3].true
        p[0].quad.extend([p[1], p[2], p[3]])
        p[1].generate_boolean_code()
        p[3].generate_boolean_code()
        print(p[1].code)
        print(p[3].code)

    def p_exp_not(self, p):
        """exp : NOT exp"""
        p[0] = NonTerminal()
        p[0].false = p[2].true
        p[0].true = p[2].false
        p[0].quad.extend([p[2], p[1]])
        p[2].generate_boolean_code()
        print(p[2].code)

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
        self.codeGenerator.generate_paran_exp(p, self.new_temp())

    def p_exp_assign(self, p):
        """exp : lvalue ASSIGN exp"""
        self.codeGenerator.generate_assign(p, False)

    def p_exp_neg(self, p):
        """exp : SUB exp"""
        self.codeGenerator.generate_negation_code(p, self.new_temp())

    def p_exp_sum(self, p):
        """exp : exp SUM exp"""
        self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_sub(self, p):
        "exp : exp SUB exp"
        self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_mul(self, p):
        "exp : exp MUL exp"
        self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_div(self, p):
        "exp : exp DIV exp"
        self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_mod(self, p):
        "exp : exp MOD exp"
        self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_const(self, p):
        """exp : const"""
        p[0] = NonTerminal()
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


#lexer = Lexer().build()
#file = open('test2.txt')
#text_input = file.read()
#file.close()
#lexer.input(text_input)

#parser = Parser()
#parser.build().parse(text_input, lexer, False)
