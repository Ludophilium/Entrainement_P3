"""Maintenant qu'on a créé main(), les classes fenetre et niveau, et réussi à faire communiquer ces classes ensemble et en conséquence à afficher le labyrinthe... 

Il faut désormais implémenter McGuyver, le garde et faire en sorte que MC Guyver gagne quand il "touche" le gardien"""

import sys
import pygame

#pygame.init() #Pas très "propre" mais au moins ça contre les problèmes que sa non-initialisation pourrait causer. 
#import pygame.locals est aussi importable ou plutôt sa forme "from pygame.locals import *" histoire que je puisse utiliser ses constantes et méthodes sans devoir mettre pygame. devant. Si on refuse ceci on ferait mieux de juste importer pygame.

class Fenetre : #Une approche FONCTIONNELLE de construction de la Classe Fenetre | Attention, ce code est lu qu'on appelle Fenetre ou pas ! Autant ce n'est pas grave vu que c'est un composant essentiel, autant si on veut la lire sur commande... 
    
    TITRE = "Project (Mc)GYVR"  
    COTE_SPRITE = 30 #30 parce que le sprite de travail fait 30x30 et qu'une cellule fera sans doute 30x30.
    RESOLUTION = [15*COTE_SPRITE,15*COTE_SPRITE] #15 parce que la fenetre doit contenir 15 sprites sur la longueur comme sur la largeur.
    ICONE_PTH = pygame.image.load("mur.png") #Suffit d'ajouter .convert_alpha et un problème surgit

    FENETRE = pygame.display.set_mode(RESOLUTION) #Et si on veut que l'utilisateur veut que la fenetre soit RESIZABLE (pygame.RESIZABLE) ?
    TITLE_FEN = pygame.display.set_caption(TITRE)
    ICONE_FEN = pygame.display.set_icon(ICONE_PTH.convert_alpha())

    @classmethod    
    def rafraichissement(cls) : 
        pygame.display.flip() 

class Niveau : #Après pourra-t-on faire : Niveau().generation().affichage() pour afficher un niveau...? | NON !
    
    def __init__(self, textver_pth) :
        self.name = "placeholder" #A modifier
        self.textver_pth = textver_pth
        self.fond = pygame.image.load("fond.jpg")
        self.sprite_mur = pygame.image.load("mur.png") 

    @property
    def listver (self) : 
        with open(self.textver_pth) as f : 
            return f.readlines() #['wwwwwwwGwwwwwww\n', 'wwwwwww0wwwwwww\n',...] où chaque membre est un str qui contient une ligne du fichier. 
    
    def afficher(self) : #peut-être un argument supplémentaire, listver...
        fond_pf = self.fond.convert()
        sprite_mur_pf = self.sprite_mur.convert() 
        #print("sprite_mur est de type {pika}".format(pika = type(sprite_mur)))

        Fenetre.FENETRE.blit(fond_pf, [0,0]) #Zero by default ?

        for y, a in enumerate(self.listver) : #enumerate(self.listver) = (0, 'wwwwwwwGwwwwwww\n'), (1, 'wwwwwww0wwwwwww\n'),...
            for x,b in enumerate(a) : #enumerate(a) = (0, 'w'), (1, 'w'),...
                if b == 'w' : 
                    Fenetre.FENETRE.blit(sprite_mur_pf, [x*Fenetre.COTE_SPRITE, y*Fenetre.COTE_SPRITE]) 

class Personnage : #Comment créer McGuyver et le garde ?
    """Classe mère, ne contient que les éléments communs à GYVR et le garde, majoritairement des attributs... 
    
    — Inst : McGuyver, le Garde. | 

            — Attr : 
                GYVR : objets_ramassés
                GURD : 
                PARTAGÉS * : position_sur_terrain, nom, conscient (donc un booléen | ou nombre d'essais, important pour la victoire ou la défaite), sprite. 

            — Meth (interactions) : 
            
                GYVR : endormir_garde (repose sur la possession des obj, réussi s'ils sont là, backfire si ce n'est pas le cas), se_déplacer, ramasser_objet,
                GURD : 
                PARTAGÉS * : affichser* """

    def __init__(self, sprite_pth, position) :
        self.sprite = pygame.image.load(sprite_pth)
        self.position = position #C'est la position avec comme unité de base le côté d'un sprite 30*30px, sous la position sous la forme (X,Y) donc
        self.ko = False
        
    @property
    def position_pf(self) : 
        return list(x*Fenetre.COTE_SPRITE for x in self.position)
        #conversion des coordonnées sous la forme (x,y) pour faciliter les opérations avec pygame. Sous cette forme, chaque unité vaut un pixel (ou presque). 

    @property
    def X (self) : #Extraire X pour l'utiliser en tant qu'index ?
        return self.position[0] 

    @property
    def Y (self) : #Extraire Y pour l'utiliser en tant qu'index ?
        return self.position[1] 

    def afficher (self) : #Tiens, j'ai oublié ça. Et comme c'est commun aux deux classes il faut le mettre ici... | sprite_pth = "goomba.png" ou "dk.png"
        sprite_pf = self.sprite.convert_alpha() #Autre manière de régler le problème posé par le fait de mettre .convert() à self.sprite. .convert_alpha pour éviter de se retrouver avec un fond noir sous le sprite personnage.
        Fenetre.FENETRE.blit(sprite_pf, self.position_pf)
        #print(type(sprite_perso))

class Item : 
    """Bon, maintenant on travaille sur la classe qui contient les objets. Mais que devons nous faire ?"""

class Joueur (Personnage) : #Avoir sa propre classe, si ÇA c'est pas la classe 😎
    def __init__(self, sprite_pth, position, niveau) : #Alors, vais-je avoir besoin de __super__().__init__() ou je pourrais accéder aux attributs de la classe mère sans... | Réponse : J'ai overridé le constructeur originel, donc faut bien ce super() avant (et pas __super__())
        super().__init__(sprite_pth, position) #Si on ne met pas les variables sur deux __init__, ça ne marche pas... Peut-être une manière de montrer explicitement d'où ces deux arguments sortent...
        self.objets = list()
        self.nl = niveau.listver #Une manière de contourner le problème posé par l'impossibilité d'appeler directement niveau_1.listver() dans la fonction deplacer

    """La prochaine fois, implémentez ces méthodes exclusives : se déplacer, ramasser objet, endormir garde"""

    def deplacer(self, direction) : #On ne gère ici ni l'appui, ni l'affichage. Tout ce qu'on change c'est la position en fait. | On reprend l'implémentation des contraintes mur après — ' or

        if direction == 'droite' and self.X+1<len(self.nl[0])-1 and self.nl[self.Y][self.X+1] != 'w' : 
            self.position[0] += 1 #Ex : (7,0) > (8,0)
            print("valeur de len(self.nl[0])-1 : {}".format(len(self.nl[0])-1))

        if direction == 'bas' and self.Y+1 < len(self.nl) and self.nl[self.Y+1][self.X] != 'w' : 
            self.position[1] += 1 #Ex : [7,0] > [7,1].
            print("valeur de len(self.nl) : {}".format(len(self.nl))) 

        if direction == 'haut' and self.Y-1 >= 0 and self.nl[self.Y-1][self.X] != 'w' : 
            self.position[1] -= 1

        if direction == 'gauche' and self.X-1 >=0 and self.nl[self.Y][self.X-1] != 'w' : 
            self.position[0] -= 1
  
    def ramasser_objet(self) :
        pass

    def endormir_garde(self) : 
        pass
    

def test() : 
    pass 
    #Fenetre.generation()
    #print(niveau.listver)
    #niveau.afficher()

def main() :

    niveau_1 = Niveau("level_1.txt")
    garde = Personnage("kd.png",[7,14]) #Pas de tuples ! La position ne peut pas changer !!
    heros = Joueur("dk.png",[7,0], niveau_1)
    
    print(niveau_1.listver)

    niveau_1.afficher() #Quand je le mets dans la boucle, ça refait la construction à chaque tour... Au niveau où on en est, pas encore nécessaire, mais ça risque de poser des problèmes à l'avenir.

    while not 0 :

        pygame.time.Clock().tick(30)

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT or evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE : 
                print("Giscard : \"...Au revoir.\"")
                pygame.quit()
                sys.exit()

            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_DOWN : 
                heros.deplacer("bas")
                print(heros.X, heros.Y)
                print(heros.position_pf)

            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_RIGHT : 
                heros.deplacer("droite")
                print(heros.X, heros.Y)
                print(heros.position_pf)
            
            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_UP : 
                heros.deplacer("haut")
                print(heros.X, heros.Y)
                print(heros.position_pf)

            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_LEFT : 
                heros.deplacer("gauche")
                print(heros.X, heros.Y)
                print(heros.position_pf)

        niveau_1.afficher() #Pour éviter que le perso se dédouble... Mais il n'y a pas de fond dans mon cas, donc ça ne marche pas encore. 
        garde.afficher() #Si garde dernier à être affiché, lui cacher avatar joueur.
        heros.afficher() 

        Fenetre.rafraichissement()

if __name__ == "__main__" : 
    #test()
    main()