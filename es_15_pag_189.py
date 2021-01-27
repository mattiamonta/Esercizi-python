def trova_cap(lista_naz, lista_cap, nazione):
    if nazione in lista_naz:
        indice = lista_naz.index(nazione)
        print("La capitale di", nazione, "é:", lista_cap[indice])
    else:
        print("La nazione", nazione, "non è nell'elenco")

nazioni = []
capitali = []
while True:
    nazione = input("Inserisci una nazione (inserisci 0 per terminare l'elenco): ")
    if nazione == "0":
        break
    nazioni.append(nazione)
    capitale = input("Inserisci la rispettiva capitale: ")
    capitali.append(capitale)

while True:
    cap_sconosciuta = input("Di quale nazione desideri sapere la capitale (0 per terminare)? ")
    if cap_sconosciuta == "0":
        break
    trova_cap(nazioni, capitali, cap_sconosciuta)