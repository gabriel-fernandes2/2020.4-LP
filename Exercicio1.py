# Atividade 1 - Idade

# Gabriel S. Fernandes

iDias = int(input('Digite sua idade em dias: '))
ano = int(iDias / 365)
mes = int((iDias % 365) / 30)
dia = int((iDias % 365) % 30)

print('Sua idade é: {} anos, {} meses e {} dias'.format(ano, mes, dia))
