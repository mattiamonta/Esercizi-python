voti_giuseppe = int(input("Quanti voti ha ottenuto Giuseppe Tagliavini? "))
voti_gabriele = int(input("Quanti voti ha ottenuto Gabriele Rossi? "))
perc_giuseppe = voti_giuseppe/(voti_giuseppe+voti_gabriele)*100
perc_gabriele = voti_gabriele/(voti_giuseppe+voti_gabriele)*100
print("La percentuale dei voti di Giuseppe Tagliavini è",perc_giuseppe)
print("La percentuale dei voti di Gabriele Rossi è",perc_gabriele)
if perc_gabriele>perc_giuseppe:
    print("Gabriele Rossi ha ottenuto la maggioranza dei voti.")
elif perc_giuseppe<perc_gabriele:
    print("Giuseppe Tagliavini ha ottenuto la maggioranza dei voti.")
else:
    print("I due candidati hanno ottenuto lo stesso numero di voti.")
