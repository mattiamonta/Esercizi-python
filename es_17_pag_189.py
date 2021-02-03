def riempimento(dict, nazione, capitale):
    dict[nazione] = capitale

def stampa(dict):
    for chiave in dict:
        print(chiave, ":", dict[chiave])

def inverti(dict, nazione, capitale):
    diz_invertito = {}
    for nazione in dict:
        diz_invertito[dict[nazione]] = nazione
    return diz_invertito

def trova_nazione(dict_invertita, capitale):
    return dict_invertita[capitale]

nazioni_dict = {}
while True:
    nazione = input("Inserisci una nazione (inserisci 0 per terminare l'elenco): ")
    if nazione == "0":
        break
    capitale = input("Inserisci la rispettiva capitale: ")
    riempimento(nazioni_dict, nazione, capitale)

print("L'elenco nazioni : capitali è:")
stampa(nazioni_dict)
print()
print("L'elenco capitali : nazioni è:")
nazioni_dict_invertita = inverti(nazioni_dict, nazione, capitale)
stampa(nazioni_dict_invertita)
while True:
    naz_sconosciuta = input("Di quale capitale vuoi sapere la nazione? (Premi 0 per uscire) ")
    if naz_sconosciuta == "0":
        break
    naz = trova_nazione(nazioni_dict_invertita, naz_sconosciuta)
    print(naz_sconosciuta, "è la capitale di", naz)