from ply import yacc
from lexer import Lexer
from nonTerminal import NonTerminal
from codeGenerator import CodeGenerator


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
        ('left', "ELSEIF", "ELSE"),
        ('left', "MUL", "DIV"),
    )

    def __init__(self):
        self.tempCount = 0
        self.codeGenerator = CodeGenerator()

    def new_temp(self):
        temp = "T" + str(self.tempCount)
        self.tempCount += 1
        return temp

    def p_program(self, p):
        """program : declist MAIN LRB RRB block
                    | MAIN LRB RRB block"""
        print("declist MAIN LRB RRB block| MAIN LRB RRB block")

    def p_declist(self, p):
        """declist : dec
                   | declist dec"""
        print("dec| declist dec")

    def p_dec(self, p):
        """dec : vardec
               | funcdec"""

        print("vardec| funcdec")

    def p_type(self, p):
        """type : INTEGER
                | FLOAT
                | BOOLEAN"""
        print("INTEGER| FLOAT| BOOLEAN")

    def p_iddec(self, p):
        """iddec : lvalue
                 | lvalue ASSIGN exp"""
        print("ID| ID LSB exp RSB| ID ASSIGN exp")

    def p_idlist(self, p):
        """idlist : iddec
                  | idlist COMMA iddec"""
        print("iddec| idlist COMMA iddec")

    def p_vardec(self, p):
        """vardec : idlist COLON type SEMICOLON"""
        print("idlist COLON type SEMICOLON")

    def p_funcdec(self, p):
        """funcdec : FUNCTION ID LRB paramdecs RRB COLON type block
                   | FUNCTION ID LRB paramdecs RRB block"""
        print("FUNCTION ID LRB paramdecs RRB COLON type block| FUNCTION ID LRB paramdecs RRB block")

    def p_paramdecs(self, p):
        """paramdecs : paramdecslist
                     | empty"""
        print("paramdecslist| empty")

    def p_paramdecslist(self, p):
        """paramdecslist : paramdec
                         | paramdecslist COMMA paramdec"""
        print("paramdec| paramdecslist COMMA paramdec")

    def p_paramdec(self, p):
        """ paramdec : ID COLON type
                     | ID LSB RSB COLON type"""
        print("ID COLON type| ID LSB RSB COLON type")

    def p_block(self, p):
        """block : LCB stmtlist RCB"""
        print("LCB stmtlist RCB")

    def p_stmtlist(self, p):
        """stmtlist : stmtlist stmt
                    | empty"""
        print("stmtlist stmt| empty")

    def p_lvalue(self, p):
        """lvalue : ID
                  | ID LSB exp RSB"""
        print("ID| ID LSB exp RSB")

    def p_case(self, p):
        """case : WHERE const COLON stmtlist"""
        print("WHERE const COLON stmtlist")

    def p_cases(self, p):
        """cases : cases case
                | empty"""
        print("cases case| empty")

    def p_stmt(self, p):
        """stmt : RETURN exp SEMICOLON
                | exp SEMICOLON
                | block
                | vardec
                | WHILE LRB exp RRB stmt
                | ON LRB exp RRB LCB cases RCB SEMICOLON
                | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt
                | FOR LRB ID IN ID RRB stmt
                | IF LRB exp RRB stmt elseiflist
                | IF LRB exp RRB stmt elseiflist ELSE stmt
                | PRINT LRB ID RRB SEMICOLON"""
        print(
            "RETURN exp SEMICOLON| exp SEMICOLON| block| vardec| WHILE LRB exp RRB stmt| ON LRB exp RRB LCB cases RCB SEMICOLON| FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt| FOR LRB ID IN ID RRB stmt| IF LRB exp RRB stmt elseiflist| IF LRB exp RRB stmt elseiflist ELSE stmt| PRINT LRB ID RRB")

    def p_elseiflist(self, p):
        """elseiflist : elseiflist ELSEIF LRB exp RRB stmt
                      | empty"""
        print("elseiflist ELSEIF LRB exp RRB stmt| empty")

    def p_exp(self, p):
        """exp : lvalue ASSIGN exp
               | exp GT exp
               | exp LT exp
               | exp NE exp
               | exp EQ exp
               | exp LE exp
               | exp GE exp
               | exp AND exp
               | exp OR exp
               | lvalue
               | lvalue LRB explist RRB
               | LRB exp RRB
               | lvalue LRB RRB
               | SUB exp
               | NOT exp"""
        print(
            "lvalue ASSIGN exp| exp GT exp| exp LT exp| exp NE exp| exp EQ exp| exp LE exp| exp GE exp| exp AND exp| exp OR exp| exp SUM exp| exp SUB exp| exp MUL exp| exp DIV exp| exp MOD exp| const| lvalue| ID LRB explist RRB| LRB exp RRB| ID LRB RRB| SUB exp| NOT exp")

    def p_exp_sum(self, p):
        "exp : exp SUM exp"
        print(3)
        print(p[1], p[3])
        pass
       # self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_sub(self, p):
        "exp : exp SUB exp"
        pass
        #self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_mul(self, p):
        "exp : exp MUL exp"
        pass
        #self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_div(self, p):
        "exp : exp DIV exp"
        pass
        #self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_mod(self, p):
        "exp : exp MOD exp"
        pass
        #self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_const(self, p):
        """exp : const"""
        p[0] = NonTerminal()
        p[0].value = p[1].value
        print(2)
        print(p[0])

    def p_const_integer(self, p):
        """const : INTEGERNUMBER"""
        p[0] = NonTerminal()
        p[0].value = p[1]
        print(1)


    def p_const_float(self, p):
        """const : FLOATNUMBER"""
        p[0] = NonTerminal()
        p[0].value = p[1]

    def p_const_trueAndFalse(self, p):
        """const : TRUE
        | FALSE"""
        print("TRUE| FALSE")

    def p_explist(self, p):
        """explist : exp
                   | explist COMMA exp"""
        print("exp| explist COMMA exp")

    def p_empty(self, p):
        """empty :"""
        print("empty")
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
