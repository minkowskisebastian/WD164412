import pandas as pd

# ZADANIE 1
imiona = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(imiona, header=0)

# ZADANIE 2
print(df[df.Liczba > 1000])
print(df[df.Imie == 'SEBASTIAN'])
print(df.agg({'Liczba': ['sum']}))
print(df.where((df.Rok >= 2000) & (df.Rok <= 2005)).groupby(by='Rok').agg({'Liczba': ['sum']}))
print(df.groupby(by='Plec').agg({'Liczba': ['sum']}))
print(df[df.Plec == 'K'].groupby(by='Rok').agg({'Liczba': ['max']}))
