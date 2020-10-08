ringid=int(input("Sisesta ringide arv: "))
porgandid=0
while ringid>=1:
    if ringid%2==0:
        porgandid+=ringid
        ringid-=1
    else:
        ringid-=1

print("Porgandide arv on "+str(porgandid))