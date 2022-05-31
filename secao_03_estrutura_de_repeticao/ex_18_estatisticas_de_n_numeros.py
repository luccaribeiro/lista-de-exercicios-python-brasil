"""
Exercício 18 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

    >>> calcular_estatisticas()
    'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    >>> calcular_estatisticas(1)
    'Maior valor: 1. Menor valor: 1. Soma: 1'
    >>> calcular_estatisticas(1, 2)
    'Maior valor: 2. Menor valor: 1. Soma: 3'
    >>> calcular_estatisticas(1, 2, -1)
    'Maior valor: 2. Menor valor: -1. Soma: 2'

"""


def calcular_estatisticas(*numeros) -> int:
    maior_valor = 0
    menor_valor = 0
    soma = 0
    if len(numeros) < 1:
        return 'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    else:
        for ind, num in enumerate(numeros):
            soma += num
            if ind == 0:
                maior_valor = num
                menor_valor = num
            if num > maior_valor:
                maior_valor = num
            if num < menor_valor:
                menor_valor = num
        return f'Maior valor: {maior_valor}. Menor valor: {menor_valor}. Soma: {soma}'
