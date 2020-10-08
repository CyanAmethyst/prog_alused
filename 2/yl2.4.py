import random
valik=input("Kas soovite istekohta ise valisa (ise) või loosida (loos)? ")
if valik=="ise":
    koht=input("Kas soovite istuda akna ääres (aken) või mitte (muu)")
    if koht=="aken":
        print("Valisite ise. Aknakoht")
    elif koht=="muu":
        print("Valisite ise. Vahekäigukoht")
    else:
        print("Vale sisend")

else:
    arv=random.randint(0, 1)
    if arv==0:
        print("Istekoht loositi. Aknakoht")
    elif arv==1:
        print("Istekoht loositi. Vahekäigukoht")
    else:
        print("Vale sisend")

