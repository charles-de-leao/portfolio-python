
# exercício número 3 - Faturamento

import pandas as pd
import statistics

tabela = pd.read_excel("dados.xlsx")
novo_index = tabela['dia'].values.tolist()
index = pd.Index(novo_index)
tabela = tabela.set_index((index))
print(tabela)
media = []
dia_minimo = []
dias_media = []
minimo = ''
maximo = ''
for i, dia in tabela.iterrows():
    valor = tabela.loc[i, "valor"]
    tabela.valor.idxmax()
    dia_maximo = tabela.loc[tabela.valor.idxmax(), 'dia']
    minimo = tabela['valor'].min()
    if valor != 0:
        media.append(valor)
        media_mensal = statistics.mean(media)
        if media_mensal <= valor:
            dias_media.append(i)

    if valor == 0:
        dia_minimo.append(i)
maximo = tabela.loc[dia_maximo, 'valor']


print(f'\nO menor valor de faturamento foi de R${minimo:.2f} nos dias {*dia_minimo,}.')
print(f'O maior valor de faturamento foi de R${maximo:.2f} no dia {dia_maximo}. ')
print(f'O valor de faturamento foi maior que a média mensal nos dias {*dias_media,}.')
