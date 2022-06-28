"""
Exercício 32 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120

    >>> calcular_fatorial(1)
    Fatorial de 1:
    1! = 1 = 1
    >>> calcular_fatorial(2)
    Fatorial de 2:
    2! = 2 . 1 = 2
    >>> calcular_fatorial(3)
    Fatorial de 3:
    3! = 3 . 2 . 1 = 6
    >>> calcular_fatorial(4)
    Fatorial de 4:
    4! = 4 . 3 . 2 . 1 = 24
    >>> calcular_fatorial(5)
    Fatorial de 5:
    5! = 5 . 4 . 3 . 2 . 1 = 120

"""


def calcular_fatorial(n: int):
    fact = 1
    numeros = []
    print(f'Fatorial de {n}:')
    for num in range(1, n+1):
        numeros.append(num)
        fact *= num
    print(f'{n}! = ',end="")
    numeros.sort(reverse=True)
    for n in numeros:
        if n != 1:
            print(f'{n} .',end=" ")
        else:
            print(f'{n}', end=" ")
    print(f'= {fact}', end="")
