class atleta:
    nome = ""
    eta = 0
    squadra = ""
    visita_medica = False

    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def set_squadra(self, nome_squadra):
        self.squadra = nome_squadra

    def effettua_visita(self):
        self.visita_medica = True
    
    def visualizza_dati(self):
        print("Atleta:", self.nome)
        print("Età:", self.eta)
        print("Squadra", self.squadra)
        print("Visita medica effettuata? ", "Si" if self.visita_medica else "No")
        print("-----------")

atleti_list = []
while True:
    nome_giocatore = input("Nome atleta (o 0 per teminare): ")
    if nome_giocatore=="0":
        break
    eta_giocatore = int(input("Età atleta: "))
    nome_squadra = input("In che squadra gioca " + nome_giocatore + "? ")
    a = atleta(nome_giocatore, eta_giocatore)
    a.set_squadra(nome_squadra)
    a.effettua_visita()
    atleti_list.append(a)

print("Atleti inseriti:")
for a in atleti_list:
    a.visualizza_dati()