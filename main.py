import pygame
import  sys

pygame.init()


display_widht =800
display_height =600

display =pygame.display.set_mode((display_widht,display_height))
pygame.display.set_caption("Run Dino RUUUUN!!!")

icon =pygame.image.load('Runner.png')
pygame.display.set_icon(icon)

user_widht = 60
user_height = 100
user_x = display_widht//3
#user_y =

def run_game():
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.fill((255,255,255))
        pygame.display.update()

run_game()

