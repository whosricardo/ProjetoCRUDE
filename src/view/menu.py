from datetime import datetime

def menu_opcoes ():
    print ("Menu de opções\n")
    print ("1- Adicionar registro de treino/competição")
    print ("2- Visualizar registro de treino/competição")
    print ("3- Atualizar registro de treino/competição")
    print ("4- Excluir registro de treino/competição")
    print ("5- Acessar o menu de metas.")
    print ("6- sair")
    opcoes ()
    
def menu_metas ():
    print ("Menu de metas\n")
    print ("1- Adicionar registro de metas.")
    print ("2- Visualizar registro de metas.")
    print ("3- Atualizar registro de metas.")
    print ("4- Deletar registro de metas.")
    print ("5- voltar ao menu principal.")
    opcao_menu ()
#aaaa
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
    from controllers.treino_controller import atualizar_treino, listar_treinos
    
    listar_treinos()
    
    nome_treino = input("Insira o nome do treino que deseja substituir: ")
    novos_dados = []
    
    campos = [
        ("nome do novo treino", str),
        ("data do treino/competição (DD/MM/YYYY)", str, "%d/%m/%Y"),
        ("tempo de treino/competição em minutos", float),
        ("distância percorrida em quilômetros", float),
        ("clima do treino/competição", str),
        ("localização do treino/competição", str)
    ]
    
    for campo, tipo, *args in campos:
        while True:
            try:
                valor = input(f"Insira o {campo}: ")
                if tipo == str and args:
                    valor = datetime.strptime(valor, args[0]).strftime(args[0])
                else:
                    valor = tipo(valor)
                novos_dados.append(valor)
                break
            except ValueError:
                print(f"Erro: valor inválido para {campo}. Tente novamente.")

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
    
    elif (opcao == 5):
        menu_metas ()
        opcao_menu ()
        
    
        


def metas_adicionar ():
    from controllers.meta_controller import adicionar_meta
    while True:
        try:
            nome = str(input("Insira o nome do treino nome: "))
            data_str = input("Insira a data do treino/competição (DD/MM/YYYY): ")
            data_format = datetime.strptime(data_str, "%d/%m/%Y")
            data = data_format.strftime("%d/%m/%Y")
            tempo = float(input("Insira o tempo de treino/competição em minutos: "))
            meta_tempo = float(input("Insira a meta de tempo da competição: "))
            distancia = (float(input("Insira a distancia percorrida em quilometros: ")))
            meta_distancia = float(input("Insira a meta de distancia percorrida em quilometros: "))
            meta_calorias = float(input("Insira a meta de calorias: "))
            break
        except ValueError:
            print("Insira por favor um valor correspondente ao que foi pedido")
    
    adicionar_meta (nome, data, tempo, distancia, meta_tempo, meta_distancia, meta_calorias)
    

def metas_visualizar():
    from controllers.meta_controller import listar_metas
    
    listar_metas()
    
def metas_atualizar():
    from controllers.meta_controller import atualizar_meta , listar_metas
    
    listar_metas ()
    
    
    
    
    nome_meta = input("Insira o nome da meta que deseja substituir: ")
    novos_dados = []
    
    campos = [
        ("nome da nova meta ", str),
        ("nova data de meta válida (DD/MM/YYYY)", str, "%d/%m/%Y"),
        ("nova meta de tempo em minutos", float),
        ("nova meta de distância percorrida em quilômetros", float),
        ("nova meta de calorias", float)
    ]
    
    for campo, tipo, *args in campos:
        while True:
            try:
                valor = input(f"Insira o {campo}: ")
                if tipo == str and args:
                    valor = datetime.strptime(valor, args[0]).strftime(args[0])
                else:
                    valor = tipo(valor)
                novos_dados.append(valor)
                break
            except ValueError:
                print(f"Erro: valor inválido para {campo}. Tente novamente.")

    atualizar_meta(nome_meta, novos_dados)
    
    
def metas_deletar ():
    from controllers.meta_controller import deletar_meta
    
    nome_meta = str(input("Insira o nome da meta a ser deletada: "))
    deletar_meta(nome_meta)
    
    
    
def opcao_menu():
    opcao_meta = int(input("Digite o código da ação correspondente: "))
    
    if opcao_meta == 1:
        metas_adicionar()
        
    elif opcao_meta == 2:
        metas_visualizar()
            
    elif opcao_meta == 3:
        metas_atualizar()
            
    elif opcao_meta == 4:
        metas_deletar()
        
    elif opcao_meta == 5:
        menu_opcoes()
        opcoes ()
            
            
        
    

 