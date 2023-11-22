def crosse_volé(nombre):
    if nombre > 0:
        print("positif")
                            #je mets mes conditions
    elif nombre < 0:
        print("negatif")

    else:
        print("0 pour toujour")

#je fais mon appel à la fonction
crosse_volé(666)       #ça affichera positif car c'est au dessus de 0
crosse_volé(900)       #ça affichera positif car c'est au dessus de 0
crosse_volé(-700)      #ça affichera negatif car c'est en dessous de 0
crosse_volé(0)         #ça affichera "0 pour toujour", comme je l'ai mis dans la condition "else"