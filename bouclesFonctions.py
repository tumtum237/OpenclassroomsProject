print ('hello, world ! bitch ass')


#boucles for : la boucle for permet de lancer un code un nombre de fois spécifique,
#le temps d'une liste, un tulpe ou un dico :
for x in range(6):
    print(x)

marques_de_basket = ("nike","adidas","NB","reebook","puma")

print (isinstance(marques_de_basket,tuple))

for shoes in marques_de_basket:
    print(f"{x}{shoes} à distribuer aux participants du tournoi")

for y in range(1,6):
    print (f"déjà {y}h travaillée cette semaine")


#boucles while : continue de s'exécuter tant qu'une codition n'est pas rempli
Capacite_max = 20
capacite_actuelle = 2
while capacite_actuelle < Capacite_max:
    capacite_actuelle += 1
    if capacite_actuelle == 15:
        break
print(capacite_actuelle)


#break et continue pour casé et continuer une boucle à tout momment, 
# "continue" va faire sauter la valeur sans exécuter le code pour elle et passzer à la suivante
# "break" va s'arreter à la valeur sans aller au bout de la liste 
for p in range (20):
    if p == 5:
        break 
    print(p)


liste = ["A","B","C","D","E","F"]
for element in liste : 
    if element == "D":
        continue
    print(element)

#exercice
liste_de_nombre = [3,4,5,6,7,8,9,10,12]
print (liste_de_nombre)

print (sum(liste_de_nombre))

somme = sum(liste_de_nombre)
nombre_element = len(liste_de_nombre)
moyenne = somme/nombre_element
print (moyenne)


compteur = 0
for element in liste_de_nombre:
    if element < 7:
        continue
    elif element > 7:
     compteur += 1
    print (compteur)


compteur = 0
for nombre in liste_de_nombre:
    if nombre % 2 == 0:
        compteur += 1
        print (compteur)
 
    
#fonctions

# sans paramètre
def afficher_message ():
    print("hello boy")

afficher_message()

# Avec paramètre
def nom_prenom (nom, prenom):
    print ("nom :", nom)
    print ("prenom :", prenom)


nom_prenom("Dikongue", "wilfried")  


def avg (somme_element, nombre_element):
    resultat = somme_element/nombre_element
    return resultat




def addition(y,z):
    solution = y + z
    return solution, y, z

y=5
z =10
retour = addition(y,z)
print (retour)


#Exercice
def salaire_mensuel(salaire_annuel, months_in_year):
    resultat = salaire_annuel/months_in_year
    return resultat

salaire_annuel = 34000
months_in_year = 12
rendu = salaire_mensuel (salaire_annuel,months_in_year)

print (rendu)


def salaire_hebdo(salaire_mensuel, weeks_in_months):
    resultat = salaire_mensuel/weeks_in_months
    return resultat

salaire_mensuel = 2833
weeks_in_months = 4
rendu = salaire_hebdo(salaire_mensuel,weeks_in_months)

print (rendu)



def salaire_horaire(): 
 while True:
    try:
        salaire_hebdo = float(input("entre ton salaire hebdo :"))
        taux_horaire = int(input("entre tes heures semaine : "))
        salaire_horaire = salaire_hebdo/taux_horaire
        print(salaire_horaire)
        break
    except ValueError:
       print("Attention, entre un montant valide")      


salaire_horaire ()





def calculer_salaire_mensuel():

  while True:
    try:
      salaire_annuel = float(input("Veuillez saisir votre salaire annuel : "))
      if salaire_annuel <= 0:
        print("Veuillez saisir un salaire annuel positif.")
      else:
        break
    except ValueError:
      print("Veuillez entrer un nombre valide.")

  salaire_mensuel = salaire_annuel / 12
  print("Votre salaire mensuel est de :", salaire_mensuel)

# Appel de la fonction pour l'utiliser
calculer_salaire_mensuel()


while True:
   try:
      prixHT = int(input("Entre le prix hors taxe"))
      prixTTC = prixHT+prixHT*0.2
      print(prixTTC)
      break
   except ValueError:
      print("Attention, tu dois mettre un nombre")