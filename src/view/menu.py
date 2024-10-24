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
        from controllers.treino_controller import adicionar_treino
        nome = input ("Insira o seu nome: ")
        data = int(input("Insira a data do treino/competição: ""{:%d/%m/%Y}".format(data)))
        tempo = input("Insira o tempo de treino/competição em minutos: ")
        distancia = float(input("Insira a distancia percorrida em quilometros: "))
        clima = input("Insira o clima do treino/competição correspondente : ")
        localizacao = input("Insira a localização do treino/competição: ")
        adicionar_treino (nome,data,tempo,distancia,clima,localizacao)


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

        
        
        
        
        
        
        
  
