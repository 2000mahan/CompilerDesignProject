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
        'true': 'TRUE',
        'false': 'FALSE',
        'return': 'RETURN',
        'fun': 'FUNCTION',
        'main': 'MAIN',
        'on': 'ON',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',
        'in': 'IN',
    }
    # Colons
    t_SEMICOLON = r';'
    t_COLON = r':'
    t_COMMA = r','
    # Operators
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_ASSIGN = r'='
    t_LT = r'\<'
    t_GT = r'\>'
    # Brackets
    t_LCB = r'\{'
    t_RCB = r'\}'
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LSB = r'\[>'
    t_RSB = r'\]>'

    def t_FLOATNUMBER(self, t):
        
        return t

    def t_INTEGERNUMBER(self, t):
        r'[+-]?[1-9][0-9]{8}'
        return t

    def t_ID(self, t):
        r'[a-z][a-zA-Z_0-9]*'
        if t.value in self.reserved:
            t.type = self.reserved[t.value]  # Check for reserved words
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore = '\t'

    # Error handling rule
    def t_error(self, t):
        raise Exception('Error at', t.value)

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module = self, **kwargs)
        return self.lexer