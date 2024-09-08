nom = "Snow"
prenom = "Jon"
taille = 1.80
Is_student = False
plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]

print (f"Salut, moi c'est {prenom} {nom} je mesure {taille} metres, étudiant ? {Is_student}")

print (type(nom)) 
print (type(prenom))
print (type(taille))
print (type(Is_student))


fruits = ["pomme","orange","banane"]
print (fruits)

fruits.append("kiwi")
print (fruits)

fruits.remove("orange")
print (fruits)

fruits[2] = "ananas"
print (fruits)

fruits.count("pomme")

fruits.sort()
print (fruits)

fruits.reverse()
print (fruits)

fruits.pop()
Dico={"loup_blanc":"jon snow","une_fille":"arya","chien":"clegane"}

Portrait_philo_jon = {
    "nom":"Jon Snow", "philosophie":"le devoir", "devise":"l'amour eest la mort du devoir",
    "Allégeance":("Stark","targaryen","baratheon"),
    "Siblings":["Robb","Bran","Arya","Sansa","Neth"],
    "Titre" : "Roi de l'hiver"
}

physique_jon = {}
physique_jon["yeux"] = "noir"
physique_jon["taille"]= 1.80
physique_jon["cheveux"] = "noir"

physique_jon.keys()
physique_jon.values()
print(physique_jon)

Portrait_philo_jon["origine"] = "first men"
Portrait_philo_jon.items()

Portrait_philo_jon.pop("origine")
print(Portrait_philo_jon)

"taille" in physique_jon


fruits={
    "orange":"orange", "pomme":"rouge","banane":"jaune"
}

fruits["kiwi"] = "vert"

couleur_banane = fruits["banane"]

fruits["pomme"] = "vert"

fruits.pop["banane"]

fruits.items()
