import math


print('Questão 01')
numero = 0
while numero != 999:
    numero = int(input('Digite o numero\n'))
    print(numero * 3)

print('Questão 02')
contador = 0
numero = 2
while numero % 2 == 0:
    numero = int(input('Digite o numero\n'))
    contador += 1
    print(f'{contador} números foram digitados ')

print('Questão 03')
sair = ''
total = 0
contador = 0
while sair != 'sair':
    numero = int(input('Digite um numero positivo\n'))
    if numero < 0:
        continue
    else:
        total += numero
        contador += 1

    print(f'A média dos números digitados é {math.trunc(total / contador)}')
    sair = input('Digite sair para encerrar ou qualquer tecla para continuar...\n')


print('Questão 04')
numero = -1
contador = 0

while numero != 0:
    numero = int(input('Digite um numero\n'))
    if 100 < numero < 200:
        contador += 1
    print(f'Foram digitados {contador} números entre 100 e 200.')

print('Questão 05')
msg = ''
while msg != 'FIM':
    msg = input('Digite um nome\n')
    if msg != 'FIM':
        print(msg[0])

print('Questão 06')
numero = 0
while numero != 999:
    numero = int(input('Digite um numero\n'))
    if numero != 999:
        for i in range(1, numero):
            if numero % i == 0:
                print(f'{i} é divisor do número {numero}')

print('Questão 07')
populacao_total_pais_a = 5000000
tx_natalidade_pais_a = 3
populacao_total_pais_b = 7000000
tx_natalidade_pais_b = 2
tempo_necessario = 0

while populacao_total_pais_a < populacao_total_pais_b:
    tempo_necessario += 1
    total_nascidos_pais_a = populacao_total_pais_a * (tx_natalidade_pais_a / 100)
    populacao_total_pais_a += total_nascidos_pais_a
    total_nascidos_pais_b = populacao_total_pais_b * (tx_natalidade_pais_b / 100)
    populacao_total_pais_b += total_nascidos_pais_b

    if populacao_total_pais_a > populacao_total_pais_b:
        print(f'Foram necessários {tempo_necessario} anos.')

print('Questão 08')
altura_chico = 1.50
crescimento_chico = 0.02
altura_juca = 1.10
crescimento_juca = 0.03
tempo_necessario = 0

while altura_juca < altura_chico:
    tempo_necessario += 1
    altura_chico += crescimento_chico
    altura_juca += crescimento_juca

    if altura_juca > altura_chico:
        print(f'Foram necessários {tempo_necessario} anos.')

print('Questão 09')

print('Questão 10')
contador = 0
while contador < 10:
    numero = int(input('Digite um número\n'))
    if numero < 0:
        print('Não é permitido número negativo.\n')
        continue
    contador += 1
    print(f'A raiz quadrada de {numero} é {math.sqrt(numero)}')
