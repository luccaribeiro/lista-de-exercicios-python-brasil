"""
Exercício 16 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o
 valor seja maior que 500.

    >>> calcular_serie_de_fibonacci_ate_valor_ser_maior_que_500()
    '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610'
"""


def calcular_serie_de_fibonacci_ate_valor_ser_maior_que_500() -> str:
    t1 = 1
    t2 = 0
    termo = 0
    while not termo > 500:
        if termo == 0:
            print(f"'{termo}", end=", ")
        else:
            print(f"{termo}", end=", ")
        termo = t1+t2
        t1 = t2
        t2 = termo
        if termo >= 500:
            print(f"{termo}'")
