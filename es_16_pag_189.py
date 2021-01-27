def trova_cap(diz, nazione):
    if nazione in diz:
        print("La capitale di", nazione, "é:", diz[nazione])
    else:
        print("La nazione", nazione, "non è nell'elenco")



nazioni = []
capitali = []
nazioni_capitali = dict()
while True:
    nazione = input("Inserisci una nazione (inserisci 0 per terminare l'elenco): ")
    if nazione == "0":
        break
    nazioni.append(nazione)
    capitale = input("Inserisci la rispettiva capitale: ")
    capitali.append(capitale)

for i in range(len(nazioni)):
    nazioni_capitali[nazioni[i]] = capitali[i]

while True:
    cap_sconosciuta = input("Di quale nazione desideri sapere la capitale (0 per terminare)? ")
    if cap_sconosciuta == "0":
        break
    trova_cap(nazioni_capitali, cap_sconosciuta)