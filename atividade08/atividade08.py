import math


def numero_par_ou_impar(numero):
    return 'par' if (numero % 2 == 0) else 'impar'


def calcula_area_do_circulo(raio):
    return round(math.pi * math.pow(raio, 2), 2)


def fahrenheit_para_celsius(temperatura):
    return round((temperatura - 32) * 5 / 9, 2)


def todas_temperaturas_em_celsius():
    temp = 32
    celsius = 0
    while celsius <= 100:
        celsius = round(fahrenheit_para_celsius(temp), 2)
        print(f' a {temp} graus em Fahrenheit é equivalente {celsius} graus em Celsius ')
        temp += 1


print('Questão 01')
print(numero_par_ou_impar(56))
print(numero_par_ou_impar(57))

print('Questão 02')
print(calcula_area_do_circulo(20))

print('Questão 03')
print(fahrenheit_para_celsius(40))

print('Questão 04')
todas_temperaturas_em_celsius()
