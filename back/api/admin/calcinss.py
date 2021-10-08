from os import curdir
import sqlite3

banco = sqlite3.connect('banco.db')
cursor = banco.cursor()

#salario
dbsalarioInss1 = cursor.execute("SELECT faixa_max FROM Inss  where id = 1  ").fetchone()[0]
dbsalarioInss2 = cursor.execute("SELECT faixa_max FROM Inss  where id = 2  ").fetchone()[0]
dbsalarioInss3 = cursor.execute("SELECT faixa_max FROM Inss  where id = 3  ").fetchone()[0]
dbsalarioInss4 = cursor.execute("SELECT faixa_max FROM Inss  where id = 4  ").fetchone()[0]


#aliquota
aliquotaInss1 = cursor.execute("SELECT aliquota FROM Inss    where id = 1  ").fetchone()[0]
aliquotaInss2 = cursor.execute("SELECT aliquota FROM Inss    where id = 2  ").fetchone()[0]
aliquotaInss3 = cursor.execute("SELECT aliquota FROM Inss    where id = 3  ").fetchone()[0]
aliquotaInss4 = cursor.execute("SELECT aliquota FROM Inss    where id = 4  ").fetchone()[0]

#deduçao
deducaoInss2 = cursor.execute("SELECT deducao FROM Inss      where id = 2  ").fetchone()[0]
deducaoInss3 = cursor.execute("SELECT deducao FROM Inss      where id = 3  ").fetchone()[0]
deducaoInss4 = cursor.execute("SELECT deducao FROM Inss      where id = 4  ").fetchone()[0]
deducaoInss5 = cursor.execute("SELECT deducao FROM Inss      where id = 5  ").fetchone()[0]


def calc (bruto):
    if(bruto <= dbsalarioInss1):
        Inss = (bruto*aliquotaInss1)
    elif((bruto >dbsalarioInss1) and bruto <= dbsalarioInss2):
        Inss = (bruto*aliquotaInss2)-deducaoInss2
    elif((bruto >=dbsalarioInss2) and bruto <= dbsalarioInss3):
        Inss = (bruto*aliquotaInss3)-deducaoInss3
    elif((bruto >=dbsalarioInss3) and bruto <= dbsalarioInss4):
        Inss = (bruto*aliquotaInss4)-deducaoInss4
    elif(bruto > dbsalarioInss4):
        Inss = deducaoInss5


    return Inss




        
