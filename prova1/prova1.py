# Roger Maurício M. Souza
# 04/11/2021

print('Questao 1')
numero = 1
while numero > 0:
    fatorial = 1
    numero = int(input('Digite um numero\n'))
    aux = numero
    if numero < 0:
        break
    while aux > 1:
        fatorial *= aux
        aux -= 1
    print(f'O fatorial de {numero} é {fatorial}')

print('Questao 2')
sair = ''

while sair != '1':
    dividendo = int(input('Digite o dividendo\n'))
    divisor = dividendo - 1

    if dividendo <= 0 or divisor <= 0:
        print('Os precisam ser inteiros positivos.')
        continue
    elif divisor > dividendo:
        print('O divisor não pode ser maior que o dividendo.')
        continue

    while divisor > 0:
        print(f'O resto da divisão entre {dividendo} e {divisor} -> {dividendo % divisor}')
        divisor -= 1

    sair = input('Digite 1 para sair ou qualquer tecla diferente para continuar...\n')

print('Questao 3')
perda_de_massa = 0.25
tempo_total = 0
sair = ''
aux = True
massa = 0

while sair != '1':
    if aux:
        massa = int(input('Digite o valor da massa\n'))

    aux = False
    massa -= perda_de_massa
    tempo_total += 30
    if massa < 0.10:
        print(f'O tempo total foi {tempo_total / 60} minutos')
        aux = True
        sair = input('Digite 1 para sair ou qualquer tecla diferente para continuar...\n')
