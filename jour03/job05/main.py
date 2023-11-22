def calcule(num1, operator, num2):
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '//':
        return num1 // num2
    
le_resultat_soustraction = calcule(5,'-',2)
le_resultat_addition = calcule(9,'+',10)
le_resultat_multiplication = calcule(4,'*',4)
le_resultat_division = calcule(38,'//',2)


print ("La soustraction fait",le_resultat_soustraction)
print ("Addition",le_resultat_addition)
print ("Multiplication",le_resultat_multiplication)
print ("Division",le_resultat_division)