#exercício número 4 - Distribuidora

import pandas as pd

estados = [['SP', 67836.43], ['RJ', 36678.66],['MG', 29229.88],['ES', 27165.48],['Outros', 19849.53]]
tab_estados = pd.DataFrame(estados, columns=['Estados','Valor'])

total = tab_estados['Valor'].sum()

nova_linha = ['Total Mensal' , total]
# tab_estados.loc[len(tab_estados)] = nova_linha

valores = tab_estados["Valor"].values.tolist()
porcentagem = []
for i , valor in enumerate(valores):
    valor_porcentagem = (valor * 100) / total
    porcentagem.append(valor_porcentagem)

tab_estados.loc[:, ['Percentual']] = porcentagem

# #esse print final exibe a tabela com uma nova coluna mostrando o resultado do percentual pedido.
print(tab_estados)