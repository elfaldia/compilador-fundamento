from lexer import lexer
from parser import parser

# Función principal
def main():
    while True:
        try:
            s = input('> ')  # Leer entrada del usuario
        except EOFError:
            break
        parser.parse(s)  # Parsear la entrada

if __name__ == '__main__':
    main()