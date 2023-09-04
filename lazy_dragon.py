import time
import pygame
import sys
import keyboard
#from pygame.locals import *
pygame.init()
gravity = 0.1
dragon_y_movement = 0

def floor_moving():
    
    screen.blit(floor_surface,(floor_x_position,450))
    screen.blit(floor_surface,(floor_x_position+288,450))
    

    

                          
def bg_moving():
    screen.blit(bg_surface,(bg_x_moving,0))
    screen.blit(bg_surface,(bg_x_moving+288,0))
    
def pause():
    screen.blit(bg_surface,(0,0))
    screen.blit(floor_surface(0,450))
    
    
    
    
    #screen.blit(floor_surface,(floor_x_position,450))


screen = pygame.display.set_mode((288,512))#,RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("         Lazy_dragon")
bg_surface = pygame.image.load("C:/Users/hp/Pictures/kali linux/python application demo/pink_bg.png") 
floor_surface = pygame.image.load("C:/Users/hp/Pictures/kali linux/python application demo/flappy_base_sizze.png")
nidhish = pygame.image.load("C:/Users/hp/Pictures/kali linux/python application demo/nidhish_1_size-removebg-preview.png") 
floor_x_position = 0
floor_nidhish = 0
bg_x_moving = 0
dragon_image = pygame.image.load("C:/Users/hp/Pictures/kali linux/python application demo/dragon_fliped_removed_resized.png")
gam_over_y=512   

#dragon_rect = dragon_image.get_rect(center=(78,269))
dragon_rect = dragon_image.get_rect(center=(78,259))
game_over = pygame.image.load("C:/Users/hp/Pictures/kali linux/python application demo/game_over_full.png")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                dragon_y_movement=gravity-5
            elif event.type==pygame.K_a:
                pause()
            
        
        
            
        

    
    bg_x_moving-=1                        
    bg_moving()
    if bg_x_moving<=-288:
        bg_x_moving=0
    floor_nidhish-=1
    screen.blit(nidhish,(floor_nidhish,100))
    #time.sleep(2)
    
    floor_x_position-=1
    floor_moving()
    if floor_x_position<=-288:
        floor_x_position=0
    
        
    dragon_y_movement = dragon_y_movement+gravity  
    dragon_rect.centery = dragon_rect.centery+dragon_y_movement
    screen.blit(dragon_image,dragon_rect)
    if dragon_rect.centery>=518:
        gam_over_y-=1
        screen.blit(game_over,(120,gam_over_y))
        if gam_over_y==400:
            pygame.quit()
            sys.exit()
    if dragon_rect.centery<=0:
        dragon_y_movement = gravity+1
        
    
   
    
    
    
    pygame.display.update()
    clock.tick(190)
    
    

    
