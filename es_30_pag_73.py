somma=0
num_binario=""
lunghezza=int(input("Quante cifre ha il numero binario? "))
for i in range(0,lunghezza):
    cifra=input("Inserisci la " + str(i+1) + " cifra da destra: ")
    num_binario=cifra+num_binario
    cifra_10=int(cifra)*(2**i)
    somma+=cifra_10
print("Il numero",num_binario,"in base 10 corrisponde a" ,somma)
funz=int(num_binario,2)
print("Il risultato della conversione nativa è" ,funz)
if somma==funz:
    print("Il calcolo è corretto")
else:
    print("IL PROGRAMMA NON FUNZIONA CORRETTAMENTE")