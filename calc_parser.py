import ply.yacc as yacc
from calc_lexer import tokens

# Definir la gramática
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_number(p):
    'term : NUMBER'
    p[0] = int(p[1])

def p_error(p):
    print("Error de sintaxis en '%s'" % p.value if p else "Error de sintaxis en EOF")

# Construir el analizador sintáctico
parser = yacc.yacc()

def parse(data):
    return parser.parse(data)
