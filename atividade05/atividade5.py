print('Questão 1')
valor = int(input('Digite um valor:\n'))
if 19 < valor < 91:
    print('Valor está entre 20 e 90')
else:
    print('Valor não está entre 20 e 90')

print('Questão 2')
pessoa = {}
pessoa['nome'] = input('Digite seu nome:\n')
pessoa['idade'] = int(input('Digite sua idade:\n'))
pessoa['sexo'] = input('Digite seu sexo:\n')
if pessoa['sexo'] == 'feminino' and pessoa['idade'] < 25:
    print('ACEITA')
else:
    print('NÃO ACEITA')

print('Questão 3')
sigla_estado = input('Digite a sigla do estado:\n')
if sigla_estado == 'RJ':
    print('carioca')
elif sigla_estado == 'SP':
    print('paulista')
elif sigla_estado == 'MG':
    print('mineira')
else:
    print('outros estados')

print('Questão 4')
primeiro_numero = int(input('Digite o primeiro número:\n'))
segundo_numero = int(input('Digite o segundo número:\n'))
if primeiro_numero > segundo_numero:
    print(primeiro_numero)
else:
    print(segundo_numero)

print('Questão 5')
primeiro_numero = int(input('Digite o primeiro número:\n'))
segundo_numero = int(input('Digite o segundo número:\n'))
terceiro_numero = int(input('Digite o terceiro número:\n'))
if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
    print(primeiro_numero)
elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
    print(segundo_numero)
else:
    print(terceiro_numero)

print('Questão 6')
primeiro_numero = int(input('Digite o primeiro número:\n'))
segundo_numero = int(input('Digite o segundo número:\n'))
terceiro_numero = int(input('Digite o terceiro número:\n'))
menor = 0
maior = 0
intermediario = 0
if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
    maior = primeiro_numero
elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
    maior = segundo_numero
else:
    print(terceiro_numero)

# print('Questão 7')
print('Questão 8')
pessoa = {}
pessoa['nome'] = input('Digite seu nome:\n')
pessoa['nota1'] = float(input('Digite primeira nota:\n'))
pessoa['nota2'] = float(input('Digite segunda nota:\n'))
pessoa['media'] = (pessoa['nota1'] + pessoa['nota2']) / 2.0

if pessoa['media'] > 7:
    print(pessoa, 'APROVADO')
elif pessoa['media'] < 4:
    print(pessoa, 'REPROVADO')
else:
    print(pessoa, 'PROVA FINAL')

print('Questão 9')
valor_produto = float(input('Digite o valor do produto:\n'))
if valor_produto < 20:
    valor_produto = valor_produto + valor_produto * 0.45
    print(valor_produto)
else:
    valor_produto = valor_produto + valor_produto * 0.30
    print(valor_produto)

print('Questão 10')
nome_municipio = input('Digite o nome do municipio:\n')
eleitores_aptos = int(input('Digite a quantidade de eleitores aptos:\n'))
votos_candidato = int(input('Digite a quantidade de votos do candidato:\n'))
porcentagem_votos = (votos_candidato * 100) / eleitores_aptos
print(porcentagem_votos)
if eleitores_aptos > 20000 and porcentagem_votos < 50:
    print(f'No municipio {nome_municipio} terá segundo turno')
else:
    print(f'No municipio {nome_municipio} não terá segundo turno')

print('Questão 11')
numero = int(input('Digite um numero:\n'))
if numero >= 20:
    print('o número é igual ou maior que 20')
else:
    print('o número é menor que 20')

print('Questão 12')
primeiro_numero = int(input('Digite o primeiro número:\n'))
segundo_numero = int(input('Digite o segundo número:\n'))
valor_total = primeiro_numero + segundo_numero
if valor_total > 20:
    valor_total += 8
    print(valor_total)
else:
    valor_total -= 5
    print(valor_total)
print('Questão 13')
numero = int(input('Digite o número:\n'))
if numero % 3 == 0:
    print('é múltiplo de 3')
else:
    print('não é múltiplo de 3')
print('Questão 14')
numero = int(input('Digite o número:\n'))
if numero % 5 == 0:
    print('é divisível por 5')
else:
    print('não é divisível por 5')
# print('Questão 15')