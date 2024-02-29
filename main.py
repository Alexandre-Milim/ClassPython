class Usuario:
    def __init__(self, plano):
        self.planos_disponiveis = ["Premium", "Basic", "Free"]
        if plano in self.planos_disponiveis:
            self.plano = plano
        else:
            raise Exception("Plano inválido!")

    def Trocar_Plano(self, novo_plano):
        if novo_plano in self.planos_disponiveis:
            self.plano = novo_plano

    def Ver_Filmes(self, filme):
        lista_premium = ["A Rede Social", "O Jogo da Imitação", "A Teoria de Tudo"]
        lista_basic = ["La La Land: Cantando Estações", "Avatar: O Caminho da Água", "O Quarto de Jack"]
        lista_free = ["Gravidade", "A Baleia"]

        if self.plano == "Premium" and (filme in lista_premium or filme in lista_basic or filme in lista_free):
            print(f"Assistindo o filme: {filme} com o plano {self.plano}")
        elif self.plano == "Basic" and (filme in lista_basic or filme in lista_free):
            print(f"Assistindo o filme: {filme} com o plano {self.plano}")
        elif self.plano == "Free" and filme in lista_free:
            print(f"Assistindo o filme: {filme} com o plano {self.plano}")
        else:
            resposta = input(f"Filme indisponível para o plano atual. Deseja fazer um upgrade? (sim/não) ")
            if resposta.lower() == "sim":
                novo_plano = input("Qual plano você deseja para o upgrade: ")
                self.Trocar_Plano(novo_plano)
                print(f"Assistindo o filme: {filme} com o novo plano {self.plano}")
            else:
                raise Exception("Filme indisponível para sua categoria")

plano_usuario = input('Digite o plano do usuário: ')
cliente = Usuario(plano=plano_usuario)
ver_filmes_desejado = input('Digite o nome do filme que você deseja assistir: ')
cliente.Ver_Filmes(ver_filmes_desejado)
