"""
Exercício 41 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1                                0
3                                10
6                                15
9                                20
12                               25

    >>> gerar_dados_de_financiamente(1000)
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1000.00      0%              1                       R$   1000.00
    R$ 1100.00      10%             3                       R$    366.67
    R$ 1150.00      15%             6                       R$    191.67
    R$ 1200.00      20%             9                       R$    133.33
    R$ 1250.00      25%             12                      R$    104.17
    >>> gerar_dados_de_financiamente(1500)
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1500.00      0%              1                       R$   1500.00
    R$ 1650.00      10%             3                       R$    550.00
    R$ 1725.00      15%             6                       R$    287.50
    R$ 1800.00      20%             9                       R$    200.00
    R$ 1875.00      25%             12                      R$    156.25

"""


def gerar_dados_de_financiamente(valor_inicial: float):
    print("Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela")
    porcentagem = 0.1
    parcela = 3
    valor_tot = 0
    for indice in range(5):
        if indice == 0:
            print(f"R$ {valor_inicial:<12.2f} 0%              1                       R$ {valor_inicial:>9.2f}")
        else:
            valor_tot = valor_inicial+(valor_inicial*porcentagem)
            print(f'R$ {valor_tot:<12.2f} {porcentagem:<15.0%} {parcela:<23d} R$ {valor_tot/parcela:9.2f}')
            porcentagem += 0.05
            parcela += 3

