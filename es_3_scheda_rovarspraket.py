print("Rovarspraket, il linguaggio dei furfanti")
list_consonanti = ["q", "w", "r", "t", "y", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
while True:
    parola = input("Inserisci la parola da tradurre nel linguaggio dei furfanti (premi 0 per terminare): ")
    if parola == "0":
        break

    parola_tradotta = ""
    for l in parola:
        #if l!="a" and l!="e" and l!="i" and l!="o" and l!="u" and l!=" ":
        if l.lower() in list_consonanti:
            if l == l.lower():
                l = l + "o" + l
            else:
                l = l + "O" + l
        parola_tradotta = parola_tradotta + l

    print("La parola in rovarspraket è:",parola_tradotta)