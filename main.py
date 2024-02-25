class Client:
    def __init__(self, name, plan):
        self.name = name
        self.list_plan = ["Premium", "Basic"]
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

        if filme in self.listBasic or filme in self.listPremium:
            print(f"Assistindo {filme} - Plano: {self.plan}")
        else:
            print(f"Filme não disponível para o plano {self.plan}")

cliente = Client("alexandre", "Premium")
cliente.filmes('batman')

