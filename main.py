#Commencons par la fonction main(), la classe fenetre et niveau et tâchons de faire communiquer l'ensemble... On devrait se retrouver à la fin avec une fenêtre, le labyrinthe et la capacité de le fermer.

import pygame
#import pygame.locals est aussi importable ou plutôt sa forme "from pygame.locals import *" histoire que je puisse utiliser ses constantes et méthodes sans devoir mettre pygame. devant. Si on refuse ceci on ferait mieux de juste importer pygame.

class Fenetre : #Possible qu'on utilise des attributs et méthodes de classe. 
    
    def __init__(self) : #Faut-il définir les attributs (comme la resolution) au niveau de la fenêtre ou de la 
        self.resolution = (640,640) #Faudra le modifier pour que ça corresponde à 15 sprites... A voir plus tard, c'est un autre problème...
        


class Niveau :
    pass

def main() : 
    pass

if __name__ == "__main__" : 
    main()