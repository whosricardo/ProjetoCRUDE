import csv
from models.meta import Metas

def adicionar_meta(nome, data, tempo, distancia, meta_tempo, meta_distancia, meta_calorias):
    meta = Metas(nome, data, tempo, distancia, meta_tempo, meta_distancia, meta_calorias)

    with open('data/metas.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([meta.nome, meta.data, meta.tempo, meta.distancia, meta.meta_tempo, meta.meta_distancia, meta.meta_calorias])

def atualizar_meta(nome_meta, novos_dados):
    try:
        metas = []
        meta_encontrado = False

        with open('data/metas.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for linha in reader:
                if len(linha) == 0:
                    continue 
                if linha[0] == nome_meta:
                    if isinstance(novos_dados, list) and len(novos_dados) == len(linha):
                        metas.append(novos_dados)
                    else:
                        print("Erro: Os novos dados devem ser uma lista com o mesmo número de colunas.")
                        return
                    meta_encontrado = True
                else:
                    metas.append(linha)

        if not meta_encontrado:
            print(f"Treino [{nome_meta}] não encontrado")
            return
        
        with open('data/treinos.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(metas)
            print(f"Treino [{nome_meta}] foi atualizado com sucesso!")

    except FileNotFoundError:
        print(f"Erro: Arquivo 'treinos.csv' não foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def deletar_meta(nome_meta):
    try:
        metas = []
        meta_encontrado = False

        with open('data/metas.csv', mode='r') as file:
            reader = csv.reader(file)
            for linha in reader:
                if linha[0] != nome_meta:
                    metas.append(linha)
                else:
                    meta_encontrado = True

        if not meta_encontrado:
            print(f"Meta [{nome_meta}] não encontrado")
            return
        
        with open('data/metas.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerows(metas)
            print(f"Meta [{nome_meta}] foi deletado com sucesso!")

    except FileNotFoundError:
        print(f"Erro: Arquivo 'metas.csv' não foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def listar_metas():
    with open('data/metas.csv', mode='r') as file:
        reader = csv.reader(file)
        for linha in reader:
            print(linha)