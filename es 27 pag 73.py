lista=[]
while True: 
    transizione=input("Il suo veicolo è in procinto di passare per questo casello? (premere 0 per terminare) "))
    lista.append(transizione)
    if transizione==0 :
        break
print(len(lista))


