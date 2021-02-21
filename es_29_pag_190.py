diz = {15000 : 23,
28000 : 27,
55000 : 38,
75000 : 41,
1000000000000 : 43}

reddito = int(input("Inserisci il reddito in euro: "))

imposta=0
scaglione_prec = 0
for scaglione in diz:
    importo_da_tassare=0
    if reddito>=scaglione:
        importo_da_tassare = scaglione-scaglione_prec
    elif reddito<scaglione and reddito>scaglione_prec:
        importo_da_tassare = reddito - scaglione_prec
    else:
        break
    
    imposta += importo_da_tassare * diz[scaglione] / 100
    scaglione_prec = scaglione

print("L'imposta totale è di euro: ", round(imposta,3))
tax = imposta * 100 / reddito
print("La tassazione media applicata è: ", round(tax,2), "%")

