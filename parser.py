from ply import yacc
from lexer import Lexer


class Parser:
    tokens = Lexer().tokens

    precedence = (

        # Statements
        ('left', "WHILE", "FOR", "ON"),
        ('left', "IN"),
        ('left', "IF"),
        ('left', "ELSE"),
        ('left', "ELSEIF"),
        ('left', "WHERE"),
        ('left', "PRINT"),
        ('left', "RETURN"),
        ('right', "ASSIGN"),

        # High-level Boolean Operators
        ('left', "OR"),
        ('left', "AND"),

        # Low-level Boolean Operators
        ('left', "GT", "LT", "NE", "EQ", "LE", "GE"),

        # Numeric Operators
        ('left', "MOD"),
        ('left', "SUM", "SUB"),
        ('left', "MUL", "DIV"),

        # Braces
        ('left', "LCB", "RCB"),
        ('left', "LSB", "RSB"),
        ('left', "LRB", "RRB"),

        # Atoms
        ('left', "INTEGERNUMBER"),
        ('left', "FLOATNUMBER"),
        ('left', "TRUE", "FALSE"),

        # Type Identifiers
        ('left', "INTEGER"),
        ('left', "FLOAT"),
        ('left', "BOOLEAN"),

        # Identifier
        ('left', "ID"),
        ('left', "FUNCTION"),
        ('left', "MAIN"),

        # Low-level Misc
        ("left", "SEMICOLON", "COLON"),

        # Error
        ("left", "ERROR")
    )

    def __init__(self):
        pass

    def p_program(self, p):
        """program : declist MAIN LRB RRB block"""
        print("declist MAIN LRB RRB block")

    def p_declist(self, p):
        """declist : dec
                   | declist dec
                   | empty"""
        print("dec| declist dec| empty")

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
        """iddec : ID
                 | ID LSB exp RSB
                 | ID ASSIGN exp"""
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
        """stmtlist : stmt
                    | stmtlist stmt
                    | empty"""
        print("stmt| stmtlist stmt| empty")

    def p_lvalue(self, p):
        """lvalue : ID
                  | ID LSB exp RSB"""
        print("ID| ID LSB exp RSB")

    def p_case(self, p):
        """case : WHERE const COLON stmtlist"""
        print("WHERE const COLON stmtlist")

    def p_cases(self, p):
        """cases : case
                | cases case
                | empty"""
        print("casecases case| empty")


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
                | PRINT LRB ID RRB"""
        print("RETURN exp SEMICOLON| exp SEMICOLON| block| vardec| WHILE LRB exp RRB stmt| ON LRB exp RRB LCB cases RCB SEMICOLON| FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt| FOR LRB ID IN ID RRB stmt| IF LRB exp RRB stmt elseiflist| IF LRB exp RRB stmt elseiflist ELSE stmt| PRINT LRB ID RRB")


    def p_elseiflist(self, p):
        """elseiflist : ELSEIF LRB exp RRB stmt
                      | elseiflist ELSEIF LRB exp RRB stmt
                      | empty"""
        print("ELSEIF LRB exp RRB stmt| elseiflist ELSEIF LRB exp RRB stmt| empty")


    def p_relopexp(self, p):
        """relopexp : exp relop exp
                    | relopexp relop exp"""
        print("exp relop exp| relopexp relop exp")


    def p_exp(self, p):
        """exp : lvalue ASSIGN exp
               | exp operator exp
               | relopexp
               | const
               | lvalue
               | ID LRB explist RRB
               | LRB exp RRB
               | ID LRB RRB
               | SUB exp
               | NOT exp"""
        print("lvalue ASSIGN exp| exp operator exp| relopexp| const| lvalue| ID LRB explist RRB| LRB exp RRB| ID LRB RRB| SUB exp| NOT exp")

    def p_operator(self, p):
        """operator : AND
                    | OR
                    | SUM
                    | SUB
                    | MUL
                    | DIV
                    | MOD"""
        print("AND| OR| SUM| SUB| MUL| DIV| MOD")

    def p_const(self, p):
        """const : INTEGERNUMBER
                 | FLOATNUMBER
                 | TRUE
                 | FALSE"""
        print("INTEGERNUMBER| FLOATNUMBER| TRUE| FALSE")

    def p_relop(self, p):
        """relop : GT
                 | LT
                 | NE
                 | EQ
                 | LE
                 | GE"""
        print("GT| LT| NE| EQ| LE| GE")

    def p_explist(self, p):
        """explist : exp
                   | explist COMMA exp"""
        print("exp| explist COMMA exp")

    def p_empty(self, p):
        """empty :"""
        print("empty")
        pass

    def p_error(self, p):
        print("p.value")
       # raise Exception('ParsingError: invalid grammar at ', p)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser

lexer = Lexer().build()
file = open('test3.txt')
text_input = file.read()
file.close()
lexer.input(text_input)

parser = Parser()
parser.build().parse(text_input, lexer, False)




