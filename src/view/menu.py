def menu_opcoes ():
    print ("Menu de opções\n")
    print ("1- Adicionar registro de treino/competição")
    print ("2- Visualizar registro de treino/competição")
    print ("3- Atualizar registro de treino/competição")
    print ("4- Excluir registro de treino/competição")
    return

def opcoes ():
    opcao = input ("Digite o código da ação correspondente: ")
    if (opcao == 1):
        from controllers.treino_controller import adicionar_treino
    elif (opcao == 2):
        from controllers.treino_controller import listar_treinos
    return