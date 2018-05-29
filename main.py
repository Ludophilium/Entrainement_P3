"""Commencons par la fonction main(), la classe fenetre et niveau et tâchons de faire communiquer l'ensemble... On devrait se retrouver à la fin avec une fenêtre, le labyrinthe et la capacité de le fermer."""

import sys
import pygame


#import pygame.locals est aussi importable ou plutôt sa forme "from pygame.locals import *" histoire que je puisse utiliser ses constantes et méthodes sans devoir mettre pygame. devant. Si on refuse ceci on ferait mieux de juste importer pygame.

class Fenetre : #Possible qu'on utilise des attributs et méthodes de classe. | Voilà, c'est fait... Vu que le sprite de travail fait 30x30,  A voir.
    
    # pygame.init() ?

    def __init__(self) : #Faut-il définir les attributs (comme la resolution) au niveau de la classe fenêtre ou de la fonction main() ? | Essayons : main()
        self.titre = "Project (Mc)GYVR" #| Voilà, c'est fait... Vu que le sprite de travail fait 30x30,  A modifier ?
        self.taille_sprite = 30

    @property
    def icone (self) : #Devenu @property parce que ça générait une erreur quand il était initialisé lors de la création de l'objet   
        return pygame.image.load("mur.png").convert_alpha() #On utilise directement pygame.set_icon() ou on se contente de juste de charger ici l'argument qui n'est autre qu'une image ? | Bon, je vais essayer d'abord de juste charger l'image. Et puis ce serait difficile de tout faire en même temps vu qu'il faut préalablement charger l'image. On utilisera pygame.display.set_icon() lors de la génération de la fenetre, ce qui est cohérent en plus.

    @property
    def resolution (self) : #Faudra le modifier pour que ça corresponde à 15 sprites... | Voilà, c'est fait... Vu que le sprite de travail fait 30x30... 
        return [15*self.taille_sprite,15*self.taille_sprite]
    
    def generation(self) : 
        pygame.display.set_mode(self.resolution) #Et si on veut que l'utilisateur veut que la fenetre soit RESIZABLE (pygame.RESIZABLE) ? 
        pygame.display.set_icon(self.icone)
        pygame.display.set_caption(self.titre)
        
    def rafraichissement(self) : 
        pygame.display.flip() #Et si on appelle cette fonction avant generation() ? On ne va pas rencontrer un problème ? | Effectivement ça génère une erreur : "pygame.error: video system not initialized" | Ouais... De toute façon, cette erreur serait survenue aussi si on avait utilisé pygame.display.flip()... Donc... Il faut juste appeler les méthodes dans le bon ordre.  

class Niveau : #On pourrait en faire une simple property... | Après pourra-t-on faire : Niveau().generation().affichage() pour afficher un niveau...?
    def __init__(self) :
        self.name = "placeholder" # | Voilà, c'est fait... Vu que le sprite de travail fait 30x30,  A modifier
        self.textver = open("level_1.txt", 'r') #Deux possibilités. (1) Soit j'ouvre le fichier ici, (2) soit je charge un "context manager" plus tard et je mets donc juste le chemin vers le fichier ici. | Choix 2 pour le moment, parait plus "secure". | Finit par faire le (1), parce que cela rendait l'écriture de listver plus facile
        #self.sprite_mur = pygame.image.load("mur.png")# Attention : .convert() pas possible sans initialisation préalable. Et bien sûr, si on le lance avant le générer un display...

    @property
    def listver (self) : 
        return self.textver.readlines() #Whoa ! J'ai trouvé ça en fouillant dans la doc, me demandant entre autres ce qu'est IO.TextIOWrapper ! Même plus besoin de créer une liste, d'iterer sur le fichier, et de stocker chaque ligne de ce fichier dans une autre liste puis de stocker cette autre liste dans la première... | Là on a directement une liste où chaque membre est un str qui contient une ligne du fichier. Ext : ['wwwwwwwGwwwwwww\n', 'wwwwwww0wwwwwww\n',

    def iterate(self) :
            print(list(enumerate(self.listver)))

    def afficher(self, fenetre) : #peut-être un argument supplémentaire, listver...
        sprite_mur = pygame.image.load("mur.png").convert() #Déplacé ici car convert dans un __init__ génère une erreur.

        for x, a in enumerate(self.listver) : # 1 var et c'est le tuple qui sort. 2 et ce sont ses membres | #(0, 'wwwwwwwGwwwwwww\n'), (1, 'wwwwwww0wwwwwww\n'),...
            for y,b in enumerate(y) : 
                if b == 'w' : 
                    fenetre.blit() #fenetre ou pygame.display.set_mode(self.resolution)

        
        """Une fois de plus, qu'est-ce qu'on doit faire... 
            Iterer sur chaque membre de cette liste.
                Iterer sur chaque caractère de chaque str
                    Si on tombe sur un 'w' : afficher le sprite d'un mur à un certain endroit de l'écran, cet endroit dépendant de l'index de l'élément.
                    Si on tombe sur un '0', un 'S' ou un 'G' ou '\n' : ne rien faire """

    """

    ['wwwwwwwGwwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwww0wwwwwww\n', 'wwwwwwwSwwwwwww\n', '\n', '#Start Goal wall 0\n']

    classe Niveau :
        — Attr : name, structure_txt, structure_list, sprites ?
        — Meth : structure_txt_to_struct_list(generate), version_graphique
        
        
        """

def test() : 

    niveau = Niveau()

    #print(niveau.listver)

    niveau.afficher()



def main() : 
    
    pygame.init()

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