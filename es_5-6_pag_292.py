'''Elenca proprietà e metodi della classe prodotto.
Definisci il metodo assegna_prezzo della classe prodotto 
'''
class prodotto():
    def __init__(self, nome_prodotto, prezzo=0, um="EUR"):
        self.prodotto = nome_prodotto
        self.assegna_prezzo(prezzo)
        self.assegna_um(um)

    def assegna_prezzo(self, prezzo):
        self.prezzo = prezzo

    def assegna_um(self, um):
        self.um = um
    
    def visualizza_dati(self):
        print(self.prodotto, self.prezzo, self.um)

class prodotto_carrello():
    def __init__(self, prodotto, qta):
        self.p = prodotto
        self.quantita = qta

def menu():
    while True:
        print()
        print("Menù:")
        print("1) Magazzino prodotti")
        print("2) Metti un prodotto nel carrello")
        print("3) Totale spesa nel carrello")
        print("4) Uscita dal programma")
        scelta = int(input("Scelta voce di menù (1, 2, 3 o 4): "))
        print()
        if scelta >=1 and scelta <=4:
            return scelta

def stampa_prodotti_magazzino(lista_prodotti):
    print("Prodotti disponibili sullo scaffale:")
    for i in range(0,len(lista_prodotti)): 
        print(str(i+1) + ")", lista_prodotti[i].prodotto, lista_prodotti[i].prezzo, lista_prodotti[i].um)

def magazzino_prodotti(lista_prodotti):
    stampa_prodotti_magazzino(lista_prodotti)
    scelta1 = input("Premi il numero del prodotto da modificare, 0 per aggiungere un nuovo prodotto o enter per torare al menu principale: ")
    if scelta1 == "0":
        nome_prodotto = input("Nome del prodotto: ")
        prezzo_prodotto = float(input("Prezzo del prodotto: "))
        um = input("Unità di misura: ")
        p = prodotto(nome_prodotto, prezzo_prodotto, um)
        lista_prodotti.append(p)
    if scelta1 == "":
        return
    elif int(scelta1)>=1 and int(scelta1)<=len(lista_prodotti):
        cancella = input("Si vuole cancellare o modificare il prodotto (C per cancellarlo o M per modificarlo): ")
        if cancella.upper() == "M":
            p = lista_prodotti[int(scelta1)-1]
            nome_prodotto = input("Nome del prodotto [" + p.prodotto + "]: ")
            if nome_prodotto!="":
                p.prodotto=nome_prodotto
            prezzo_prodotto = input("Prezzo del prodotto [" + str(p.prezzo) + "]: ")
            if prezzo_prodotto!="":
                #p.prezzo=float(prezzo_prodotto)
                p.assegna_prezzo(float(prezzo_prodotto))
        elif cancella.upper() == "C":
            del lista_prodotti[int(scelta1)-1]

def mostra_carrello(lista_prodotti, carrello):
    print("Prodotti nel carrello e rispettive quantità:")
    for i in range(0,len(carrello)): 
        print(str(i+1) + ")", carrello[i].p.prodotto, carrello[i].quantita)
    scelta1 = input("Premi il numero del prodotto da eliminare, 0 per aggiungere un nuovo prodotto o enter per torare al menu principale: ")
    if scelta1 == "0":
        stampa_prodotti_magazzino(lista_prodotti)
        scelta2 = input("Premi il numero del prodotto da mettere nel carrello: ")
        if int(scelta2)>=1 and int(scelta2)<=len(lista_prodotti):
            p = lista_prodotti[int(scelta2)-1]
            qta = float(input("Che quantità ne desideri? "))
            pc = prodotto_carrello(p, qta)
            carrello.append(pc)
    elif int(scelta1)>=1 and int(scelta1)<=len(carrello):
        del carrello[int(scelta1)-1]
    totale_spesa(carrello)

def totale_spesa(carrello):
    tot = 0
    for pc in carrello:
        tot += pc.p.prezzo * pc.quantita
    print("Totale costo prodotti nel carrello:", tot)

def main():      
    lista_prodotti = []
    carrello = []

    # creo dei prodotti in magazzino per non doverli creare ogni volta
    lista_prodotti.append(prodotto("Filetto di chianina", 30, "€/kg"))
    lista_prodotti.append(prodotto("Pane comune", 2, "€/kg"))
    lista_prodotti.append(prodotto("Biscotti", 4, "€/kg"))

    while True:
        scelta = menu()
        if scelta == 1:     # Magazzino prodotti
            magazzino_prodotti(lista_prodotti)
        elif scelta == 2:   # Carrello
            mostra_carrello(lista_prodotti, carrello)
        elif scelta == 3:   # Totale spesa
            totale_spesa(carrello)
        elif scelta == 4:
            print("Arrivederci!!")
            break

    
if __name__ == "__main__":
    main()

