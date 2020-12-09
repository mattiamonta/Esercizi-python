print("Verifica palindromo")
parola = input("Inserisci la parola da verificare: ")

# 1 metodo di inversione
parola_invert1 = ""
for l in parola:
    parola_invert1 = l + parola_invert1
print("Parola ribaltata (1 metodo):", parola_invert1)

# 2 metodo di inversione
parola_invert2 = ""
for i in range(len(parola)-1,-1,-1):
    parola_invert2 = parola_invert2 + parola[i]
print("Parola ribaltata (2 metodo):", parola_invert2)

# 3 metodo di inversione
parola_list = list(parola)
parola_list.reverse()
separator = ""
parola_invert3 = separator.join(parola_list)
print("Parola ribaltata (3 metodo):", parola_invert3)

if (parola_invert1!=parola_invert2) or (parola_invert2!=parola_invert3) or (parola_invert1!=parola_invert3):
    print("Uno dei metodi di ribaltamento ha fallito!")
else:
    if parola == parola_invert1:
        print(parola,"è un palindromo")
    else:
        print(parola,"non è un palindromo")