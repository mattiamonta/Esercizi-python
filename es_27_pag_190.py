'''
Organizza con un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici.
Fornito poi il nome della persona, il programma visualizza il suo numero di telefono oppure un 
messaggio nel caso la persona non sia presente nella rubrica.
'''
def stampa(dizionario):
    print("Rubrica:")
    for chiave in dizionario:
        print(chiave, ":", dizionario[chiave])

diz = dict()
while True:
    nome = input("Inserisci il nome di cui vuoi memorizzare il numero telefonico (0 per terminare): ")
    if nome == "0":
        break
    numero_telefonico = input("Inserisci il suo numero di telefono: ")
    diz[nome]=numero_telefonico

stampa(diz)

while True:
    num_sconosciuto = input("Di chi vuoi sapere il numero di telefono (0 per uscire)? ")
    if num_sconosciuto == "0":
        break
    if num_sconosciuto in diz:
        print("Il numero di telefono di", num_sconosciuto, "è", diz[num_sconosciuto])
    else:
        print("Il numero di telefono di", num_sconosciuto, "non è presente nella rubrica")
