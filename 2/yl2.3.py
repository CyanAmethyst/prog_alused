vanus=int(input("Sisestage enda vanus: "))
sugu=input("Sisestage enda sugu (M/N): ")
treening_tyyp=int(input("Sisestage treeningu tüüp (1/2/3): "))
if sugu.lower()=="n":
    if treening_tyyp==1:
        pulss1=0.5*(206-0.88*vanus)
        pulss2=0.7*(206-0.88*vanus)
    elif treening_tyyp==2:
        pulss1=0.7*(206-0.88*vanus)
        pulss2=0.8*(206-0.88*vanus)
    else:
        pulss1=0.8*(206-0.88*vanus)
        pulss2=0.87*(206-0.88*vanus)
else:
    if treening_tyyp==1:
        pulss1=0.5*(220-0.88*vanus)
        pulss2=0.7*(220-0.88*vanus)
    elif treening_tyyp==2:
        pulss1=0.7*(220-0.88*vanus)
        pulss2=0.8*(220-0.88*vanus)
    else:
        pulss1=0.8*(220-0.88*vanus)
        pulss2=0.87*(220-0.88*vanus)

print("Pulsisagedus peaks olema vahemikus "+str(round(pulss1))+" kuni "+str(round(pulss2)))