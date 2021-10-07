print('Questão 01')
pessoas_proximas = {
    'Rosa Angélica' : 'vermelho',
    'Nádila': 'branca',
    'Bruno': 'azul',
    'Ana Maria': 'vermelho',
    'Rafael': 'preto'}
print(pessoas_proximas)

print('Questão 02')
semana = {}
semana['segunda'] = []
semana['terça'] = []
semana['quarta'] = []
semana['quinta'] = ['INF032D Programação Python - Básico']
semana['sexta'] = []
print(semana)

print('Questão 03')
filmes = {}
filmes['Batman - O Cavaleiro das Trevas'] = {'Coringa': 2008}
filmes['O Lobo de Wall Street'] = {'Jordan Belfort': 2013}
filmes['Laranja Mecânica'] = {'Alex': 1971}
filmes['Sangue Negro'] = {'Daniel Plainview': 2007}
filmes['O Abutre'] = {'Louis Bloom': 2014}
print(filmes)

print('Questão 04')
d = {
    'nome': 'Roger Mauricio M. Souza',
    'idade': 31,
    'telefone': '71 991916695',
    'endereco': 'Travessa São Judas Tadeu, 28 - Boca do rio'
}
print(d['nome'])

print('Questão 05')
agenda = {}
agenda['cpf'] = input('Digite seu cpf:\n')
agenda['nome'] = input('Digite seu nome:\n')
agenda['idade'] = int(input('Digite sua idade:\n'))
agenda['telefone'] = input('Digite seu telefone:\n')
print(agenda)