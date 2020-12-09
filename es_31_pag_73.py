num=int(input("Inserisci il numero in base 10 da convertire in binario? "))
num_base_10=num
num_binario=""
while num!=0:
    resto=num%2
    num=num//2
    num_binario=str(resto)+num_binario
print("Il numero in binario è",num_binario)
funz=bin(num_base_10)[2:]   #rimuovo i primi 2 caratteri (0b), che non fanno parte del numero in se, ma indicano solo che è in base 2
print("Il risultato della conversione nativa è" ,funz)
if num_binario==funz:
    print("Il calcolo è corretto")
else:
    print("IL PROGRAMMA NON FUNZIONA CORRETTAMENTE")