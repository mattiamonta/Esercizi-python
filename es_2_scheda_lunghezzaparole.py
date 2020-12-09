lista_parole = []
lista_lunghezze = []
while True:
    parola = input("Inserisci una parola di cui vuoi ottenere la lunghezza (premi 0 per terminare): ")
    if parola == "0":
        break
    lista_parole.append(parola)
    lista_lunghezze.append(len(parola))

print("Lista parole inserite:")
print(lista_parole)
print("Lista lunghezze delle parole inserite:")
print(lista_lunghezze)

print("Lista parole e relative lunghezze:")
for i in range(0,len(lista_parole)):
    print("\t", lista_parole[i], "- lunghezza:", lista_lunghezze[i])