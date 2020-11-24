lista_nomi = []
lista_punti = []
cont = int(input("Inserisci il numero di candidati: "))

for i in range(cont):
    lista_nomi.append(input("Dimmi il nome del " + str(i+1) + " candidato: "))
    lista_punti.append(int(input("Qual è il punteggio del " + str(i+1) + " candidato? ")))

lista_nomi.sort()
print("Candidati in ordine alfabetico:")
for c in lista_nomi:
    print("\t- " + c)

lista_punti.sort(reverse=True)
print("Punteggi in ordine descrescente:")
for p in lista_punti:
    print("\t- " + str(p))
