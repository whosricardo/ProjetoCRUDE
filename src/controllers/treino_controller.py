import csv
from models.treino import Treino

def adicionar_treino(nome, data, tempo, distancia, clima, localizacao):
    treino = Treino(nome, data, tempo, distancia, clima, localizacao)

    with open('data/treinos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([treino.nome, treino.data, treino.tempo, treino.distancia, treino.clima, treino.localizacao])

def listar_treinos():
    with open('data/treinos.csv', mode='r') as file:
        reader = csv.reader(file)
        for linha in reader:
            print(linha)