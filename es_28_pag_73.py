studenti_list = []
while True:
    studente = []
    nome = input("Qual è il nome dello studente? [indicare 0 per terminare]")
    if nome=="0":
        break
    studente.append(nome)
    lancio = float(input("Quanti metri ha percorso il peso? "))
    studente.append(lancio)
    studenti_list.append(studente)
max = 0
nome_studente_max = ""
for s in studenti_list:
    if s[1] > max:
        max = s[1] 
        nome_studente_max = s[0]
print("Lo studente",nome_studente_max,"ha fatto il lancio più lungo con",max,"m")