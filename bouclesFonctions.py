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
def afficher_message ():
    print("hello boy")

afficher_message()


