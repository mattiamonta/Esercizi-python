print("Questo programma permette di eseguire un'equazione di primo grado del tipo ax + b = 0")
a = float(input("Inserisci il valore di a: "))
b = float(input("Inserisci il valore di b: "))
if a==0 and b==0:
    print("Il valore di x risulta essere indeterminato")
elif a==0 and b!=0:
    print("Il valore di x risulta essere impossibile")
elif a!=0 and b==0:
    print("Il risultato è x=0")
else:
    x = -b/a
    print("Il risultato è x=",x)