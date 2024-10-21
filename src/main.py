from view.menu import menu_opcoes
from view.menu import opcoes
from models.treino import Treino
from controllers.treino_controller import adicionar_treino, listar_treinos

def main():
    nome = "Corrida de 100 Metros"
    data = "12/10/2024"
    tempo = 2 
    distancia = 5
    clima = "Ensolarado"
    localizacao = "Boa Vista"

    adicionar_treino(nome, data, tempo, distancia, clima, localizacao)
if __name__ == "__main__":
    main()