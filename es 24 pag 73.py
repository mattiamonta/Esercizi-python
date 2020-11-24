candidato1 = input("Inserisci il nome del primo candidato: " )
candidato2 = input("Inserisci il nome del secondo candidato: " )
voti_candidato1 = int(input("Quanti voti ha ottenuto il primo candidato? "))
voti_candidato2 = int(input("Quanti voti ha ottenuto il secondo candidato? "))
perc_candidato1 = voti_candidato1/(voti_candidato1+voti_candidato2)*100
perc_candidato2 = voti_candidato2/(voti_candidato1+voti_candidato2)*100
print("La percentuale dei voti di ",candidato1, "è",perc_candidato1)
print("La percentuale dei voti di ",candidato2 ,"è",perc_candidato2)
if perc_candidato2>perc_candidato1:
    print(candidato2, "ha ottenuto la maggioranza dei voti.")
elif perc_candidato1<perc_candidato2:
    print(candidato1, "ha ottenuto la maggioranza dei voti.")
else:
    print("I due candidati hanno ottenuto lo stesso numero di voti.")
