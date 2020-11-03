# Atividade 5 - Frase Invertida

# Gabriel S. Fernandes

frase = input('Digite uma frase: ')
invertida = ' '.join(palavra[::-1] for palavra in frase.split())
print('Sua frase invertida fica: {}'.format(invertida))