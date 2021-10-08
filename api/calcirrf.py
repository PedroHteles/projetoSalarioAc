from os import curdir
import sqlite3


banco = sqlite3.connect('inss.db')
cursor = banco.cursor()

#salario
dbsalarioirrf1 = cursor.execute("SELECT faixa_max FROM Irrf  where id = 1  ").fetchone()[0]
dbsalarioirrf2 = cursor.execute("SELECT faixa_max FROM Irrf  where id = 2  ").fetchone()[0]
dbsalarioirrf3 = cursor.execute("SELECT faixa_max FROM Irrf  where id = 3  ").fetchone()[0]
dbsalarioirrf4 = cursor.execute("SELECT faixa_max FROM Irrf  where id = 4  ").fetchone()[0]


#aliquota
aliquotairrf2 = cursor.execute("SELECT aliquota FROM Irrf    where id = 2  ").fetchone()[0]
aliquotairrf3 = cursor.execute("SELECT aliquota FROM Irrf    where id = 3  ").fetchone()[0]
aliquotairrf4 = cursor.execute("SELECT aliquota FROM Irrf    where id = 4  ").fetchone()[0]

#deduçao
deducaoirrf2 = cursor.execute("SELECT deducao FROM Irrf       where id = 2  ").fetchone()[0]
deducaoirrf3 = cursor.execute("SELECT deducao FROM Irrf       where id = 3  ").fetchone()[0]
deducaoirrf4 = cursor.execute("SELECT deducao FROM Irrf       where id = 4  ").fetchone()[0]



def irrf(inss,bruto,dep):

    iv= bruto - inss - (dep*189)

    if(iv<dbsalarioirrf1):
        ir = 0
    elif((iv> dbsalarioirrf1) and (iv<dbsalarioirrf2)):
        ir = (iv*aliquotairrf2)-deducaoirrf2
    elif((iv> dbsalarioirrf2) and (iv<dbsalarioirrf3)):
        ir = (iv*aliquotairrf3)-deducaoirrf3
    elif((iv> dbsalarioirrf3) and (iv<dbsalarioirrf4)):
        ir = (iv*aliquotairrf2)-deducaoirrf4
    elif(iv> dbsalarioirrf4):
        ir = (iv*0.275)-869.36
        
    
    return ir






        
