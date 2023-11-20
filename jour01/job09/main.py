nom = "menu Mcfirst"
prix_unitaire = 6.50
quantité_en_stock = 1222

print("prix du",nom,prix_unitaire,"€")
print("il reste",quantité_en_stock,nom,"en stock pour aujourd'huit")


#la fameuse promo
promotion = 10

print ("BONNE NOUVELLE ! REDUCTION de",promotion,"%","sur le",nom,"ce qui revient donc à ")

#comme 6.50 diviser par 10 = 0.65
#alors je fais 6.50 moins 0.65 ce qui fait 5.85


total_promotion = 0.65

print (prix_unitaire - total_promotion,"€","le",nom,)     # et voilas la promotion apliquée !!!