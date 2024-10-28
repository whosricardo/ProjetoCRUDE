def menu_opcoes ():
    print ("Menu de opções\n")
    print ("1- Adicionar registro de treino/competição")
    print ("2- Visualizar registro de treino/competição")
    print ("3- Atualizar registro de treino/competição")
    print ("4- Excluir registro de treino/competição")
    print ("5- sair")

def opcoes ():
    opcao = input ("Digite o código da ação correspondente: ")
    if (opcao == 1):
        opcao_adicionar()
        
    elif (opcao == 2):
        opcao_visualizar()
        
    elif (opcao == 3):
        opcao_atualizar()
        
    elif (opcao == 4):
        
        
        
        
        
        
        
        
        
        
        
        
        """
        from controllers.treino_controller import adicionar_treino
        nome = input ("Insira o seu nome: ")
        data = int(input("Insira a data do treino/competição: ""{:%d/%m/%Y}".format(data)))
        tempo = input("Insira o tempo de treino/competição em minutos: ")
        distancia = float(input("Insira a distancia percorrida em quilometros: "))
        clima = input("Insira o clima do treino/competição correspondente : ")
        localizacao = input("Insira a localização do treino/competição: ")
        adicionar_treino (nome,data,tempo,distancia,clima,localizacao)
        """

def opcao_adicionar ():
    from controllers.treino_controller import adicionar_treino
    while True:
        try:
            nome = str(input("Insira o seu nome: "))
            data = int(input("Insira a data do treino/competição: ""{:%d/%m/%Y}".format(data)))
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
    nome_treino = str(input("Insira o nome do treino que deseja substituir: "))
    novos_dados = str(input("Insira o novo dado de treino: "))
    atualizar_treino (nome_treino , novos_dados)
        

def opcao_deletar ():
    from controllers.treino_controller import deletar_treino
    nome_treino = str(input("Insira o nome do treino/competição a ser deletado: "))
    deletar_treino(nome_treino)
    
