import pygame
import sys

class Jeu:
        def __init__(self):       
            self.ecran = pygame.display.set_mode((1920, 1080))
            pygame.display.set_caption('Ping/Pong')
            self.jeu_encours = True
        def boucle_principale(self):
            while self.jeu_encours:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                self.ecran.fill((0,0,0,))   
                pygame.display.flip()

if  __name__ == '__main__':
    pygame.init()
    Jeu().boucle_principale()
    pygame.quit()
    