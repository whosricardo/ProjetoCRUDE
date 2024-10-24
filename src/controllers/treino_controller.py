import csv
from models.treino import Treino

def adicionar_treino(nome, data, tempo, distancia, clima, localizacao):
    treino = Treino(nome, data, tempo, distancia, clima, localizacao)

    with open('data/treinos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([treino.nome, treino.data, treino.tempo, treino.distancia, treino.clima, treino.localizacao])

def atualizar_treino(nome_treino, novos_dados):
    try:
        treinos = []
        treino_encontrado = False

        with open('data/treinos.csv', mode='r') as file:
            reader = csv.reader(file)
            for linha in reader:
                if linha[0] == nome_treino:
                    treinos.append(novos_dados)
                    treino_encontrado = True
                else:
                    treinos.append(linha)

        if not treino_encontrado:
            print(f"Treino [{nome_treino}] não encontrado")
            return
        
        with open('data/treinos.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerows(treinos)
            print(f"Treino [{nome_treino}] foi atualizado com sucesso!")

    except FileNotFoundError:
        print(f"Erro: Arquivo 'treinos.csv' não foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def deletar_treino(nome_treino):
    try:
        treinos = []
        treino_encontrado = False

        with open('data/treinos.csv', mode='r') as file:
            reader = csv.reader(file)
            for linha in reader:
                if linha[0] != nome_treino:
                    treinos.append(linha)
                else:
                    treino_encontrado = True

        if not treino_encontrado:
            print(f"Treino [{nome_treino}] não encontrado")
            return
        
        with open('data/treinos.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerows(treinos)
            print(f"Treino [{nome_treino}] foi deletado com sucesso!")

    except FileNotFoundError:
        print(f"Erro: Arquivo 'treinos.csv' não foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def listar_treinos():
    with open('data/treinos.csv', mode='r') as file:
        reader = csv.reader(file)
        for linha in reader:
            print(linha)