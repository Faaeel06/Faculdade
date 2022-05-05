import pandas as pd

data = pd.read_csv('../datasets/kc_house_data.csv')

# função que converte de object(string) -> date

data['date'] = pd.to_datetime(data['date'])

print(data.dtypes)

# Converter tipos de variavéis
# inteiro -> float
data['bedrooms'] = data['bedrooms'].astype(float)
print(data.dtypes)
# float -> inteiro
data['bedrooms'] = data['bedrooms'].astype(int)
print(data.dtypes)
# inteiro -> str
data['badrooms'] = data['badrooms'].astype(str)
print(data.dtypes)
# string -> inteiro
data[''] = data['bedrooms'].astype(int)
print(data.dtypes)
# String -> data
data['date'] = pd.to_datetime(data['date'])
