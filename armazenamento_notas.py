import os
import csv

def bimestre():
    while True:
        try:
            while True:
                quantidade_bimestres = int(input("Quais bimestres deseja agregar nota? \nDigite apenas números: ").strip())
                if quantidade_bimestres > 4:
                    print("""valor inválido, digite novamente!! 
                    """)
                else: 
                    break
            break
        except:
            print("""valor inválido, digite novamente!!
            """)

bimestre()
