lista_citta=[]
while True:
    citta=[]
    nome=input("Scrivi il nome della città (digitare 0 per terminare): ")
    if nome=="0":
        break  
    citta.append(nome)  
    temp_min=float(input("Quanto è stata la temperatura minima oggi [°C]? "))
    citta.append(temp_min)  
    temp_max=float(input("Quanto è stata la temperatura massima oggi [°C]? "))
    citta.append(temp_max)  
    lista_citta.append(citta)

citta_cont=0
lista_citta_escursione_superiore=[]
print()
escursione_prefiss=float(input("Qual è l'escursione termica da verificare? "))
for c in lista_citta:
    if (c[2]-c[1])>escursione_prefiss:
        citta_cont+=1
        lista_citta_escursione_superiore.append(c)

print("Le città che hanno superato l'escursione termica prefissata di",escursione_prefiss,"°C sono state",citta_cont,":")
for c in lista_citta_escursione_superiore:
    print("\t-",c[0],"- escursione:",c[2]-c[1])
