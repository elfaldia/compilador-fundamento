import ply.yacc as yacc

# Importar tokens desde el lexer
from lexer import tokens

# Reglas de gramatica

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]
def p_term_factor(p):
    'term : factor'
    p[0] = p[1]
def p_factor_NUMERO(p):
    'factor : NUMERO'
    p[0] = p[1]
def p_factor_expr(p):
    'factor : PARENTECISIZQ expression PARENTECISDER'
    p[0] = p[2]

#Reglas de matematica
def p_expression_SUMA(p):
    'expression : expression SUMA term'
    p[0] = p[1] + p[3]

def p_expression_RESTA(p):
    'expression : expression RESTA term'
    p[0] = p[1] - p[3]

def p_expression_MULTIPLICACION(p):
    'term : term MULTIPLICACION factor'
    p[0] = p[1] * p[3]

def p_expression_DIVISION(p):
    'term : term DIVISION factor'
    p[0] = p[1] / p[3]

def p_expression_RESTO(p):
    'term : term RESTO factor'
    p[0] = p[1] % p[3]

def p_error(p):
    print("Error de sintaxis")

# Construir el parser
parser = yacc.yacc()
