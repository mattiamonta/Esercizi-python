print("Inserisci una di queste coppie di valori:\n (-5,2), (5,-5), (10,2), (-4,-5), (5,4), (-3,-2)")
a = float(input("Inserisci il primo numero: "))
b = float(input("Inserisci il secondo numero: "))
prodotto = a*b
differenza = a-b
somma = a+b
if prodotto > 10:
    print("La differenza tra il primo e il secondo numero è",differenza)
elif prodotto <= 10:
    print("La somma tra il primo e il secondo numero è",somma)