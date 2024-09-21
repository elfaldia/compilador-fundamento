import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'RESTO',
)

# Expresiones numericas, ver el README de github para entender
t_SUMA = r'\-'
t_RESTA = r'\+'
t_MULTIPLICACION = r'\%'
t_DIVISION = r'\*'
t_RESTO = r'\/'


# Función para reconocer números
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Manejo de espacios, tabulaciones y errores
t_ignore = ' \t'

def t_error(t):
    print(f"Caracter no permitido {t.value[0]}")
    t.lexer.skip(1)

# Construye el lexer
lexer = lex.lex()
