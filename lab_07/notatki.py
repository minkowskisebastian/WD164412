import numpy as np
import pandas as pd

# s = pd.Series([1, 3, 5, np.nan, 8])
# print(s)

s1 = pd.Series([1, 2, 20, 4], index=['a', 'b', 'c', 'd'])
print(s1)

dane = {'Kraj': ['Polska', 'Bułgaria', "Chorwacja"],
        'Stolica': ['Warszawa', 'Sofia', 'Zagrzeb'],
        'Populacja': [37954695, 6927372, 4047047]}

df = pd.DataFrame(dane)
print(df)

# data = pd.date_range('20220420', periods=7)
# df = pd.DataFrame(np.random.randn(7, 4), index=data, columns=list('ABCD'))
# print(df)

iris_df = pd.read_csv('iris.csv', header=0, sep=',', decimal='.')
print(iris_df)

# iris_df.to_csv('nowe.csv', index=False)

print(s1['a'])
# print(s1.a)

print(df['Populacja'])
# print(df.Populacja)

print(df.iloc[[1], [1]])
# print(df.loc[[1],['Kraj']])

print(df.at[1, 'Kraj'])

# dosłownie jak pętla
print('Kraj: ' + df.Kraj)

# print(df.sample(2))
# print(df.sample(frac=0.5))

# print(df.sample(10, replace=True))

# print(iris_df.head(10))
# print(iris_df.tail(10))

# print(s1[s1 > 10])
# print(s1.where(s1 > 10, 'element nie spełnia warunku'))

# seria = s1.copy()
# print(seria)
# seria.where(s1 > 10, 'element nie spełnia warunku', inplace=True)
# print(seria)

# print(s1[~(s1 > 10)])
# print(s1[(s1 > 2) & (s1 < 30)])
# print(df[df['Populacja'] > 5000000])
# print(df[(df.Populacja > 20000000) & (df.index.isin([0, 1]))])

# szukaj = ['Bułgaria', 'Zagrzeb']
# print(df.isin(szukaj))

# s1['e'] = 25
# print(s1)

df.loc[3] = 'nowy_element'
df.loc[4] = ['Japonia', 'Tokyo', 125835951]
print(df)

df.drop(3, inplace=True)
print(df)

# df.drop('Stolica', axis=1, inplace=True)
# print(df)

df['Kontynent'] = ['Europa', 'Europa', 'Europa', 'Azja']
print(df)
print(df.sort_values(by='Kraj'))

grupa = df.groupby(by='Kontynent')
print(grupa.get_group('Europa'))

print(df.groupby(by='Kontynent').agg({'Populacja': ['sum']}))
