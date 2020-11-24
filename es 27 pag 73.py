lista=[]
while True: 
    n=int(input("Quanti veicoli sono transitati? (premere 0 per terminare) "))
    lista.append(n)
    if n==0 :
        break

somma = 0
for n in lista:
    somma += n

print("Sono tranistati in tutto " + str(somma) + " veicoli")


