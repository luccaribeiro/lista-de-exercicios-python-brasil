"""
Exercício 09 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50

    >>> calcular_numeros_impares_de_1_a_50()
    '1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49'

"""


def calcular_numeros_impares_de_1_a_50() -> str:
    print("""'""", end="")
    for i in range(1,51):
        if not i % 2 == 0 and i != 49:
            print(f"""{i}""", end=", ")
        elif i == 49:
            print(f"""{i}'""")
