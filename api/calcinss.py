from os import curdir
import sqlite3
import calcirrf as tes

banco = sqlite3.connect('inss.db')
cursor = banco.cursor()

#salario
dbsalarioinss1 = cursor.execute("SELECT faixa_max FROM Inss  where id = 1  ").fetchone()[0]
dbsalarioinss2 = cursor.execute("SELECT faixa_max FROM Inss  where id = 2  ").fetchone()[0]
dbsalarioinss3 = cursor.execute("SELECT faixa_max FROM Inss  where id = 3  ").fetchone()[0]
dbsalarioinss4 = cursor.execute("SELECT faixa_max FROM Inss  where id = 4  ").fetchone()[0]


#aliquota
aliquotainss1 = cursor.execute("SELECT aliquota FROM Inss    where id = 1  ").fetchone()[0]
aliquotainss2 = cursor.execute("SELECT aliquota FROM Inss    where id = 2  ").fetchone()[0]
aliquotainss3 = cursor.execute("SELECT aliquota FROM Inss    where id = 3  ").fetchone()[0]
aliquotainss4 = cursor.execute("SELECT aliquota FROM Inss    where id = 4  ").fetchone()[0]

#deduçao
deducaoinss2 = cursor.execute("SELECT deducao FROM Inss      where id = 2  ").fetchone()[0]
deducaoinss3 = cursor.execute("SELECT deducao FROM Inss      where id = 3  ").fetchone()[0]
deducaoinss4 = cursor.execute("SELECT deducao FROM Inss      where id = 4  ").fetchone()[0]
deducaoinss5 = cursor.execute("SELECT deducao FROM Inss      where id = 5  ").fetchone()[0]


def calc (bruto):

    if(bruto <= dbsalarioinss1):
        inss = (bruto*aliquotainss1)
    elif((bruto >dbsalarioinss1) and bruto <= dbsalarioinss2):
        inss = (bruto*aliquotainss2)-deducaoinss2
    elif((bruto >=dbsalarioinss2) and bruto <= dbsalarioinss3):
        inss = (bruto*aliquotainss3)-deducaoinss3
    elif((bruto >=dbsalarioinss3) and bruto <= dbsalarioinss4):
        inss = (bruto*aliquotainss4)-deducaoinss4
    elif(bruto > dbsalarioinss4):
        inss = deducaoinss5


    return inss




        
