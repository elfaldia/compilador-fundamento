import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
)

# Expresiones regulares para los tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_NUMBER = r'\d+'

# Regla para ignorar espacios en blanco
def t_whitespace(t):
    r'\s+'
    pass

# Regla para manejar errores
def t_error(t):
    print(f"Caracter inesperado '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()
