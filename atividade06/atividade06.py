import math


# print('Questão 01\n')
# peso_maximo_estabelecido = 50
# multa_por_quilo_excedente = 4.0
# while True:
#     quilo_excedente = 0
#     multa = 0
#     peso = int(input('Digite o peso dos peixes: '))
#     if peso > peso_maximo_estabelecido:
#         quilo_excedente = peso - peso_maximo_estabelecido
#         multa = quilo_excedente * multa_por_quilo_excedente
#
#     print('O valor da multa é:', multa)
#     print('O peso excedente é:', quilo_excedente)
#     sair = input('\n1- Para sair\n2- Para continuar\n')
#     if sair == '1':
#         break

print('Questão 02\n')
# 1 litro pinta 6 metros quadrados
litros_lata = 18
preco_lata = 80.0
litros_galao = 3.6
preco_galao = 25.0
metros_quadrados_por_litro = 6
while True:
    quantidade_de_latas_a_serem_compradas = 0
    quantidade_de_galoes_a_serem_comprados = 0
    preco_final_lata = 0.0
    preco_final_galao = 0.0

    tamanho_metros_quadrados = int(input('Digite o tamanho da area a ser pintada: '))
    quantidade_de_litros = tamanho_metros_quadrados / metros_quadrados_por_litro

    if quantidade_de_litros > litros_lata:
        quantidade_de_latas_a_serem_compradas = math.ceil(quantidade_de_litros / litros_lata)
    else:
        quantidade_de_latas_a_serem_compradas = 1

    if quantidade_de_litros > litros_galao:
        quantidade_de_galoes_a_serem_comprados = math.ceil(quantidade_de_litros / litros_galao)
    else:
        quantidade_de_galoes_a_serem_comprados = 1

    preco_final_lata = quantidade_de_latas_a_serem_compradas * preco_lata
    preco_final_galao = quantidade_de_galoes_a_serem_comprados * preco_galao

    print(f'Será necessário {quantidade_de_latas_a_serem_compradas} lata(s) e custará ${preco_final_lata} reais.')
    print(f'Será necessário {quantidade_de_galoes_a_serem_comprados} galões e custará ${preco_final_galao} reais.')
    sair = input('\n1- Para sair\n2- Para continuar\n')
    if sair == '1':
        break