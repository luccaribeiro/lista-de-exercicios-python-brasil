"""
Exercício 19 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

    >>> calcular_estatisticas()
    'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    >>> calcular_estatisticas(1)
    'Maior valor: 1. Menor valor: 1. Soma: 1'
    >>> calcular_estatisticas(1, 2)
    'Maior valor: 2. Menor valor: 1. Soma: 3'
    >>> calcular_estatisticas(1, 2, -1)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, -10)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1001)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1198)
    'Somente números de 0 a 1000 são permitidos'

"""


def calcular_estatisticas(*numeros) -> str:
    maior_valor = ''
    menor_valor = ''
    soma = 0
    fora_padrao = False
    if len(numeros) > 0:
        for n in numeros:
            if n > 1000 or n < 0:
                fora_padrao = True
            soma += n
            if maior_valor == '':
                maior_valor = menor_valor = n
            if n > maior_valor:
                maior_valor = n
            if n < menor_valor:
                menor_valor
        if fora_padrao == False:
            print(f"'Maior valor: {maior_valor}. Menor valor: {menor_valor}. Soma: {soma}'")
        else:
            print("'Somente números de 0 a 1000 são permitidos'")
    else:
        print("'Maior valor: não existe. Menor valor: não existe. Soma: 0'")
