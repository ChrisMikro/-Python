#Xrhsimopoih8hke python 3.6
print ("Tha kataskeuastei mia lista kai tha vrethei h tupikh ths apoklish")
lista=list()
n=int(input("Dwse sunolo stoixeiwn ths listas"))
while (n<5):
    n=int(input("lanthasmenh timh , dwse arithmo megalutero-iso tou 5"))
if (n==5):
    print ("H tupikh apoklish einai 0")
else:
    i=1
    while (i<=n):
        stoixeio=float(input("dwse stoixeio listas"))
        lista.append(stoixeio)
        i=i+1
    lista.sort()
    j=2
    athr1=0
    while (j<=(n-3)):
        athr1=athr1+lista[j]
        j=j+1
    meshtimh=athr1/(n-4)
    k=2
    athr2=0
    while (k<=(n-3)):
        athr2=athr2+(lista[k]-meshtimh)**2
        k=k+1
    sigmatetragwno= athr2/(n-4)
    tupikh=sigmatetragwno**(1/2)
    print ("h tupikh apoklish einai " , tupikh)
