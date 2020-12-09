import math
q = "quadrato"
r = "rettangolo"
c = "cerchio"
t = "triangolo"
area=input("Vuoi calcolare l'area del " + q + ", del "+ r + ", del " + c + " o del " + t + " ? ")
if area==q:
    lato=float(input("Inserisci il lato del quadrato: "))
    area_quadrato=lato**2
    print("L'area del",area,"è",round(area_quadrato,2))
elif area==r:
    base_rettangolo=float(input("Inserisci la base del rettangolo: "))
    altezza_rettangolo=float(input("Inserisci l'altezza del rettangolo: "))
    area_rettangolo=base_rettangolo*altezza_rettangolo
    print("L'area del",area,"è",round(area_rettangolo,2))
elif area==t:
    base_triangolo=float(input("Inserisci la base del triangolo: "))
    altezza_triangolo=float(input("Inserisci l'altezza del triangolo: "))
    area_triangolo=base_triangolo*altezza_triangolo/2
    print("L'area del",area,"è",round(area_triangolo,2))
elif area==c:
    raggio_cerchio=float(input("Inserisci il raggio del cerchio: "))
    area_cerchio=raggio_cerchio**2*math.pi
    print("L'area del",area,"è",round(area_cerchio,2))
else:
    print("Questo programma calcola solo l'area del quadrato, del rettangolo, del triangolo o del cerchio?")