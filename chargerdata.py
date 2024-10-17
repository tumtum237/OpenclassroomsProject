import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


titre_articles = soup.find_all("a", class_="govuk-link gem-print-link govuk-link--no-underline")
titres_des_articles = []
for titre in titre_articles:
    titres_des_articles.append(titre.string)
 



description = soup.find_all("p", class_="gem-c-document-list__item-description")
descriptions = []
for desc in description:
    descriptions.append(desc.string)
  

# Créer une liste pour les en-têtes
en_tete = ["titre", "desc"]

with open('data.csv', 'w') as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=',')
    writer.writerow(en_tete)
    for titre, desc in zip(titres_des_articles, descriptions):
        writer.writerow([titre, desc])
        



#------------

# mettre les manip d'ETL dans des fonctions 
from bs4 import BeautifulSoup
import csv


def extraire(url):
    reponse = requests.get(url)
    page = reponse.content

    # transforme (parse) le HTML en objet BeautifulSoup
    soup = BeautifulSoup(page, "html.parser")
    elements = soup.find_all("li", class_="gem-c-document-list__item")
    return elements


def transformer(element):
    titre = element.find("a", class_="govuk-link")
    description = element.find("p", class_="gem-c-document-list__item-description")
    return (titre.string, description.string)


def charger(donnees):
    en_tete = ["titre", "description"]
    # création du fichier data.csv
    with open("data.csv", "w", newline="") as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=",")
        writer.writerow(en_tete)

        for donnee in donnees:
            writer.writerow(donnee)


def etl(url):
    elements = extraire(url)
    resultats = [transformer(element) for element in elements]
    charger(resultats)


if __name__ == "__main__":
    etl("https://www.gov.uk/search/news-and-communications")




#--------
#creation du csv avec un code plus rapide

import requests
from bs4 import BeautifulSoup
import csv

# lien de la page à scrapper
url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)
page = reponse.content

# transforme (parse) le HTML en objet BeautifulSoup
soup = BeautifulSoup(page, "html.parser")

# récupération de tous les éléments
elements = soup.find_all("li", class_="gem-c-document-list__item")

resultats = []

for element in elements:
    titre = element.find("a", class_="govuk-link")
    description = element.find("p", class_="gem-c-document-list__item-description")
    donnee = (titre.string, description.string)
    resultats.append(donnee)

# création du fichier data.csv
en_tete = ["titre", "description"]
with open("data.csv", "w", newline="") as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=",")
    writer.writerow(en_tete)
    # zip permet d'itérer sur deux listes à la fois
    for donnee in resultats:
        writer.writerow(donnee)
