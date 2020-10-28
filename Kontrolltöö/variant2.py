import random
hind=float(input("Sisesta kõneminuti hind: "))
arv=int(input("Sisesta kõneminutite arv: "))

turniir=[]
summa=0

while arv!=0: #genereerib vajaliku arvu juhuslikke numbreid
    i=random.randint(1, 1000) #genereerib juhuslikke arve
    turniir.append(i) #lisab juhusliku arvu listi
    arv-=1

def kone_maksumus(kestus, hind):
    if kestus<60: #minimaalne kõne hind
        return round(1*hind,2)
    elif kestus>600: #maximaalne kõne hind
        return round(10*hind,2)
    else:
        return round((kestus/60)*hind,2) #kõne hind

for i in turniir: #loeb ühe kaupa kõne kestvused
    print("Kõne maksumus: "+str(kone_maksumus(i, hind))) #arvutab iga kõne hinna
    summa+=kone_maksumus(i, hind) #lisab iga kõne hinna kogu arvesse

print("Kogu arve: "+str(round(summa,2))+"EUR")