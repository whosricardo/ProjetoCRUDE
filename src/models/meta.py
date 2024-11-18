class Metas:
    def __init__(self, nome, data, tempo, distancia, meta_tempo, meta_distancia, meta_calorias):
        self.nome = nome
        self.data = data
        self.tempo = tempo
        self.distancia = distancia
        self.meta_tempo = meta_tempo
        self.meta_distancia = meta_distancia
        self.meta_calorias = meta_calorias .

    def __str__(self):
        return (f"Nome do Treino: {self.nome}, Data do Treino: {self.data}, Duração do Treino: {self.tempo}, Distância do Treino: {self.distancia}, Meta de Tempo: {self.meta_tempo}, Meta de Distância: {self.meta_distancia}, Meta de Calorias: {self.meta_calorias}")
