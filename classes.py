import sys
import pygame
import random 

pygame.init()  

class Window:  
    """Window class contains the basic elements to launch a pygame window and refresh it"""

    TITLE = "(MC)GYVR 2600 - (C) 1985 PLACEHOLDER INC"  
    SPRITE_SIZE = 30 
    RESOLUTION = [15*SPRITE_SIZE,15*SPRITE_SIZE] 
    ICON_PTH = pygame.image.load("sprites/mur.png") 

    WINDOW = pygame.display.set_mode(RESOLUTION) 
    WIN_TITLE = pygame.display.set_caption(TITLE)
    WIN_ICON = pygame.display.set_icon(ICON_PTH.convert_alpha())

    @classmethod    
    def refresh(cls): 
        pygame.display.flip() 


class Level: 
    """Level class manages level creation on logical and graphical level"""
    
    def __init__(self, textver_pth):
        self.textver_pth = textver_pth
        self.backgr = pygame.image.load("sprites/fond_n.png")
        self.wall_spr = pygame.image.load("sprites/mur2.png")
        self.ligh_sprite = pygame.image.load("sprites/lig.png")
    
    @property
    def listver (self): 
        with open(self.textver_pth) as f: 
            l = list()
            for x in f.readlines(): 
                l += [list(x.strip('\n'))] 
            return l
    
    def display(self, guard): 
        backgr_pf = self.backgr.convert()
        wall_spr_pf = self.wall_spr.convert()
        ligh_sprite_pf = self.ligh_sprite.convert_alpha()

        Window.WINDOW.blit(backgr_pf, [0,0]) 

        for y, a in enumerate(self.listver): 
            for x,b in enumerate(a): 
                if b == 'W': 
                    Window.WINDOW.blit(wall_spr_pf, [x*Window.SPRITE_SIZE, y*Window.SPRITE_SIZE])
                if b == 'U' and guard.orientation == 'up': 
                    Window.WINDOW.blit(ligh_sprite_pf, [x*Window.SPRITE_SIZE, y*Window.SPRITE_SIZE])
                if b == 'L' and guard.orientation == 'left':
                    Window.WINDOW.blit(ligh_sprite_pf, [x*Window.SPRITE_SIZE, y*Window.SPRITE_SIZE])


class Character: 
    """Character class manages character sprites, positioning, orientation and display"""
    
    def __init__(self, sprite_pth, position, orientation):
        self.position = position 
        self.sprite = pygame.image.load(sprite_pth)
        self.ko = False
        self.orientation = orientation
        self.count = 0
              
    @property
    def position_pf(self): 
        return list(x*Window.SPRITE_SIZE for x in self.position)
      
    @property
    def X (self): 
        return self.position[0] 

    @property
    def Y (self): 
        return self.position[1] 

    def orient (self):
        self.count += 1

        if self.count % 30 == 0: 
            if self.orientation == 'left': 
                self.sprite = pygame.transform.rotate (self.sprite, -90)
                self.orientation = "up" 
            elif self.orientation == 'up':
                self.sprite = pygame.transform.rotate(self.sprite, 90)
                self.orientation = "left" 

    def display (self): 
        sprite_pf = self.sprite.convert_alpha() 
        if self.ko == False:
            Window.WINDOW.blit(sprite_pf, self.position_pf)       


class Player (Character): 
    """Player class is a subclass of Character. It especially manages player movement, items collection, and ability to send a guard off to sleep"""
    
    def __init__(self, spriteG_pth, spriteD_pth, spriteH_pth, spriteB_pth, position, orientation, level): 
        super().__init__(spriteD_pth, position, orientation) 
        self.items = list()
        self.nl = level.listver
        self.sprite_pth_dict = dict(left = spriteG_pth, right = spriteD_pth, up = spriteH_pth, down = spriteB_pth) 
    
    def move(self, direction): 
        self.sprite = pygame.image.load(self.sprite_pth_dict[direction])
        self.orientation = direction

        if direction == 'right':
            if self.X+1<len(self.nl[0]) and self.nl[self.Y][self.X+1] != 'W': 
                self.position[0] += 1

            elif self.X+1 == len(self.nl[0]) and self.nl[self.Y][self.X-14] != 'W': 
                self.position[0] = 0

        if direction == 'down':
            if self.Y+1 < len(self.nl) and self.nl[self.Y+1][self.X] != 'W': 
                self.position[1] += 1
            
            elif self.Y+1 == len(self.nl) and self.nl[self.Y-14][self.X] != 'W': 
                self.position[1] = 0 
          
        if direction == 'up':
            if self.Y-1 >= 0 and self.nl[self.Y-1][self.X] != 'W': 
                self.position[1] -= 1

            elif self.Y-1 < 0 and self.nl[self.Y+14][self.X] != 'W': 
                self.position[1] = 14

        if direction == 'left': 
            if self.X-1 >=0 and self.nl[self.Y][self.X-1] != 'W': 
                self.position[0] -= 1
            
            elif self.X-1 <0 and self.nl[self.Y][self.X+14] != 'W':
                self.position[0] = 14

    def gather(self, *items): 
        if self.position in Item.VAL_POSITIONS:
            for item in items:
                if self.position == item.position and item.get == False:
                    self.items += [item.rank]
                    item.get = True
                    print(self.items)

    def sleep (self, guard): 
        monitored = dict(left = [guard.position,[13,14], [12,14], [11,14], [10,14], [9,14]], up = [guard.position, [14,13], [14,12], [14,11], [14,10], [14,9]])

        if self.position in monitored[guard.orientation]:

            if sorted(self.items) == [1,2,3] and self.position == guard.position:
               
                if self.orientation == 'right' and guard.orientation == 'up' or self.orientation == 'down' and guard.orientation == 'left':
                    guard.ko = True
                    print("Awesome! You won! Thanks for playing!")
                    pygame.quit()
                    sys.exit()
                
                else:
                    self.ko = True
                    for x in range(15):
                        print("What... What have you done...")
                               
            else: 
                self.ko = True
                for x in range(15):
                    print("What... What have you done...")


class Item: 
    """Item class manages item positioning and display"""

    VAL_POSITIONS = list() 
    
    def __init__(self, rank_item, sprite_pth):
        self.rank = rank_item
        self.position = self.VAL_POSITIONS[rank_item-1]
        self.get = False
        self.sprite = pygame.image.load(sprite_pth)
    
    @classmethod
    def get_positions(cls, nombre_item, level_listver):
        pos_positions = list()

        for y, a in enumerate(level_listver): 
            for x, b in enumerate(a):
                if b == '0': 
                    pos_positions += [[x,y]]
        
        while len(cls.VAL_POSITIONS) < nombre_item: 
            a = random.choice(pos_positions)
            if a not in cls.VAL_POSITIONS: 
                cls.VAL_POSITIONS += [a] 

    @property
    def position_pf(self): 
        return list(x*Window.SPRITE_SIZE for x in self.position)
    
    def display(self):
        sprite_pf = self.sprite.convert_alpha() 
        if not self.get: 
            Window.WINDOW.blit(sprite_pf, self.position_pf)
