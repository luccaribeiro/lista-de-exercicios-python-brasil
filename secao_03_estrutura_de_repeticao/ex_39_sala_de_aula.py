"""
Exercício 39 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o nome do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o nome do aluno mais alto
 e o número do aluno mais baixo, junto com suas alturas.
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162))
    'O maior aluno é o Renzo com 162 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165))
    'O maior aluno é o Clara com 165 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165), ('Oscar', 199))
    'O maior aluno é o Oscar com 199 cm. O menor aluno é o Renzo com 162 cm'

"""


def calcular_aluno_mais_baixo_e_mais_alto(*alunos) -> str:
    maior = ['',0]
    menor = ['',0]
    for aluno in alunos:
        if maior[0] == '':
            maior[0] = aluno[0]
            maior[1] = aluno[1]
            menor[0] = aluno[0]
            menor[1] = aluno[1]
        if aluno[1] > maior[1]:
            maior[0] = aluno[0]
            maior[1] = aluno[1]
        if aluno[1] < menor[1]:
            menor[0] = aluno[0]
            menor[1] = aluno[1]
    print(f"""'O maior aluno é o {maior[0]} com {maior[1]} cm. O menor aluno é o {menor[0]} com {menor[1]} cm'""")

#     nome_aluno_mais_alto, altura_aluno_mais_alto = max(alunos, key=lambda aluno: aluno[1])
#     nome_aluno_mais_baixo, altura_aluno_mais_baixo = min(alunos, key=lambda aluno: aluno[1])
#     return (
#         f'O maior aluno é o {nome_aluno_mais_alto} com {altura_aluno_mais_alto} cm. '
#         f'O menor aluno é o {nome_aluno_mais_baixo} com {altura_aluno_mais_baixo} cm'
#     )
#Olhar o funcionamento
