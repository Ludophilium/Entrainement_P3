
import sys
import pygame
import random 
import time

pygame.init()  

class Fenetre :  
    
    TITRE = "Project (Mc)GYVR"  
    COTE_SPRITE = 30 
    RESOLUTION = [15*COTE_SPRITE,15*COTE_SPRITE] 
    ICONE_PTH = pygame.image.load("mur.png") 

    FENETRE = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE) 
    TITLE_FEN = pygame.display.set_caption(TITRE)
    ICONE_FEN = pygame.display.set_icon(ICONE_PTH.convert_alpha())

    @classmethod    
    def rafraichissement(cls) : 
        pygame.display.flip() 

class Niveau : 
    
    def __init__(self, textver_pth) :
        self.textver_pth = textver_pth
        self.fond = pygame.image.load("fond.jpg")
        self.sprite_mur = pygame.image.load("mur.png") 
    
    @property
    def listver (self) : 
        with open(self.textver_pth) as f : 
            l = list()
            for x in f.readlines() : 
                l += [list(x.strip('\n'))] 
            return l
    
    def afficher(self) : 
        fond_pf = self.fond.convert()
        sprite_mur_pf = self.sprite_mur.convert() 

        Fenetre.FENETRE.blit(fond_pf, [0,0]) 

        for y, a in enumerate(self.listver) : 
            for x,b in enumerate(a) : 
                if b == 'w' : 
                    Fenetre.FENETRE.blit(sprite_mur_pf, [x*Fenetre.COTE_SPRITE, y*Fenetre.COTE_SPRITE]) 

class Personnage : 
  
    def __init__(self, sprite_pth, position) :
        self.sprite = pygame.image.load(sprite_pth)
        self.position = position 
        self.ko = False
        
    @property
    def position_pf(self) : 
        return list(x*Fenetre.COTE_SPRITE for x in self.position)
      
    @property
    def X (self) : 
        return self.position[0] 

    @property
    def Y (self) : 
        return self.position[1] 

    def afficher (self) : 
        sprite_pf = self.sprite.convert_alpha() 
        if self.ko == False :
            Fenetre.FENETRE.blit(sprite_pf, self.position_pf)       

class Joueur (Personnage) : 
    def __init__(self, sprite_pth, position, niveau) : 
        super().__init__(sprite_pth, position) 
        self.objets = list()
        self.nl = niveau.listver 

    def deplacer(self, direction) : 

        if direction == 'droite' and self.X+1<len(self.nl[0]) and self.nl[self.Y][self.X+1] != 'w' : 
            self.position[0] += 1 

        if direction == 'bas' and self.Y+1 < len(self.nl) and self.nl[self.Y+1][self.X] != 'w' : 
            self.position[1] += 1 
          
        if direction == 'haut' and self.Y-1 >= 0 and self.nl[self.Y-1][self.X] != 'w' : 
            self.position[1] -= 1

        if direction == 'gauche' and self.X-1 >=0 and self.nl[self.Y][self.X-1] != 'w' : 
            self.position[0] -= 1

    def ramasser_objet(self, *items) : 
        
        if self.position in Item.POSITIONS_VAL :
            for item in items :
                if self.position == item.position and item.recupere == False :
                    self.objets += [item.rang]
                    item.recupere = True
                    print(self.objets)

    def endormir (self, garde) : 
        if self.position == garde.position :
            if sorted(self.objets) == [1,2,3] :
                garde.ko = True
                print("Geniaaal ! Tu as gagné ! Merci d'avoir joué")
                #pygame.time.wait(3*1000)
                pygame.quit()
                sys.exit()
            else : 
                self.ko = True
                for x in range(15) :
                    print("What... What have you done...")
                #pygame.time.wait(1*1000)
                #time.sleep(1)

class Item : 

    POSITIONS_VAL = list() 
    
    def __init__(self, rang_item, sprite_pth) :
        self.rang = rang_item
        self.position = self.POSITIONS_VAL[rang_item-1]
        self.recupere = False
        self.sprite = pygame.image.load(sprite_pth)
    
    @classmethod
    def positionner(cls, nombre_item, niveau_listver) :
        positions_pos = list()

        for y, a in enumerate(niveau_listver) : 
            for x, b in enumerate(a) :
                if b == '0' : 
                    positions_pos += [[x,y]]
        
        while len(cls.POSITIONS_VAL) < nombre_item : 
            a = random.choice(positions_pos)
            if a not in cls.POSITIONS_VAL : 
                cls.POSITIONS_VAL += [a] 

    @property
    def position_pf(self) : 
        return list(x*Fenetre.COTE_SPRITE for x in self.position)
    
    def afficher(self) :
        sprite_pf = self.sprite.convert_alpha() 
        if not self.recupere : 
            Fenetre.FENETRE.blit(sprite_pf, self.position_pf)

def main() :

    niveau_1 = Niveau("level_1.txt")
    garde = Personnage("kd.png",[7,14]) 
    heros = Joueur("dk.png",[7,0], niveau_1)
    
    Item.positionner(3,niveau_1.listver)

    item1 = Item(1, "item.png")
    item2 = Item(2, "item.png")
    item3 = Item(3, "item.png")

    niveau_1.afficher() 

    while heros.ko == False :

        pygame.time.Clock().tick(30)

        for evt in pygame.event.get():
            if evt.type == pygame.QUIT or evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE : 
                pygame.quit()
                sys.exit()

            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_DOWN : 
                heros.deplacer("bas")
               
            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_RIGHT : 
                heros.deplacer("droite")
            
            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_UP : 
                heros.deplacer("haut")

            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_LEFT : 
                heros.deplacer("gauche")

        niveau_1.afficher() 
        garde.afficher() 

        heros.ramasser_objet(item1, item2, item3)
        heros.endormir(garde)
        
        item1.afficher()
        item2.afficher()
        item3.afficher()

        heros.afficher()

        Fenetre.rafraichissement()

    main() 

if __name__ == "__main__" : 
    main()