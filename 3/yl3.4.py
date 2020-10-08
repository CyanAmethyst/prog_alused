import random
poialpoisid=int(input("Mitu pöialpoissi tahab õunu? "))
ounad=14

while poialpoisid>=1:
    ounade_arv=random.randint(1,2)
    print(ounade_arv)
    ounad=ounad-ounade_arv
    poialpoisid-=1

print("Lumivalgekesele jäi "+str(ounad))