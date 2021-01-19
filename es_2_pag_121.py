# data la parabola y = ax2 + bx + c calcola il vertice e il fuoco

def delta(n1, n2, n3):
    d = n2*n2 - 4*n1*n3
    return d

def vertice(n1, n2, n3):
    d = delta(a, b, c)
    v= {'x': -n2/2*n1 , 'y': -d/4*n1}  
    return v

def fuoco(n1,n2,n3):
    d = delta(a, b, c)
    f = {'x': -n2/2*n1 , 'y': 1-d/4*n1}
    return f

def printresult(v, f):
    print("Il vertice della parabola è (",v['x'],",",v['y'],")")
    print("Il fuoco della parabola è (",f['x'],",",f['y'],")")

a = float(input("Inserisci il valore di a: "))
b = float(input("Inserisci il valore di b: "))
c = float(input("Inserisci il valore di c: "))
v = vertice(a, b, c)
f = fuoco(a, b, c)
printresult(v, f)