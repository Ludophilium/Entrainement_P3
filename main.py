"""Maintenant qu'on a créé main(), les classes fenetre et niveau, et réussi à faire communiquer ces classes ensemble et en conséquence à afficher le labyrinthe... 

Il faut désormais implémenter McGuyver, le garde et faire en sorte que MC Guyver gagne quand il "touche" le gardien"""

import sys
import pygame

#pygame.init() #Pas très "propre" mais au moins ça contre les problèmes que sa non-initialisation pourrait causer. 
#import pygame.locals est aussi importable ou plutôt sa forme "from pygame.locals import *" histoire que je puisse utiliser ses constantes et méthodes sans devoir mettre pygame. devant. Si on refuse ceci on ferait mieux de juste importer pygame.

class Fenetre : #Une approche FONCTIONNELLE de construction de la Classe Fenetre | Attention, ce code est lu qu'on appelle Fenetre ou pas ! Autant ce n'est pas grave vu que c'est un composant essentiel, autant si on veut la lire sur commande... 
    
    TITRE = "Project (Mc)GYVR"  
    SQUARE_SIZE = 30 #30 parce que le sprite de travail fait 30x30 et qu'une cellule fera sans doute 30x30.
    RESOLUTION = [15*SQUARE_SIZE,15*SQUARE_SIZE] #15 parce que la fenetre doit contenir 15 sprites sur la longueur comme sur la largeur.
    ICONE_PTH = pygame.image.load("mur.png") #Suffit d'ajouter .convert_alpha et un problème surgit

    FENETRE = pygame.display.set_mode(RESOLUTION) #Et si on veut que l'utilisateur veut que la fenetre soit RESIZABLE (pygame.RESIZABLE) ?
    TITLE_FEN = pygame.display.set_caption(TITRE)
    ICONE_FEN = pygame.display.set_icon(ICONE_PTH.convert_alpha())

    @classmethod    
    def rafraichissement(cls) : 
        pygame.display.flip() 

class Niveau : #Après pourra-t-on faire : Niveau().generation().affichage() pour afficher un niveau...? | NON !
    
    def __init__(self) :
        self.name = "placeholder" #A modifier
        self.textver = open("level_1.txt", 'r') #Deux possibilités. (1) Soit j'ouvre le fichier ici, (2) soit je charge un "context manager" plus tard et je mets donc juste le chemin vers le fichier ici. | Choix 2 pour le moment, parait plus "secure". | Finit par faire le (1), parce que cela rendait l'écriture de listver plus facile
        self.sprite_mur = pygame.image.load("mur.png")# Attention : .convert() pas possible sans initialisation préalable. Et bien sûr, si on le lance avant le générer un display...

    @property
    def listver (self) : 
        return self.textver.readlines() #Whoa ! J'ai trouvé ça en fouillant dans la doc, me demandant entre autres ce qu'est IO.TextIOWrapper ! Même plus besoin de créer une liste, d'iterer sur le fichier, et de stocker chaque ligne de ce fichier dans une autre liste puis de stocker cette autre liste dans la première... | Là on a directement une liste ['wwwwwwwGwwwwwww\n', 'wwwwwww0wwwwwww\n',...] où chaque membre est un str qui contient une ligne du fichier. 
    
    def afficher(self) : #peut-être un argument supplémentaire, listver...
        sprite_mur_pf = self.sprite_mur.convert() #Déplacé ici car convert dans un __init__ génère une erreur. Et puis c'est mieux de l'appeler uniquement quand on en a besoin...
        #print("sprite_mur est de type {pika}".format(pika = type(sprite_mur)))

        for y, a in enumerate(self.listver) : # 1 var et c'est le tuple (x,y) en entier qui sort. 2 et ce sont ses membres x et y individuellement | enumerate(self.listver) = (0, 'wwwwwwwGwwwwwww\n'), (1, 'wwwwwww0wwwwwww\n'),...
            for x,b in enumerate(a) : #enumerate(a) = (0, 'w'), (1, 'w'),...
                if b == 'w' : 
                    Fenetre.FENETRE.blit(sprite_mur_pf, [x*Fenetre.SQUARE_SIZE, y*Fenetre.SQUARE_SIZE]) 

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
        self.position = position #Quelles sont elles d'ailleurs ? C'est sur des 15 cases donc en [30*(numero_case_x),30*(numero_case_y)]
        self.ko = False
        
    def afficher (self) : #Tiens, j'ai oublié ça. Et comme c'est commun aux deux classes il faut le mettre ici... | sprite_pth = "goomba.png" ou "dk.png"
        sprite_pf = self.sprite.convert() #Autre manière de régler le problème posé par le fait de mettre .convert() à self.sprite
        Fenetre.FENETRE.blit(sprite_pf, self.position)
        #print(type(sprite_perso))

class Joueur (Personnage) : #Avoir sa propre classe, si ÇA c'est pas la classe 😎
    def __init__(self, sprite_pth, position) : #Alors, vais-je avoir besoin de __super__().__init__() ou je pourrais accéder aux attributs de la classe mère sans... | Réponse : J'ai overridé le constructeur originel, donc faut bien ce super() avant (et pas __super__())
        super().__init__(sprite_pth, position) #Si on ne met pas les variables sur deux __init__, ça ne marche pas... Peut-être une manière de montrer explicitement d'où ces deux arguments sortent...
        self.objets = list()

    """La prochaine fois, implémentez ces méthodes exclusives : se déplacer, ramasser objet, endormir garde"""

    def deplacer(self, direction) :
        pass

        
        if direction == 'droite' and 1 : #ET que case suivante n'est pas un mur ET  qu'on est pas hors terrain
            pass


    
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
    
    case = Fenetre.SQUARE_SIZE #A mettre dans un document à part. 

    niveau_1 = Niveau()
    garde = Personnage("kd.png",(7*case,14*case)) 
    heros = Joueur("dk.png",(7*case,0*case))
    
    niveau_1.afficher() #Quand je le mets dans la boucle, ça refait la construction à chaque tour... Au niveau où on en est, pas encore nécessaire, mais ça risque de poser des problèmes à l'avenir.

    """Test sur les objets Rect : """

    heros_rect = heros.sprite.get_rect(x=heros.position[0], y=heros.position[1])
    mur_rect = niveau_1.sprite_mur.get_rect()

    print(heros_rect.center) #Première surface
    print(mur_rect.center) #Deuxième
    
    a = mur_rect.contains(heros_rect) #SurfaceA = Containing. SurfaceB = Contained. Surface A est donc le sprite_mur et B le personnage. Mais honnêtement pour ce qu'on veut faire... C'est interchangeable. | Resultat ? Ça MARCHE sans problème et dans les deux sens. La méthode renvoie 0 si faux et 1 si True. | Faudra utiliser la fonction bool() si necessaire | Bon on va ajouter un attribut ou une propriété pour générer des versions Rect des Surface toujours à la bonne place.

    b = heros_rect.contains(mur_rect) 

    print("This is the a result : {}".format(a))
    print("This is the b result : {}".format(b))

    pygame.draw.rect(garde.sprite, pygame.Color(255, 0, 0, 255), garde.sprite.get_rect(),1)

    while not 0 :

        pygame.time.Clock().tick(30)

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT or evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE : 
                print("Giscard : \"...Au revoir.\"")
                pygame.quit()
                sys.exit()
        heros.afficher() 
        garde.afficher()

        Fenetre.rafraichissement()

        
if __name__ == "__main__" : 
    #test()
    main()