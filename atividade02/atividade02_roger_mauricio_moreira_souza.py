import math

print('Questão 01\n')
primeiro_numero: int = int(input('Digite o primeiro número\n'))
segundo_numero: int = int(input('Digite o segundo número\n'))
quociente = primeiro_numero / segundo_numero
resto = primeiro_numero % segundo_numero

print('Dividendo: ', primeiro_numero)
print('Divisor: ', segundo_numero)
print('Quociente: ', quociente)
print('Resto: ', resto)

print('\nQuestão 02\n')
peso_01 = 1
peso_02 = 2
peso_03 = 3
peso_04 = 4
n1: int = int(input('Digite o primeiro número\n'))
n2: int = int(input('Digite o segundo número\n'))
n3: int = int(input('Digite o terceiro número\n'))
n4: int = int(input('Digite o quarto número\n'))
media_ponderada = (peso_01 * n1 + peso_02 * n2 + peso_03 * n3 + peso_04 * n4) / (peso_01 + peso_02 + peso_03 + peso_04)
print('Media ponderada é igual: ', media_ponderada)

print('\nQuestão 03\n')
nome = input('Digite um nome:\n')
tamanho_nome: int = len(nome)
print('Nome completo:', nome)
print('Primeiro caracter:', nome[0])
print('Último caracter:', nome[tamanho_nome - 1])
print('Primeiro ao terceiro caracter:', nome[0:3])
print('Quarto caracter:', nome[5])
print('Dois últimos caracteres:', nome[tamanho_nome - 2:tamanho_nome])

print('\nQuestão 04\n')
valor_hora_aula: float = float(input('Digite o valor da aula por hora\n'))
aulas_dadas: int = int(input('Digite a quantidade de aulas dadas\n'))
percentual_desconto_inss: int = int(input('Digite o percentual de desconto do INSS\n'))
salario_liquido: float = (valor_hora_aula * 8 * aulas_dadas) * ((100 - percentual_desconto_inss) / 100)
print('O salário líquido é:', salario_liquido)

print('\nQuestão 05\n')
tempo_gasto: int = int(input('Digite o tempo gasto\n'))
velocidade_media: int = int(input('Digite a velocidade média\n'))

print('\nQuestão 08\n')
numero: int = int(input('Digite um número de 3 dígitos\n'))
numero_invertido: int = int(str(numero)[::-1])
soma = numero + numero_invertido
primeiro_digito: int = math.trunc((soma - soma % 100) / 100)
segundo_digito: int = math.trunc(soma % 100 / 10)
terceiro_digito: int = soma % 10
digito_verificador = (primeiro_digito * 1 + segundo_digito * 2 + terceiro_digito * 3) % 10
print('O digito verificador é:', digito_verificador)

print('\nQuestão 09\n')
frase = input('Digite uma frase\n')
frase_invertida = frase[::-1]
print(frase_invertida)

print('\nQuestão 10\n')
frase: str = 'Python é muito legal'
python = frase[0:5]
eh = frase[7]
muito = frase[9:14]
legal = frase[15: len(frase)]
print(python)
print(eh)
print(muito)
print(legal)
print('Tamanho da frase:' ,len(frase))
print('Tamanho da frase -> python:' ,len(python))
print('Tamanho da frase -> é:' ,len(eh))
print('Tamanho da frase -> muito:' ,len(muito))
print('Tamanho da frase -> legal:' ,len(legal))
