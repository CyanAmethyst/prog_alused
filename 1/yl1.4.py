nimi=input("Sisestage oma nimi: ")
lubatud_kiirus=int(input("Sisestage lubatud kiitus (km/h): "))
tegelik_kiirus=int(input("Sisestage tegelik kiitus (km/h): "))
trahv=(tegelik_kiirus-lubatud_kiirus)*3
print(nimi+", kiiruse ületamise eest on teie trahv "+str(min(190,trahv))+" eurot.")