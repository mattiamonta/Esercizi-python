lista_stip = []
while True:
    stipendio=int(input("A quanto ammonta lo stipendio del dipendente? (se viene inviata la quota -1 verrà calcolata la media) "))
    if stipendio == -1:
        break
    else:
        lista_stip.append(stipendio)

media = sum(lista_stip)/len(lista_stip)
print("Media stipendi: " + str(media))
