import ply.lex as lex
import ply.yacc as yacc
from lexer import lexer
from parser import parser

def ejecutar_instrucciones(instrucciones):
    """
    Ejecuta las instrucciones procesadas.
    """
    for instruccion in instrucciones:
        if isinstance(instruccion, tuple) and instruccion[0] == "print":
            print(instruccion[1])

def main():
    block = ""
    open_blocks = 0

    while True:
        try:
            s = input('Trolleangue > ')
        except EOFError:
            break

        if not s.strip():
            continue

        open_blocks += s.count('}')
        open_blocks -= s.count('{')

        block += s + "\n"

        if open_blocks == 0 and block.strip():
            lexer.input(block)
            result = parser.parse(block)
            if result is not None:
                ejecutar_instrucciones(result)  # Solo ejecuta el bloque seleccionado
            block = ""

if __name__ == '__main__':
    main()
