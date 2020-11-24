candidato_1 = input("Dimmi il nome del primo candidato: ")
candidato_2 = input("Dimmi il nome del secondo candidato: ")
punteggio_1 = int(input("Qual è il punteggio del primo candidato? "))
punteggio_2 = int(input("Qual è il punteggio del secondo candidato? "))
lista = [candidato_1,candidato_2]
lista_punt = [punteggio_1,punteggio_2]
print(min(lista),max(lista))
lista_punt.sort()
lista_punt.reverse()
print(lista_punt)