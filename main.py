class Client:
    def __init__(self, name, plan):
        self.name = name
        self.list_plan = ["Premium", "Basic", "Free"]
        if plan in self.list_plan:
            self.plan = plan
        else:
            raise Exception("Plano Inválido!")

    def mudar_plan(self, new_plan):
        if new_plan in self.list_plan:
            self.plan = new_plan
        else:
            raise Exception("Plano Inválido!")

    def filmes(self, filme):
        self.listPremium = ['bee-moovie', 'avengers', 'tinker bell']
        self.listBasic = ['batman', 'sem floresta']
        self.listFree = ['Robin Hood', 'senhor dos anéis']

        if self.plan == "Premium" and filme in self.listPremium:
            print(f"Assistindo {filme} - Plano: {self.plan}")
        elif filme in self.listBasic:
            print(f"Assistindo {filme} - Plano: {self.plan}")
        elif filme in self.listFree:
            print(f"Assistindo {filme} - Plano: {self.plan}")
        else:
            upgrade_option = input(f"Filme não disponível para o plano {self.plan}. Deseja fazer um upgrade? (Sim/Não): ")
            if upgrade_option.lower() == "sim":
                new_plan = input("Escolha o novo plano (Premium/Basic/Free): ")
                self.mudar_plan(new_plan)
                print(f"Upgrade realizado! Agora você está no plano {self.plan}.")
                print(f"Agora você pode assistir {filme}.")
            else:
                print("Upgrade não realizado. Filme indisponível.")

cliente = Client("alexandre", "Premium")
cliente.filmes('Robin Hood')
