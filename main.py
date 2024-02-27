class Usuario:
    def __init__(self, plano):
        self.Lista_Plano = ['Premium', 'Basic', 'Free']
        if plano in self.Lista_Plano:
            self.plano = plano
        else:
            raise Exception ("Plano Inválido!")

    def Ver_Filmes(self, Filme):
        self.ListaPremium = ['A Rede Social', 'O Jogo da Imitação', 'A Teoria de Tudo']
        self.ListaBasic = ['La La Land: Cantando Estações', 'Avatar: O Caminho da Água', 'O Quarto de Jack']
        self.ListaFree = ['Gravidade', 'A Baleia']
        if self.plano == "Premium":
            print(f"Assistindo o filme: {Filme} com o plano {self.plano}")
        elif self.plano == "Basic" and (Filme in self.ListaBasic or Filme in self.ListaFree):
            print(f"Assistindo o filme: {Filme} com o plano {self.plano}")
        elif self.plano == "Free" and Filme in self.ListaFree:
            print(f"Assistindo o filme: {Filme} com o plano {self.plano}")
        else:
            raise Exception ("Filme inválido para o atual plano usuario, deseja fazer um upgrade?")

cliente = Usuario("Basic")
cliente.Ver_Filmes("A Rede Social")
