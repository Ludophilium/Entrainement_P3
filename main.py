
import sys
import pygame
import random 

from classes import *

pygame.init()  

def main():
    """Main part of the program. Every instances are initialized here. This is also where player inputs and game and display behavior is managed."""

    level_1 = Level("level_1.txt")
    guard = Character("sprites/aku.png", [14,14], 'left') 
    hero = Player("sprites/manL.png", "sprites/manR.png", "sprites/manU.png", "sprites/manD.png", [0,0], "right", level_1)
    
    Item.get_positions(3,level_1.listver)

    item1 = Item(1, "sprites/eth.png")
    item2 = Item(2, "sprites/tub.png")
    item3 = Item(3, "sprites/aig.png")

    level_1.display(guard)

    pygame.key.set_repeat(100, 25)

    while hero.ko == False:

        pygame.time.Clock().tick(30)
        
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT or evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE: 
                pygame.quit()
                sys.exit()

            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_DOWN: 
                hero.move("down")

            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_RIGHT: 
                hero.move("right")            
            
            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_UP: 
                hero.move("up")

            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_LEFT: 
                hero.move("left")

        level_1.display(guard) 
        guard.orient()
        guard.display() 

        hero.gather(item1, item2, item3)
        hero.sleep(guard)
        
        item1.display()
        item2.display()
        item3.display()

        hero.display()

        Window.refresh()

    main() 

if __name__ == "__main__": 
    main()