"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""


def calcular_estatisticas(*cidades):
    from statistics import mean
    cidade = []
    veiculos = []
    acidentes = []
    indice = []
    media = 0
    for c in cidades:
        cidade.append(c[0])
        veiculos.append(c[1])
        acidentes.append(c[2])
        indice.append((c[2]*1000 / c[1]))
        if c[1] >= 150_000:
            media = c[2]
    print(f"O maior índice de acidentes é de {cidade[indice.index(max(indice))]}, com {max(indice):.1f} acidentes por mil carros.")
    print(f"O menor índice de acidentes é de {cidade[indice.index(min(indice))]}, com {min(indice):.1f} acidentes por mil carros.")
    print(f"O média de veículos por cidade é de {mean(veiculos)}.")
    print(f"A média de acidentes total nas cidades com menos de 150 mil carros é de {media:.1f} acidentes.")
