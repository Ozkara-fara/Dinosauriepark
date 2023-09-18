#hur många dinosaurier har du tämjt?
AntalDinosaurier = float(input("Hur många dinosaurier har du tämjt? "))
#Hur många dinosaurier har dött?
Antaldöda = float(input("hur många dinosaurier har dött? "))
#totalt antal
Totalt = AntalDinosaurier - Antaldöda

if Totalt < 0:
    print ("Här har du räknat fel. Det går inte att ha mindre än 0 dinosaurier. Testa igen!")
elif Totalt == 0:
    print ("Du har inga dinosaurier, eller så har alla dött")
else:
    print ("Du har " + str(Totalt) + " dinosaurier.")