import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

#==========

x=np.linspace(0.5,10,100)
y1=np.log(2*x)
y2=(-4)*x+2
y3=2*(np.cos(x))
print(y1)
print(y2)
print(y3)
plt.plot(x,y1,">",color='#ffcc99',label="y=log2x")
plt.plot(x,y2,":",color='#ccccff',label="y=-4x+2")
plt.plot(x,y3,"--",color='#ff3399',label="y=2cosx")
plt.grid()
plt.legend()
plt.xlabel("oś x")
plt.ylabel("oś y")
plt.ylim(-10,10)
plt.savefig("zad1.png")
plt.show()

#==========

x=np.array(['A','B','C','D','E'])
y=np.array([23,66,17,96,24])
plt.barh(x,y,height=0.75,color=['#ff4d4d','g','b','c','k'])
for index, value in enumerate(y):
    plt.text(value, index, str(value))
plt.yticks(rotation = 45)
plt.title("Wykres Slupki")
plt.savefig("zad1.pdf")
plt.show()

#==========

miesiace = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']

fig = plt.figure(figsize=(10, 6))
dataframe = pd.read_excel('ceny1.xlsx')
lata = dataframe['Rok'].unique()
for x in lata:
    a = dataframe[dataframe.Rok == x].groupby(["Miesiące"]).sum("Wartosc")
    a = a.reindex(miesiace)
    plt.plot(a["Wartosc"])

plt.xlabel("Miesiące")
plt.ylabel("Cena")
plt.title("Ceny ryżu")
plt.legend(lata)
fig.tight_layout()
plt.savefig("zad2.png")
plt.show()

#==========

dataframe = pd.read_excel('przewozy1.xlsx')
print(dataframe)
x=dataframe['Nazwa']
y=dataframe['2015']
plt.bar(x,y,width=0.25,color=['#e6ffee','#6600ff','#9966ff','#ffcc99','#666600','#ff99cc','#66ff66','#ff6600','#cc3300','#ffffcc','#00b36b','#66ffff','#3366ff','#290066','#6699ff','#3366cc'])
plt.title("2015")
plt.xticks(rotation=90)
plt.ylabel("Wartosci")
plt.tight_layout()
plt.savefig("zad3.jpg")
plt.show()

#==========

x = np.arange(-5, 10, step=0.01)
y = (4 - x + x ** 3) / (6 + x - 4 * x ** 2 + x ** 3)
plt.plot(x, y, color="lightblue", label="Funkcja")
plt.ylim(-30, 30)
# asympotota pozioma
av = np.ones(len(x))
plt.plot(x, av, color="orange", linestyle="--", label="y=1")
# asymptota pionowa
x1 = [-1, -1]
y1 = [-30, 30]
plt.plot(x1, y1, color="red", linestyle="--", label="x=-1")
x2 = [2, 2]
y2 = [-30, 30]
plt.plot(x2, y2, color="green", linestyle="--", label="x=2")
x3 = [3, 3]
y3 = [-30, 30]
plt.plot(x3, y3, color="violet", linestyle="--", label="x=3")
plt.title("Wykres funkcji")
plt.legend()
plt.savefig("zad1.pdf", format="pdf")
plt.show()

#==========

dane = pd.read_excel("sport.xlsx", header=None)
x = dane.iloc[:, 1]
etykiety = dane.iloc[:, 0]
plt.pie(x, labels=etykiety, autopct="%1.0f%%", explode=(0.1, 0, 0, 0, 0, 0))
plt.title("Popularność sportu w grupie nastolatków")
plt.annotate("12345", [-1, 1])
plt.savefig("zad2.jpg")
plt.show()

#==========

dane = pd.read_csv("wyksz.csv")
wyzsze = dane[dane["Wykształcenie"] == "wyższe"]
sred = dane[dane["Wykształcenie"] == "średnie"]
podst = dane[dane["Wykształcenie"] == "podstawowe"]
x = np.arange(0, len(wyzsze))
plt.bar(x - 0.25, wyzsze["Liczebność"], label="Wyższe", width=0.25, color="blue")
plt.bar(x, sred["Liczebność"], label="Średnie", width=0.25, color="green")
plt.bar(x + .25, podst["Liczebność"], label="podstawowe", width=0.25, color="brown")
plt.legend(loc=7)
plt.ylabel("Liczebność")
plt.xlabel("Przedział wiekowy")
plt.title("Wykształcenie a wiek")
plt.xticks(x, wyzsze["Wiek"])
plt.show()

#===========

fig, ax1=plt.subplots()
x=np.arange(0,10,step=0.01)
y1=np.log(x)
ax1.plot(x,y1,color='g',label='y=ln(x)')
ax1.legend(loc=7)
ax1.set_xlabel("oś x")
ax1.set_ylabel("oś y dla ln",color='g')
ax1.ticks_params("y",colors='g')
ax2=ax1.twinx()
y2=np.exp(x)
ax2.plot(x,y2,color='b',linestyle="--",label='y=exp(x)')
ax2.legend(loc=4)
ax2.set_ylabel("oś y dla exp",color='b')
ax2.ticks_params("y",colors='b')
plt.title("Zestawienie log i exp")
plt.savefig("zad1.pdf",format="pdf")
plt.show()

#===========

dane=pd.read_csv("samochody.csv",index_col=0)

plt.pie(dane,labels=dane.index)
plt.title("Samochody")
plt.savefig("samochody.pdf",format='pdf')
plt.show()

#===========

dane=pd.read_csv("sklepy.csv",index_col=0)
r16=dane[dane["Rok"]==2016]

x=np.arange(0,len(r16))
plt.bar(x,r16['Liczba obiektów'])
plt.xticks(x,r16.index)
plt.title("Rodzaj sklepow")
plt.show()

