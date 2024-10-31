from datetime import datetime

def menu_opcoes ():
    print ("Menu de opções\n")
    print ("1- Adicionar registro de treino/competição")
    print ("2- Visualizar registro de treino/competição")
    print ("3- Atualizar registro de treino/competição")
    print ("4- Excluir registro de treino/competição")
    print ("5- sair")

def opcao_adicionar ():
    from controllers.treino_controller import adicionar_treino
    while True:
        try:
            nome = str(input("Insira o nome do treino nome: "))
            data_str = input("Insira a data do treino/competição (DD/MM/YYYY): ")
            data_format = datetime.strptime(data_str, "%d/%m/%Y")
            data = data_format.strftime("%d/%m/%Y")
            tempo = float(input("Insira o tempo de treino/competição em minutos: "))
            distancia = float(input("Insira a distancia percorrida em quilometros: "))
            clima = str(input("Insira o clima do treino/competição correspondente : "))
            localizacao = str(input("Insira a localização do treino/competição: "))
            break
        except ValueError:
            print("Insira por favor um valor correspondente ao que foi pedido")
    
    adicionar_treino (nome,data,tempo,distancia,clima,localizacao)
    
    
def opcao_visualizar ():
    from controllers.treino_controller import listar_treinos
    listar_treinos()
    
        
def opcao_atualizar():
    from controllers.treino_controller import atualizar_treino
    from controllers.treino_controller import listar_treinos
    listar_treinos()
    
    novos_dados = []
    nome_treino = str(input("Insira o nome do treino que deseja substituir: "))
    
    while True:
        try:
            nome = str(input("Insira o nome do novo treino: "))
            data_str = input("Insira a nova data do treino/competição (DD/MM/YYYY): ")
            data_format = datetime.strptime(data_str, "%d/%m/%Y")
            data = data_format.strftime("%d/%m/%Y")
            tempo = float(input("Insira o novo tempo de treino/competição em minutos: "))
            distancia = float(input("Insira a nova distancia percorrida em quilometros: "))
            clima = str(input("Insira o novo clima do treino/competição correspondente : "))
            localizacao = str(input("Insira a nova localização do treino/competição: "))
            break
        except ValueError:
            print("Insira um data type pedido")
            
    novos_dados += [nome,data,tempo,distancia,clima,localizacao]
    atualizar_treino(nome_treino, novos_dados)

def opcao_deletar ():
    from controllers.treino_controller import deletar_treino
    nome_treino = str(input("Insira o nome do treino/competição a ser deletado: "))
    deletar_treino(nome_treino)
    
def opcoes ():
    opcao = int(input("Digite o código da ação correspondente: "))

    if (opcao == 1):
        opcao_adicionar()
        
    elif (opcao == 2):
        opcao_visualizar()
        
    elif (opcao == 3):
        opcao_atualizar()
        
    elif (opcao == 4):
        opcao_deletar()        
