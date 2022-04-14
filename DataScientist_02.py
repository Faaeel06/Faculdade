import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

# Criando novas variáveis

data['Nome'] = 'Rafael R. Machado'
# print(data.columns)

# Deletando variáveis
data = data.drop('Nome', axis=1)
# print(data.columns)

# Forma 01: Direto pelo nome das colunas

print(data[['price', 'id', 'date']])

# Forma 02: Pelos Indices das linhas e colunas

print(data.iloc[0:10, 0:3])
