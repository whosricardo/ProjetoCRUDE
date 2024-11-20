class Treino:
    def __init__(self, nome, data, tempo, distancia, clima, localizacao):
        self.nome = nome
        self.data = data
        self.tempo = tempo
        self.distancia = distancia
        self.clima = clima
        self.localizacao = localizacao 

    def __str__(self):
        return f"Nome do Treino: {self.nome}, Data do Treino: {self.data}, Duração do Treino: {self.tempo}, Distância do Treino: {self.distacia}, Localização do Treino: {self.localizacao}, Clima: {self.clima}"
