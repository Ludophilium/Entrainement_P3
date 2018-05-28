"""Commencons par la fonction main(), la classe fenetre et niveau et tâchons de faire communiquer l'ensemble... On devrait se retrouver à la fin avec une fenêtre, le labyrinthe et la capacité de le fermer."""

import sys
import pygame
#import pygame.locals est aussi importable ou plutôt sa forme "from pygame.locals import *" histoire que je puisse utiliser ses constantes et méthodes sans devoir mettre pygame. devant. Si on refuse ceci on ferait mieux de juste importer pygame.

class Fenetre : #Possible qu'on utilise des attributs et méthodes de classe. A voir.
    
    def __init__(self) : #Faut-il définir les attributs (comme la resolution) au niveau de la fenêtre ou de la 
        self.resolution = (640,640) #Faudra le modifier pour que ça corresponde à 15 sprites... A voir plus tard, c'est un autre problème...
        self.icone = pygame.image.load("mur.png") #On utilise directement pygame.set_icon() ou on se contente de juste de charger ici l'argument qui n'est autre qu'une image ? | Bon, je vais essayer d'abord de juste charger l'image. Et puis ce serait difficile de tout faire en même temps vu qu'il faut préalablement charger l'image. On utilisera pygame.display.set_icon() lors de la génération de la fenetre, ce qui est cohérent en plus.
        self.titre = "Project (Mc)GYVR" #A modifier ?

    def generation(self) : 
        pygame.display.set_mode(self.resolution) #Et si on veut que l'utilisateur veut que la fenetre soit RESIZABLE (pygame.RESIZABLE) ? 
        pygame.display.set_icon(self.icone)
        pygame.display.set_caption(self.titre)
        
    def rafraichissement(self) : 
        pygame.display.flip() #Et si on appelle cette fonction avant génération ? On ne va pas rencontrer un problème ?

class Niveau :
    pass

def main() : 
    
    fenetre = Fenetre()

    fenetre.generation()

    while 0<1 :
        
        pygame.time.Clock().tick(30)

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT or evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE : 
                print("Giscard : \"...Au revoir.\"")
                pygame.quit()
                sys.exit()

        fenetre.rafraichissement()

if __name__ == "__main__" : 
    main()