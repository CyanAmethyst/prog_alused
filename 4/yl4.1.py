nimi=input("Sisestage oma nimi: ").split(" ")
vastus=[]
for i in nimi:
 vastus.append(i.lower().capitalize())

print(" ".join(vastus))