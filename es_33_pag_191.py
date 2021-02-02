def stampa_coda(coda):
    print("L'ordine dei pazienti in coda è:")
    for e in coda:
        print(e)

def menu():
    while True:
        print()
        print("Menù:")
        print("1) Arrivo nuovo paziente")
        print("2) Avanzamento coda (analisi prossimo paziente in coda)")
        print("3) Stampa pazienti in coda")
        print("4) Uscita dal programma")
        scelta = int(input("Scelta voce di menù (1, 2, 3 o 4): "))
        print()
        if scelta >=1 and scelta <=4:
            return scelta

coda = []
while True:
    scelta = menu()
    if scelta == 1:
        nome = input("Inserisci il nome del paziente appena arrivato: ")
        coda.append(nome)
    elif scelta == 2:
        utente_da_servire = coda.pop(0)
        print("Serviamo il paziente", utente_da_servire)
        stampa_coda(coda)
    elif scelta == 3:
        stampa_coda(coda)
    elif scelta == 4:
        print("Arrivederci!!")
        break