print ('hello, world ! bitch ass')

ensoleille = True
on_en_semaine = True
on_est_en_weekend = False

if ensoleille and not on_est_en_weekend:
    print("pas de plage demain je taff")
elif ensoleille and on_est_en_weekend:
    print("on va à la plage !")
else:
    print("on reste à la maison !")


nombre_de_sieges = 30
nombre_dinvites = 25

if nombre_dinvites < nombre_de_sieges:
    print("plus d'invité")
else:
    print("la salle est pleine")



fruit = "pomme"
match fruit:
    case "pomme":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes.")
    case "orange":
        print("Les oranges sont bonnes pour la santé.")
    case _:
        print("Je ne connais pas ce fruit.")


nombre_a_gauche = 23
nombre_a_droite = 9

symbole = "/"

resultat = 0

if not isinstance(nombre_a_gauche,int) or not isinstance (nombre_a_droite,int) :
    print ("erreur les variables ne sont pas des entiers")
    # isinstance me permet de vérifier le type de mon objet

match symbole :
    case "+" :
        print("symbole plus")
    case "-" :
        print("symbole moins")
    case "*" :
        print("symbole multiplication")
        if nombre_a_droite == 0 or nombre_a_droite == 0:
            print ("toute multiplication par 0 donne 0")
        else: 
            resultat = nombre_a_droite*nombre_a_gauche
            print(resultat)
    case "/" :
        if nombre_a_droite == 0:
            print ("impossible de diviser par 0")
        else:
            resultat = nombre_a_gauche/nombre_a_droite
            print (resultat)
        print ("symbole division")    

    case _:
        print("symbole inexistant")    