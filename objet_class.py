class Carre :
    size = 5
    def calculate_area(self):
        return self.size*self.size
        

class Rectangle:
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color



class Hammers:
    def __init__(self,color = "red"):
        self.color = color

    def remove_nail(self, nail):
        "enleve clous"
        nail.remove()

    def hammer_in(self,nail):
        """enfonce le clous"""
        nail.nail_in()  

    def paint(self,color):
        """paint le marteau"""
        self.color = color
    
    def __repr__(self):
        """representation de l'objet."""
        return f"Marteau de coleur {self.color}"




class Screwdriver:
    """Tournevis."""

    def __init__(self, size = 3, color = "red"):
        """Initialise la taille."""
        self.size = size
        self.color = color

    def tighten(self, screw):
        """Serrer une vis."""
        screw.tighten()

    def loosen(self, screw):
        """Desserre une vis."""
        screw.loosen()

    def __repr__(self):
        """representation de l'objet."""
        return f"tournevis de taille {self.size}"



class Screw:
    """Vis."""

    MAX_TIGHTNESS = 5

    def __init__(self):
        """Initialise son degré de serrage."""
        self.tightness = 0

    def loosen(self):
        """Déserre le vis."""
        if self.tightness > 0:
            self.tightness -= 1

    def tighten(self):
        """Serre le vis."""
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1

    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        return "Vis avec un serrage de {}".format(self.tightness)




class Nail:
    """Clou."""

    def __init__(self):
        """Initialise son statut "dans le mur"."""
        self.in_wall = False

    def nail_in(self):
        """Enfonce le clou dans un mur."""
        if not self.in_wall:
            self.in_wall = True

    def remove(self):
        """Enlève le clou du mur."""
        if self.in_wall:
            self.in_wall = False

    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"Clou {wall_state}."
    



class ToolBox:
    def __init__(self):
        self.tools = []
        
    def add_tool(self, tool):
        """Ajoute un outil."""
        self.tools.append(tool)

    def remove_tool(self, tool):
        """Enleve un outil."""
        index = self.tools.index(tool)
        del self.tools[index]


hammer1 = Hammers()
screwdriver1 = Screwdriver()

toolbox = ToolBox()
toolbox.add_tool(hammer1)
toolbox.add_tool(screwdriver1)

print(toolbox.tools)


screw = Screw()
print(screw)
screwdriver1.tighten(screw)
print(screw)

# Instanciez un clou, puis enfoncez-le avec le marteau.
# Affichez le clou avant et après avoir été enfoncé.
nail = Nail()
print(nail)
hammer1.hammer_in(nail)
print(nail)


# --------------------------------------------------------------
# Que pouvez-vous faire d’autre avec ces classes et ces objets ?

# enlever un outil
print("outils dans la boîte:", toolbox.tools)
toolbox.remove_tool(hammer1)
print("on a enlevé le marteau")
print("outils dans la boîte:", toolbox.tools)

# désserrer la vis
screwdriver1.loosen(screw)
print(screw)

# enlever le clou
hammer1.remove(nail)
print(nail)

# repeindre le marteau
hammer1.paint("yellow")
print(hammer1)



"""class character :

    def __init__(self, name, power, speed, quote): 
        self.name = name
        self.power = power
        self.speed = speed
        self.quote = quote 

    def run():
        print ("I'm running")
    
    def restore():
        print ("I'm restoring")

warrior = character("guerrier", "rogue", 50, "it's time to die")
melissandre = character("melissandre","mage",10, "you don't know nothing, jon snow")
ninja = character("Naruto", "futon",90,"découvre la souffrance")


print(melissandre.quote)
character.run()

print (f"the ninja speed is : {ninja.speed}")
character.run()


print(f"le nom du guerrier : {warrior.name}")
print(f"the warrior said : {warrior.quote}")
character.restore()

warrior.name = "samorai"

print(warrior.name)"""



###classse et sous classe ###


"""Définit les classes propres à notre forum. ;)"""

from abc import ABC


class File(ABC):
    """Fichier."""

    def __init__(self, name, size):
        """Initialise le nom et la taille."""
        self.name = name
        self.size = size

    def display(self):
        """Affiche le fichier."""
        pass


class ImageFile(File):
    """Fichier image."""

    def display(self):
        """Affiche l'image."""
        print(f"Fichier image '{self.name}'.")


class GifImageFile(ImageFile):
    """Fichier image Gif."""

    def display(self):
        """Affiche l'image."""
        super().display()
        print("L'image est de type 'Gif'.")


class PNGImageFile(ImageFile):
    """Fichier image PNG."""

    def display(self):
        """Affiche l'image."""
        super().display()
        print("L'image est de type 'PNG'.")


class User:
    """Utilisateur."""

    def __init__(self, username, password):
        """Initialise le nom d'utilisateur et le mot de passe."""
        self.username = username
        self.password = password

    def login(self):
        """Connecte l'utilisateur."""
        print(f"L'utilisateur {self.username} est connecté.")

    def post(self, thread, content, file=None):
        """Poste un message dans un fil de discussion."""
        if file:
            post = FilePost(self, "aujourd'hui", content, file)
        else:
            post = Post(user=self, time_posted="aujourd'hui", content=content)
        thread.add_post(post)
        return post

    def make_thread(self, title, content):
        """Créé un nouveau fil de discussion."""
        post = Post(self, "aujourd'hui", content)
        return Thread(title, "aujourd'hui", post)

    def __str__(self):
        """représentation de l'utilisateur."""
        return self.username


class Moderator(User):
    """Utilisateur modérateur."""

    def edit(self, post, content):
        """Modifie un message."""
        post.content = content

    def delete(self, thread, post):
        """Supprime un message."""
        index = thread.posts.index(post)
        del thread.posts[index]


class Post:
    """Message."""

    def __init__(self, user, time_posted, content):
        """Initialise l'utilisateur, la date et le contenu."""
        self.user = user
        self.time_posted = time_posted
        self.content = content

    def display(self):
        """Affiche le message."""
        print(f"Message posté par {self.user} le {self.time_posted}:")
        print(self.content)


class FilePost(Post):
    """Message comportant un fichier."""

    def __init__(self, user, time_posted, content, file):
        """Initialise le fichier."""
        super().__init__(user, time_posted, content)
        self.file = file

    def display(self):
        """Affiche le contenu et le fichier."""
        super().display()
        print("pièce jointe:")
        self.file.display()


class Thread:
    """Fil de discussions."""

    def __init__(self, title, time_posted, post):
        """Initialise le titre, la date et les posts.

        Attention ici: on commence par un seul post, celui du sujet.
        Les réponses à ce post ne pourrons s'ajouter qu'ultérieurement.
        En effet, on ne créé pas directement un nouveau fil avec des réponses. ;)
        """
        self.title = title
        self.time_posted = time_posted
        self.posts = [post]

    def display(self):
        """Affiche le fil de discussion."""
        print("----- THREAD -----")
        print(f"titre: {self.title}, date: {self.time_posted}")
        print()
        for post in self.posts:
            post.display()
            print()
        print("------------------")

    def add_post(self, post):
        """Ajoute un post."""
        self.posts.append(post)





###collection d'objet dans une liste ###

class Human:

    def __init__(self, race, power):
        self.race = race
        self.power = power
    
    def run (self,power):
        self.power = power
        if self.power > 80:
            print("i'm running and i'm black")
        else:    
            print("i'm running but i'm not black")


class Felin:

    def __init__(self, power, speed):
        self.power = power
        self.speed = speed

    def run (self,power):
        self.power = power
        if self.power < 80:
            print("miaou")
        else:
            print("roar")

    def speak(self,speed):
        self.speed = speed
        if self.speed < 10:
            print(f"je suis garfield je sais parler, ma vitesse s'élève à : {self.speed}")
        elif self.speed > 70 and self.speed < 100:
            print("roar, c'est moi le roi lion")
        elif self.speed == 100:
            print ("c'est rob lucci")    
        else:
            print("miaou miaou")        



class cat(Felin):
    pass


salem = cat(20,70)
Garfield = cat(20,5)
Simba = Felin(100, 80)
Rob_lucci = cat(100,100)




print (salem.power)
salem.run(20)
Garfield.speak(5)
Simba.speak(80)
Rob_lucci.speak(100)

entities = [Human("black", 150), Felin(100,80), cat(20,5)]
for entity in entities:
    entity.run(60)


    
