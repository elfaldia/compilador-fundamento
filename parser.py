import ply.yacc as yacc

# Importar tokens desde el lexer
from lexer import tokens

# Regla de gramática y su acción asociada
def p_expression_SUMA(p):
    'expression : expression SUMA expression'
    p[0] = p[1] + p[3]

def p_expression_RESTA(p):
    'expression : expression RESTA expression'
    p[0] = p[1] - p[3]

def p_expression_MULTIPLICACION(p):
    'expression : expression MULTIPLICACION expression'
    p[0] = p[1] * p[3]

def p_expression_DIVISION(p):
    'expression : expression DIVISION expression'
    p[0] = p[1] / p[3]

def p_expression_RESTO(p):
    'expression : expression RESTO expression'
    p[0] = p[1] % p[3]

def p_expression_NUMERO(p):
    'expression : NUMERO'
    p[0] = p[1]

def p_error(p):
    print("Error de sintaxis")

# Construir el parser
parser = yacc.yacc()
