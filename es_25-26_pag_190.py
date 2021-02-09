'''
Es. 25 pag. 190
I voti assegnati a 30 studenti di una classe in una prova di italiano sono memorizzati in un dizionario
che ha per chiave la matricola, mentre il valore associato è il voto. Elenca i risultati in ordine crescente di voto
e successivamente visualizza quali voti diversi tra loro sono stati assegnati, riducendo a uno i voti uguali.

Es. 26 pag. 190
Con riferimento al dizionario del problema precedente, elenca i numeri di matricola degli studenti che hanno ottenuto
una votazione superiore alla media di tutte le votazioniù
'''
def stampa(dizionario):
    print("Lista voti:")
    for chiave in dizionario:
        print(chiave, ":", dizionario[chiave])

def media_voti(dizionario):
    lista_voti_sommati = []
    somma = 0
    for voto in dizionario.values():
        somma += voto
        lista_voti_sommati.append(voto)
    media = somma/len(lista_voti_sommati)
    return media


# Es 25
diz = dict()
while True:
    matricola = int(input("Inserisci la matricola (0 = fine): "))
    if matricola == 0:
        break
    voto = float(input("Inserisci il voto: "))
    diz[matricola] = voto
    if len(diz) > 30:
        print("Il numero massimo di studenti che possono aver eseguito la prova è 30")
        break

stampa(diz)
# Ordino il dizionario per matricola
chiavi_ord = sorted(diz)
print(chiavi_ord)
diz_ord = dict()
for chiave in chiavi_ord:
    diz_ord[chiave] = diz[chiave]
print("La lista ordinata per numero di matricola è:")
stampa(diz_ord)

# Ordino il dizionario per voto
voti_ord = sorted(diz.values())
diz_ord_by_voto = dict()
for voto in voti_ord:
    for mat in diz:
        if diz[mat]==voto:
            diz_ord_by_voto[mat]=voto
print("La lista ordinata per voto è:")
stampa(diz_ord_by_voto)

# Trovo i voti assegnati diversi tra loro
voti_univoci = []
for matricola in diz:
    voto = diz[matricola]
    #trovato=False
    #for e in voti_univoci:
    #    if voto == e:
    #        trovato=True
    #if trovato==False:
    #    voti_univoci.append(voto)
    if voto not in voti_univoci:
        voti_univoci.append(voto)
print("Questi sono i voti tra loro diversi, i voti uguali sono scritti una sola volta")
for e in voti_univoci:
    print(e)

#Es. 26 - scrivere la media dei voti ed elencare gli studenti con voto >= media
media = media_voti(diz)
lista_studenti_sopra_media = []
for matricola in diz:
    if diz[matricola] >= media:
        lista_studenti_sopra_media.append(matricola)

print("Gli studenti che hanno un voto individuale maggiore o uguale alla media generale di", media, "sono:")
for e in lista_studenti_sopra_media:
    print(e)