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



