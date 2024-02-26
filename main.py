class Usuario:
    def __init__(self, plano):
        self.Lista_Plano = ['Premium', 'Basic', 'Free']
        if plano in self.Lista_Plano:
            self.plano = plano
        else:
            raise Exception ("Plano Inválido!")

    def Ver_Animes(self, Anime):
        self.ListaPremium = ['Naruto', 'Dragon Ball', 'One Piece']
        self.ListaBasic = ['Jujutsu Kaisen', 'Death Note', 'Hunter X Hunter']
        self.ListaFree = ['Solo Leving', 'Shingeki no Kyojin']
        if self.plano == "Premium":
            print(f"Assistindo o anime: {Anime} com o plano {self.plano}")
        elif self.plano == "Basic" and (Anime in self.ListaBasic or Anime in self.ListaFree):
            print(f"Assistindo o anime: {Anime} com o plano {self.plano}")
        elif self.plano == "Free" and Anime in self.ListaFree:
            print(f"Assistindo o anime: {Anime} com o plano {self.plano}")
        else:
            raise Exception ("Filme inválido para o atual plano usuario, deseja fazer um upgrade?")

cliente = Usuario("Basic")
cliente.Ver_Animes("Naruto")
