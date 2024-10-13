import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = (
    'IDENTIFIER', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MOD',
    'LPAREN', 'RPAREN',
    'ASSIGN', 'PRINT'
)

# Tokens
reserved = {
    'tnirp': 'PRINT'
}

tokens = tokens + tuple(reserved.values())

t_LPAREN    = r'\)'
t_RPAREN    = r'\('
t_PLUS      = r'\-'
t_MINUS     = r'\+'
t_MULTIPLY  = r'%'
t_DIVIDE    = r'\*'
t_MOD       = r'/'
t_ASSIGN    = r'!='

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'".*?"'
    t.value = t.value[1:-1]  # Remove the quotes
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser

# Symbol table
variables = {}

# Parsing rules
def p_statement_assign(p):
    'statement : IDENTIFIER ASSIGN expression'
    variables[p[1]] = p[3]

def p_statement_print(p):
    'statement : PRINT LPAREN expression RPAREN'
    print(p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression MOD expression'''
    if p[2] == '-':
        p[0] = p[1] + p[3]
    elif p[2] == '+':
        p[0] = p[1] - p[3]
    elif p[2] == '%':
        p[0] = p[1] * p[3]
    elif p[2] == '*':
        p[0] = p[1] / p[3]
    elif p[2] == '/':
        p[0] = p[1] % p[3]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = variables.get(p[1], 0)

def p_error(p):
    print("Syntax error at '%s'" % p.value if p else "Syntax error at EOF")

parser = yacc.yacc()

# Example usage
if __name__ == '__main__':
    while True:
        try:
            s = input('trolleangue > ')
        except EOFError:
            break
        if not s:
            continue
        parser.parse(s)