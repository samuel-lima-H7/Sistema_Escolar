import os
import csv

def info_aluno():
    aluno = input("Qual aluno deseja cadsatrar?: ")
    with open("data_base.csv", "a", newline="", encoding="utf-8") as armazena:
        armazena_csv = csv.writer(armazena, delimiter=";")
        for c in range(4):
            armazena_csv.writerow([aluno, "", "", "", "", "", "", ""])

info_aluno()
