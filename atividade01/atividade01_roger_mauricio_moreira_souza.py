import math

# Aluno: Roger Maurício M. Souza
# INF032D 2021.2

# questao 1
print('1 - Calcule o resto da divisão de 10 por 3')
resto = 10 % 3
print(resto)

# questao 2
print('\n2 - Calcule a tabuada do 13.')
treze = 13
dez = 10
print(treze * (dez - 9), treze * (dez - 8), treze * (dez - 7), treze * (dez - 6), treze * (dez - 5), treze * (dez - 4),
      treze * (dez - 3), treze * (dez - 2), treze * (dez - 1), treze * dez)

# questao 3
print('\n3 - Davinir não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75% delas.\n'
      'Ele quer saber quantas aulas pode faltar, sabendo que tem duas aulas por semana, durante quatro meses.\n'
      'Ajude o Davinir!')

porcentagemdeaula = 0.75
aulasporsemana = 2
semanaspormes = 4
aulaspormes = aulasporsemana * semanaspormes
duracaodasaulasemmeses = 4
totalDeAulas = aulaspormes * duracaodasaulasemmeses
totalDeAulasQuePodeFaltar = totalDeAulas - (totalDeAulas * porcentagemdeaula)
print(totalDeAulasQuePodeFaltar)

# questao 4
print('\n4 - Calcule a área de um círculo de raio r = 2. \n'
      'Lembrete: a área de um círculo de raio r é: A = pi.r^2')
raiodocirculo = 2
areadocirculo = math.pi * (raiodocirculo ** raiodocirculo)
print(areadocirculo)

# questao 5
print('\n5 - Quantos segundos há em 3 horas, 23 minutos e 17 segundos?')
horasemsegundos = 3 * 60 * 60
minutosemsegundos = 23 * 60
segundos = 17
totaldesegundos = horasemsegundos + minutosemsegundos + segundos
print(totaldesegundos)

# questao 6
print('\n6 - Se você correr 65 quilômetros em 3 horas, 23 minutos e 17 segundos, '
      'qual é a sua velocidade média em m/s?')
quilometros = 65
metros = quilometros * 1000
velocidademedia = metros / totaldesegundos
print(velocidademedia)

# questao 7
print(
    '\n7 - Uma figura cujo ângulo e 80 graus. Imprima o seno, co-seno, tangente, secante, cp-secante, e co-tangente. ')
oitentagraus = 80
grausemradianos = oitentagraus * math.pi / 180
seno = math.sin(grausemradianos)
cosseno = math.cos(grausemradianos)
tangente = math.tan(grausemradianos)
secante = 1 / seno
cosecante = 1 / cosseno
cotangente = 1 / tangente
print(seno)
print(cosseno)
print(tangente)
print(secante)
print(cosecante)
print(cotangente)

# questao 8
print('\n8 - Supondo um numero 123, imprimi-lo invertido. Exemplo (123, 321).\n'
      'O numero deverá ser armazenado em outra  variável.')
numero = 123
tres = numero % 10
vinte = numero % 100 - tres
cem = numero - numero % 100
numeroinvertido = (tres * cem) + vinte + (cem // cem)
print(numeroinvertido)

# questao 9
print(
    '\n9 - Supondo um retângulo de 10cm de base e 5cm de altura,\n imprimir a seguinte saída perímetro: / área: / diagonal: ')
base = 10.0
altura = 5.0
area = base * altura
perimetro = 2 * (base + altura)
baseaoquadrado = base ** 2
alturaaoquadrado = altura ** 2
diagonal = math.sqrt(baseaoquadrado + alturaaoquadrado)

print(area)
print(perimetro)
print(diagonal)

# questao 10
print(
    '\n10 - Dado os valores das variáveis a=5 e b=12,\n efetuar a troca de forma que (A) passe ter o valor de (B) e vice-versa.\n'
    'Apresentar os valores invertidos.')
a = 5
b = 12
print(a, b)
a, b = b, a
print(a, b)

# questao 11
print('\n11 - Você e os outros integrantes da sua república (Joca, Moacir, Demival e Jackson)\n '
      'foram no supermercado e compraram alguns itens:\n'
      '75 latas de cerveja: R$ 2,20 cada (da ruim ainda, pra fazer o dinheiro render)\n'
      '2 pacotes de macarrão: R$ 8,73 cada\n'
      '1 pacote de Molho de tomate: R$ 3,45\n'
      '420g Cebola: R$ 5,40/kg\n'
      '250g de Alho: R$ 30/kg\n'
      '450g de pães franceses: R$ 25/kg\n'
      'Calcule quanto ficou para cada um:')
quilo = 1000.0
cervejas = 75 * 2.20
macarrao = 2 * 8.73
molhodetomate = 3.45
cebola = (420 / quilo) * 5.40
alho = (250 / quilo) * 30.0
paes = (450 / quilo) / 25.0
subtotalparacadaum = (cervejas + macarrao + molhodetomate + cebola + alho + paes) / 4
print(subtotalparacadaum)
# questao 12
print(
    '\nKrissia gosta de bolinhas de queijo. Ela quer saber quantas bolinhas de queijo dá para colocar dentro de um pote de sorvete de 2L.\n'
    ' Ela pensou assim: Um pote de sorvete tem dimensões 15 cm x 10 cm x 13 cm. Uma bolinha de queijo é uma esfera de raio r = 1.2 cm.\n'
    'O fator de empacotamento ideal é 0.74, mas o pote de sorvete tem tamanho comparável às bolinhas de queijo, aí \n'
    'tem efeitos de borda, então o fator deve ser menor. Mas as bolinhas de queijo são razoavelmente elásticas, então \n'
    'empacota mais. Esse valor parece razoável. \n'
    'Sabendo que o volume de uma esfera de raio r é V = 4 3πr^3, o volume do pote de sorvete é V = x· y · z e o fator \n'
    'de empacotamento é a fração de volume ocupado pelas bolinhas de queijo. Ou seja, 74% do pote de sorvete vai \n'
    'ser ocupado pelas bolinhas de queijo. Ajude a Krissia descobrir quantas bolinhas de queijo cabem no pote de sorvete!')
raiodaesfera = 1.2
volumedopoteemcentimetroscubicos = 2000
volumedabolinhadequeijo = (4 * math.pi * math.pow(raiodaesfera, 3)) / 3
totaldebolinhasquecabemnopote = volumedopoteemcentimetroscubicos / volumedabolinhadequeijo
print(totaldebolinhasquecabemnopote)
