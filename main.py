"""Commencons par la fonction main(), la classe fenetre et niveau et tâchons de faire communiquer l'ensemble... On devrait se retrouver à la fin avec une fenêtre, le labyrinthe et la capacité de le fermer."""

import sys
import pygame

#pygame.init() #Pas très "propre" mais au moins ça contre les problèmes que sa non-initialisation pourrait causer. 
#import pygame.locals est aussi importable ou plutôt sa forme "from pygame.locals import *" histoire que je puisse utiliser ses constantes et méthodes sans devoir mettre pygame. devant. Si on refuse ceci on ferait mieux de juste importer pygame.

class FenetreC : #Une approche FONCTIONNELLE de construction de la Classe Fenetre | Attention, ce code est lu qu'on appelle FenetreC ou pas ! Autant ce n'est pas grave vu que c'est un composant essentiel, autant si on veut la lire sur commande... 
    
    TITRE = "Project (Mc)GYVR"  
    CELL_SIZE = 30 #30 parce que le sprite de travail fait 30x30 et qu'une cellulle fera sans doute 30x30.
    RESOLUTION = [15*CELL_SIZE,15*CELL_SIZE]
    ICONE_PTH = pygame.image.load("mur.png") #Suffit d'ajouter .convert_alpha et un problème surgit

    FENETRE = pygame.display.set_mode(RESOLUTION) #Et si on veut que l'utilisateur veut que la fenetre soit RESIZABLE (pygame.RESIZABLE) ?
    TITLE_FEN = pygame.display.set_caption(TITRE)
    ICONE_PRG = pygame.display.set_icon(ICONE_PTH.convert_alpha())

    @classmethod    
    def rafraichissement(cls) : 
        pygame.display.flip() 

class Fenetre : #Autre approche **PAS FONCTIONNELLE.** de construction de la classe Fenetre.  
    
    def __init__(self) :
        self.TITRE = "Project (Mc)GYVR"  
        self.CELL_SIZE = 30 #30 parce que le sprite de travail fait 30x30 et qu'une cellulle fera sans doute 30x30.
        self.RESOLUTION = [15*self.CELL_SIZE,15*self.CELL_SIZE]
        self.ICONE = pygame.image.load("mur.png") #Suffit d'ajouter .convert_alpha et un problème surgit

    @property
    def generation(self) :
        pygame.display.set_mode(self.RESOLUTION) #Et si on veut que l'utilisateur veut que la fenetre soit RESIZABLE (pygame.RESIZABLE) ? 

    def extra(self) : 
        pygame.display.set_icon(self.ICONE.convert_alpha())
        pygame.display.set_caption(self.TITRE)
    
    def rafraichissement(self) : 
        pygame.display.flip() #Et si on appelle cette fonction avant generation() ? On ne va pas rencontrer un problème ? | Effectivement ça génère une erreur : "pygame.error: video system not initialized" | Ouais... De toute façon, cette erreur serait survenue aussi si on avait utilisé pygame.display.flip()... Donc... Il faut juste appeler les méthodes dans le bon ordre. 

class Niveau : #Après pourra-t-on faire : Niveau().generation().affichage() pour afficher un niveau...? | NON !
    
    """ classe Niveau :
        — Attr : name, structure_txt, structure_list, sprites ?
        — Meth : structure_txt_to_struct_list(generate), version_graphique
        
        """
    def __init__(self) :
        self.name = "placeholder" #A modifier
        self.textver = open("level_1.txt", 'r') #Deux possibilités. (1) Soit j'ouvre le fichier ici, (2) soit je charge un "context manager" plus tard et je mets donc juste le chemin vers le fichier ici. | Choix 2 pour le moment, parait plus "secure". | Finit par faire le (1), parce que cela rendait l'écriture de listver plus facile
        #self.sprite_mur = pygame.image.load("mur.png")# Attention : .convert() pas possible sans initialisation préalable. Et bien sûr, si on le lance avant le générer un display...

    @property
    def listver (self) : 
        return self.textver.readlines() #Whoa ! J'ai trouvé ça en fouillant dans la doc, me demandant entre autres ce qu'est IO.TextIOWrapper ! Même plus besoin de créer une liste, d'iterer sur le fichier, et de stocker chaque ligne de ce fichier dans une autre liste puis de stocker cette autre liste dans la première... | Là on a directement une liste où chaque membre est un str qui contient une ligne du fichier. Ext : ['wwwwwwwGwwwwwww\n', 'wwwwwww0wwwwwww\n',
    
    def afficher(self) : #peut-être un argument supplémentaire, listver...
        sprite_mur = pygame.image.load("mur.png").convert() #Déplacé ici car convert dans un __init__ génère une erreur. Et puis c'est mieux de l'appeler uniquement quand on en a besoin...

        for y, a in enumerate(self.listver) : # 1 var et c'est le tuple qui sort. 2 et ce sont ses membres | #(0, 'wwwwwwwGwwwwwww\n'), (1, 'wwwwwww0wwwwwww\n'),...
            for x,b in enumerate(a) : 
                if b == 'w' : 
                    FenetreC.FENETRE.blit(sprite_mur, [x*FenetreC.CELL_SIZE, y*FenetreC.CELL_SIZE]) #fenetre ou pygame.display.set_mode(self.resolution). Je me demande si utiliser fenetre.generation().blit() dessus ne va pas poser des problèmes.... | EFFECTIVEMENT. AttributeError : 'NoneType' object has no attribute 'blit'.
        
    """Une fois de plus, qu'est-ce qu'on doit faire...? 
        Iterer sur chaque membre de la liste du niveau.
            Iterer sur chaque caractère de chaque str
                Si on tombe sur un 'w' : afficher le sprite d'un mur à un certain endroit de l'écran, cet endroit dépendant de l'index de l'élément.
                Si on tombe sur un '0', un 'S' ou un 'G' ou '\n' : ne rien faire """

def test() : 
    pass 
    #Fenetre.generation()
    #print(niveau.listver)
    #niveau.afficher()

def main() : 
    
    niveau_1 = Niveau()
    niveau_1.afficher() #Quand je le mets dans la boucle, ça refait la construction à chaque tour... Au niveau où on en est, pas encore nécessaire, mais ça risque de poser des problèmes à l'avenir.

    while 0<1 :

        pygame.time.Clock().tick(30)

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT or evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE : 
                print("Giscard : \"...Au revoir.\"")
                pygame.quit()
                sys.exit()

        FenetreC.rafraichissement()

if __name__ == "__main__" : 
    #test()
    main()