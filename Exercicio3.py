# Atividade 3 - Maior número

# Gabriel S. Fernandes

primeiro = int(input("Digite o primeiro numero: "))
segundo = int(input("Digite o segundo numero: "))
terceiro = int(input("Digite o terceiro numero: "))
maiornum = primeiro

if segundo > maiornum :
        maiornum = segundo

if terceiro > maiornum :
        maiornum = terceiro

print('O maior numero é: {} '.format(maiornum))