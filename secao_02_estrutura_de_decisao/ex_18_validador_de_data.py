"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    from datetime import datetime
    try:
        datetime.strptime(data.strip(), '%d/%m/%Y')
        print("""'Data válida'""")
    except ValueError:
        print("""'Data inválida'""")



"""
    if len(data) <5:
        print("""'Data inválida'""")
    elif data[1] and data[3] == '/' or data[1] and data[4] == '/' or data[2] and data[5] == '/':
        if int(data[0]) > 3 or int(data[0]) >= 3 and int(data[4]) == 2:
            print("""'Data inválida'""")
        elif data[2] and data[5] == '/' and int(data[3]) == 1 and int(data[4]) > 2:
            print("""'Data inválida'""")
        else:
            print("""'Data válida'""")
"""




