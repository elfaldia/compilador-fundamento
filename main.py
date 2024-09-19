from calc_parser import parse

# Prueba del parser con una expresión simple
expression = "3 + 5 - 2"
result = parse(expression)
print(f"Resultado de '{expression}' es {result}")
