import numpy as np
import pandas as pd

# ZADANIE 1
imiona = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(imiona, header=0)

# ZADANIE 2

# a)
print(df[df.Liczba > 1000])
# b)
print(df[df.Imie == 'SEBASTIAN'])
# c)
print(df.agg({'Liczba': ['sum']}))
# d)
print(df.where((df.Rok >= 2000) & (df.Rok <= 2005)).groupby(by='Rok').agg({'Liczba': ['sum']}))
# e)
print(df.groupby(by='Plec').agg({'Liczba': ['sum']}))
# f)

# g)


# ZADANIE 3
zam = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';', decimal='.')
print(zam)

# a)
print(zam['Sprzedawca'].unique())
# b)
print(zam['Utarg'].sort_values(ascending=False).head(5))
# c)
print(zam[['Sprzedawca', 'idZamowienia']].groupby(['Sprzedawca']).agg({'idZamowienia': ['count']}))
# d)
print(zam[['Kraj', 'idZamowienia']].groupby(['Kraj']).agg({'idZamowienia': ['count']}))
# e)
print(zam[(zam['Kraj'] == 'Polska') & (pd.to_datetime(zam['Data zamowienia']).dt.year == 2005)].agg(
    {'idZamowienia': ['count']}))
# f)
print(zam[pd.to_datetime(zam['Data zamowienia']).dt.year == 2004].agg({'Utarg': ['mean']}))
# g)
zam[pd.to_datetime(zam['Data zamowienia']).dt.year == 2004].to_csv('zamówienia_2004.csv', index=False)
zam[pd.to_datetime(zam['Data zamowienia']).dt.year == 2005].to_csv('zamówienia_2005.csv', index=False)