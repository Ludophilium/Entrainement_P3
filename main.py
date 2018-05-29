"""Commencons par la fonction main(), la classe fenetre et niveau et tâchons de faire communiquer l'ensemble... On devrait se retrouver à la fin avec une fenêtre, le labyrinthe et la capacité de le fermer."""

import sys
import pygame

#import pygame.locals est aussi importable ou plutôt sa forme "from pygame.locals import *" histoire que je puisse utiliser ses constantes et méthodes sans devoir mettre pygame. devant. Si on refuse ceci on ferait mieux de juste importer pygame.

class Fenetre : #Possible qu'on utilise des attributs et méthodes de classe. A voir.
    
    def __init__(self) : #Faut-il définir les attributs (comme la resolution) au niveau de la classe fenêtre ou de la fonction main() ? | Essayons : main()
        self.titre = "Project (Mc)GYVR" #A modifier ?
        self.resolution = (640,640) #Faudra le modifier pour que ça corresponde à 15 sprites... A voir plus tard, c'est un autre problème...
        self.icone = pygame.image.load("mur.png") #On utilise directement pygame.set_icon() ou on se contente de juste de charger ici l'argument qui n'est autre qu'une image ? | Bon, je vais essayer d'abord de juste charger l'image. Et puis ce serait difficile de tout faire en même temps vu qu'il faut préalablement charger l'image. On utilisera pygame.display.set_icon() lors de la génération de la fenetre, ce qui est cohérent en plus.

    def generation(self) : 
        pygame.display.set_mode(self.resolution) #Et si on veut que l'utilisateur veut que la fenetre soit RESIZABLE (pygame.RESIZABLE) ? 
        pygame.display.set_icon(self.icone)
        pygame.display.set_caption(self.titre)
        
    def rafraichissement(self) : 
        pygame.display.flip() #Et si on appelle cette fonction avant generation() ? On ne va pas rencontrer un problème ? | Effectivement ça génère une erreur : "pygame.error: video system not initialized" | Ouais... De toute façon, cette erreur serait survenue aussi si on avait utilisé pygame.display.flip()... Donc... Il faut juste appeler les méthodes dans le bon ordre.  

class Niveau : #On pourrait en faire une simple property... | Après pourra-t-on faire : Niveau().generation().affichage() pour afficher un niveau...
    def __init__(self) :
        self.name = "placeholder" # A modifier
        self.niveau = "level_1.txt" #Deux possibilités. (1) Soit j'ouvre le fichier ici, (2) soit je charge un "context manager" plus tard et je mets donc juste le chemin vers le fichier ici. | Choix 2 pour le moment, parait plus "secure".
        self.sprite_mur = pygame.image.load("mur.png")

    @property
    def generation (self) : 
        f = open(self.niveau, 'r') :
            l = list()
            l.append(f.readlines()) #Whoa ! J'ai trouvé ça en fouillant dans la doc, me demandant entre autres ce qu'est IO.TextIOWrapper ! Même plus besoin de créer une liste, d'iterer sur le fichier, et de stocker chaque ligne de ce fichier dans une autre liste puis de stocker cette autre liste dans la première... | Là on a directement une liste où chaque membre est un str qui contient une ligne du fichier.
            print(l) 

    """Ce qu'on doit faire ? 
    - lire le fichier ligne par ligne
    - Itérer sur cette ligne
    - Ajouter le contenu de chaque ligne dans une liste vide,
    - Ajouter cette ligne à structure_ls 

    INUTILE MAINTENANT QU'ON A CA :

    ['wwwwwwwGwwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwwwSwwwwwww\n', '\n', '#Start Goal wall 0\n']"""

    def afficher(self) : 
        pass


"""classe Niveau :
        — Attr : name, structure_txt, structure_list, sprites ?
        — Meth : structure_txt_to_struct_list(generate), version_graphique"""

def test() : 
    niveau = Niveau()

    niveau.generation

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
    test()
    #main()