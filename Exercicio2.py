# Atividade 2 - Triangulo e area

# Gabriel S. Fernandes

import math
a = int(input("Digite o lado do triângulo A: "))
b = int(input("Digite o lado do triângulo B: "))
c = int(input("Digite o lado do triângulo C: "))

if a > b + c:
    print('As medidas não formam um triângulo')
else:
    p = (a + b + c)/ 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('As medidas formam um triângulo com area de: {:.4f}'.format(area))