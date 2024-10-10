import requests

from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.title)
soup.find_all('a')

title = soup.title 
h1content = soup.find_all("h1")

titre_articles = soup.find_all("a", class_="govuk-link govuk-link--no-underline")
titres_des_articles = []
for titre in titre_articles:
    titres_des_articles.append(titre.string)
print(titres_des_articles)


description = soup.find_all("p", class_="gem-c-document-list__item-description")
descriptions = []
for desc in description:
    descriptions.append(desc.string)
print(descriptions)


prixeuro = [12, 4.5, 6, 9, 7]
prixdollars = []
#prixdollar = prixeuro * 1.2

for prix in prixeuro:
    prixdollar = prix * 1.2
    prixdollars.append(prixdollar)
print(prixdollars)
print(prixeuro)




