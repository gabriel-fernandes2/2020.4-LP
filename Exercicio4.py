# Atividade 4 - Numero Primo

# Gabriel S. Fernandes

numero = int(input("Digite um número: "))
if numero < 2:
    print('O número {} não é primo'.format(numero))
elif numero == 2:
    print('O número {} é primo'.format(numero))
elif numero % 2 == 0:
    print('O número {} não é primo'.format(numero))
else:

    for i in range(3, numero // 2, 2):
        if numero % i == 0:
            print('O número {} não é primo'.format(numero))
            break
    else:
        print('O número {} é primo'.format(numero))