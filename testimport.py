#from operations import addition

#addition (40,10)


#import operations

#operations.multiplication(4,5)

import csv

with open('input.csv', 'r') as csvfile:
    reader = csv.reader(csvfile) 
    for row in reader:
        nom = row[0]
        heures_travaillees = row[1]
        print(f"{nom} a travaillé {heures_travaillees} heures.")

en_tete = ("Nom", "Salaires")
with open ('output.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter= ',')
    writer.writerow(en_tete)
    
