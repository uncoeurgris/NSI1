# 7.1 -- "Convertir un nombre de la base 10 à la base 2"

# Création de la fonction conversion qui prend en argument d qui signifie "décimal", de type integer (entier)
def conversion(d: int):
    # Création du help(conversion) => spécification
    """Conversion de la base 10 (décimal) à la base 2 (binaire)"""
    #### Assertion de précondition ####
    # On teste le type du nombre choisi et on vérifie qu'il est bien de type integer
    assert type(d) == int, "Le programme ne prend en charge que les nombres entiers"
    # On initialise la variable qui contiendra le nombre binaire
    b = ''
    # Si le nombre décimal choisi est égal à 0
    if d == 0:
        # On affecte la valeur de 0 à la variable binaire
        b = '0'
    # Si le nombre décimal choisi est négatif
    elif d < 0: 
        # On affecte un message d'erreur à la variable binaire
        b = 'Erreur, le nombre doit être positif'
        # Tant que le nombre décimal est positif (boucle non bornée (while))
    while d > 0:
        # On ajoute le reste de la division par 2 sous forme string au début de la variable binaire
        b = str(d % 2) + b
        # On divise le nombre décimal par 2
        d = d // 2
        # On renvoie le nombre binaire
    return b

def fonctionPrincipale():
    """Fonction principale qui permet de convertir un nombre décimal en binaire par le biais d'un input; se réfère à la fonction conversion"""
    # On demande à l'utilisateur de choisir un nombre décimal
    d = int(input("Entrez un nombre entier positif: "))
    # On affiche le résultat de la fonction conversion
    print(conversion(d))
# Appel de la fonction 
fonctionPrincipale()

############# Assertions de postcondition #############
# On teste la fonction avec le nombre 0
assert conversion(0) == '0', "Erreur de conversion de 0 en binaire. Le résultat attendu est 0 or le résultat obtenu est " + conversion(0)
# On teste la fonction avec un nombre choisi au hasard, 1838
assert conversion(1838) == '11100101110', "Erreur de conversion de 1838 en binaire ! Le résultat attendu est 11100101110 or le résultat obtenu est " + conversion(1838)
# On teste la fonction avec un nombre négatif
assert conversion(-1) == 'Erreur, le nombre doit être positif', "Une erreur est survenue, le programme ne prend pas en charge les nombres négatifs"
