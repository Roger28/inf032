print('Questão 1')
lista_nomes = ['Bruno', 'Nádila', 'Angélica']
print('A lista de nomes é', lista_nomes)

print('\nQuestão 2')
frutas = ['Manga', 'Caju', 'Acerola', 'Cajá', 'Mangaba']
doces_festa = ['Brigadeiro', 'Cajuzinho', 'Olho de sogra', 'Beijinho', 'Casadinho']
ingredientes_feijoada = ['Carne seca', 'Pé de porco', 'Rabo de porco', 'Feijão preto', 'Orelha de porco']
listona = [frutas, doces_festa, ingredientes_feijoada]
print(listona[1][0])
listona[1].append('Brigadeiros')
listona[1].append('Brigadeiros')
print('Listona com mais brigadeiros:', listona)
listona.append('Refrigerante')
listona.append('Cerveja')
listona.append('Vinho')
print('Listona com bebidas:', listona)

print('\nQuestão 3')
tamanho_lista = len(listona)
del listona[0:tamanho_lista]
print('Listona:', listona)

print('\nQuestão 4')
compras_do_mes = ['arroz','feijao','carne','açúcar','farinha','leite','detergente','sabao em pó','desengordurante','sorvete de cocô']
print('Compras do mês:', compras_do_mes)
del compras_do_mes[6:9]
print('Lista de compras do mês sem produtos de limpeza:', compras_do_mes)
del compras_do_mes[-1]
print('Lista de compras do mês sem sorvete:', compras_do_mes)

print('\nQuestão 5\n')
lista_numeros = [9, 2, 5, 6, 4, 8, 100]
lista_numeros.sort()
print(lista_numeros)
print(lista_numeros[::-1])