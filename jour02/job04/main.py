# je demmende de saisir un entier au dessue de zéro
while True:
    try:
        N = int(input("Saisissez un entier supérieur à zéro (N) : "))
        if N > 0:
            break
        else:
            print("Veuillez saisir un entier supérieur à zéro.")
    except ValueError:
        print("Veuillez saisir un nombre entier.")



        
# j'affiche les tables de multipliquation de 1 à infini
for i in range(1, N+1):
    print(f"\nTable de multiplication de {i} :")                               
    for j in range(1, 11):
        resultat = i * j
        print(f"{i} x {j} = {resultat}")
