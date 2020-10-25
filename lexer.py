from ply import lex

class lexer:

    tokens = {
       'ID', 'INTEGERNUMBER', 'FLOATNUMBER', 'INTEGER', 'FLOAT',
        'BOOLEAN', 'FUNCTION', 'TRUE', 'FALSE', 'PRINT', 'RETURN',
        'MAIN', 'IF', 'ELSE', 'ELSEIF', 'WHILE', 'ON', 'WHERE', 'FOR',
        'AND', 'OR', 'NOT', 'IN', 'ASSIGN', 'SUM', 'MUL', 'DIV',
        'MOD', 'GT', 'GE', 'LT', 'LE', 'EQ', 'NE', 'LCB', 'RCB',
        'LRB', 'RRB', 'LSB', 'RSB', 'SEMICOLON', 'COLON', 'COMMA', 'ERROR!'
    }
