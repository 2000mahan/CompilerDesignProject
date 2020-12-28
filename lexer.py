from ply import lex


class Lexer:
    tokens = [
        'ID', 'INTEGERNUMBER', 'FLOATNUMBER', 'INTEGER', 'FLOAT',
        'BOOLEAN', 'FUNCTION', 'TRUE', 'FALSE', 'PRINT', 'RETURN',
        'MAIN', 'IF', 'ELSE', 'ELSEIF', 'WHILE', 'ON', 'WHERE', 'FOR',
        'AND', 'OR', 'NOT', 'IN', 'ASSIGN', 'SUM', 'SUB', 'MUL', 'DIV',
        'MOD', 'GT', 'GE', 'LT', 'LE', 'EQ', 'NE', 'LCB', 'RCB',
        'LRB', 'RRB', 'LSB', 'RSB', 'SEMICOLON', 'COLON', 'COMMA', 'ERROR'
    ]
    reserved = {
        # Conditional
        'if': 'IF',
        'then': 'THEN',
        'else': 'ELSE',
        'elseif': 'ELSEIF',
        # Loops
        'for': 'FOR',
        'while': 'WHILE',
        # Types
        'int': 'INTEGER',
        'float': 'FLOAT',
        'bool': 'BOOLEAN',
        # Other Keywords
        'print': 'PRINT',
        'True': 'TRUE',
        'False': 'FALSE',
        'return': 'RETURN',
        'fun': 'FUNCTION',
        'main': 'MAIN',
        'on': 'ON',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',
        'in': 'IN',
        'where': 'WHERE'
    }
    # Colons
    t_SEMICOLON = r';'
    t_COLON = r':'
    t_COMMA = r','
    # Operators
    t_MUL = r'\*'
    t_DIV = r'/'
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MOD = r'%'
    t_ASSIGN = r'='
    t_GT = r'>'
    t_GE = r'>='
    t_LT = r'<'
    t_LE = r'<='
    t_EQ = r'=='
    t_NE = r'!='
    # Brackets
    t_LCB = r'{'
    t_RCB = r'}'
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LSB = r'\['
    t_RSB = r'\]'

    def t_TRUE(self, t):
        r'True'
        return t

    def t_FALSE(self, t):
        r'False'
        return t

    def t_ERROR(self, t):
        r"""([0-9]{10,})(\.[0-9]+)
       |([0-9]{10,})
       |([0-9]+)(\.[0-9]+){2,}
        |([A-Z])+[a-zA-Z_0-9]+
        |[0-9]+[a-z_A-Z][a-zA-Z_0-9]*
        |[\+\-\%\/\*](\s*[\+\-\%\/\*]+)+
        |ERROR
        """
        return t

    def t_newline(self, t):
        r""""\n+"""
        t.lexer.lineno += len(t.value)

    t_ignore = '\n \t \r '

    def t_FLOATNUMBER(self, t):
        r"""[0-9]{1,9}\.[0-9]+"""
        t.value = str(float(t.value))
        return t

    def t_INTEGERNUMBER(self, t):
        r"""[0-9]{1,9}"""
        t.value = str(int(t.value))
        return t

    def t_ID(self, t):
        r"""[_a-z][a-zA-Z_0-9]*"""
        if t.value in self.reserved:
            t.type = self.reserved[t.value]
        return t

    def t_error(self, t):
        raise Exception('Error at', t.value)

    def build(self, **kwargs):
        """
        build the lexer
        """
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer
