lista = []

fatturato_nord = int(input("Inserisci il fatturato del nord d'Italia (0 per terminare): "))
lista.append(fatturato_nord)
fatturato_centro = int(input("Inserisci il fatturato del centro d'Italia: "))
lista.append(fatturato_centro)
fatturato_sud = int(input("Inserisci il fatturato del sud d'Italia: "))
lista.append(fatturato_sud)
fatturato_isole = int(input("Inserisci il fatturato delle isole d'Italia: "))
lista.append(fatturato_isole)

fatturato_italia = sum(lista)
print("Il fatturato totale è: ", fatturato_italia, "EURO")
print("Le percentuali delle vendite nelle quattro zone rispetto al totale è:")
for i in range(len(lista)):
    percentuale = 100 * lista[i] / fatturato_italia
    print(percentuale, "%")