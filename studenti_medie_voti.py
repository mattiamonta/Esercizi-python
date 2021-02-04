'''Si definisca una funzione che preso un dizionario di studenti e voti, restituisca
un dizionario con gli studenti suddivisi per intervalli di media di voto: k1
(18,23), k2(24,26) e k3(27,30).
Nel calcolo della media la lode permette di arrotondare all’intero successivo,
nel caso in cui nella lista dei voti non sia presente una lode l’arrotondamento è
per difetto.
Esempio:
Dizionario di partenza:
studente_mediaVoti: [‘Alighieri’: [24,30,26]], [‘Boccaccio’: [18,22,24]],
[‘Manzoni’: [30,29,30], …………….]
Dizionario finale:
votoMedio_studenti: [(18,23): [‘Boccaccio’, ...], (24,27): [‘Alighieri’,.....], (28,30):
[‘Manzoni’, …….]]
'''

def stampa_studenti(diz):
    for studente in diz:
        print("Voti di", studente, ":")
        for voto_lode in diz[studente]:
            print("\t", voto_lode[0], end='')
            if voto_lode[1] == True:
                print(" Con lode")
            else:
                print()
        print()
        
def raggruppa_per_media(diz):
    voto_medio_studenti = dict()
    k1 = [18,23]
    k2 = [24,26]
    k3 = [27,30]
    k1_studenti = []    #contiene le medie voti comprese tra 18 e 23
    k2_studenti = []    #contiene le medie voti comprese tra 24 e 26
    k3_studenti = []    #contiene le medie voti comprese tra 27 e 30
    for studente in diz:
        somma_voti = 0
        trovato_lode = False
        for voto_lode in diz[studente]:
            somma_voti += voto_lode[0]
            if voto_lode[1] == True:
                trovato_lode = True
        
        media = somma_voti // len(diz[studente])
        if trovato_lode:
            media += 1
        
        if media>=min(k1) and media<=max(k1):
            k1_studenti.append(studente)
        elif media>=min(k2) and media<=max(k2):
            k2_studenti.append(studente)
        elif media>=min(k3) and media<=max(k3):
            k3_studenti.append(studente)

    voto_medio_studenti[str(k1)] = k1_studenti
    voto_medio_studenti[str(k2)] = k2_studenti
    voto_medio_studenti[str(k3)] = k3_studenti
    return voto_medio_studenti

def stampa_diz_finale(diz):
    for intervallo in diz:
        print("Studenti con media nell'intervallo", intervallo)
        for s in diz[intervallo]:
            print("\t", s)

studente_media_voti = dict()
while True:
    lista_voti = []     #contiene come elemnti sottoliste di 2 elementi: voto, True or False per la lode
    studente = input("Inserisci il nome dello studente (premi 0 per terminare): ")
    if studente == "0":
        break

    while True:
        voto_lista = [] #2 elementi: voto, True or False per la lode
        voto = int(input("Inserisci i voti dello studente " + studente + " (premi 0 per terminare): "))
        if voto == 0:
            break
        if voto<18 or voto>30:
            print("Inserisci un voto valido!")
        else:
            voto_lista.append(voto)
            if voto == 30:
                lode = input("Ha ottenuto la lode? (Digita S oppure N) ").capitalize()
                if lode == "S":
                    voto_lista.append(True)
                else:
                    voto_lista.append(False)
            else:
                voto_lista.append(False)

            lista_voti.append(voto_lista)

    studente_media_voti[studente] = lista_voti

stampa_studenti(studente_media_voti)
voto_medio_studenti = raggruppa_per_media(studente_media_voti)
stampa_diz_finale(voto_medio_studenti)