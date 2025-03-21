import pygame
import sys
from joueur import Joueur

class Jeu:
        
        def __init__(self):       
            self.ecran = pygame.display.set_mode((1920, 1080))
            pygame.display.set_caption('Ping/Pong')
            self.jeu_encours = True
            self.rect = pygame.Rect(0, 0, 1920, 1080)
            self.joueur_1_x, self.joueur_1_y = 20, 450
            self.joueur_2_x, self.joueur_2_y = 1880, 450
            self.joueur_taille = [20,130]
            self.vitesse_y_1, self.vitesse_y_2 = 0,0
            self.joueur_1 = Joueur(self.joueur_1_x, self.joueur_1_y, self.joueur_taille)
            self.joueur_2 = Joueur(self.joueur_2_x, self.joueur_2_y, self.joueur_taille)

        def boucle_principale(self):
            while self.jeu_encours:
                for event in pygame.event.get():
                    
                    if event.type == pygame.QUIT:
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.vitesse_y_2 = -2  
                        if event.key == pygame.K_DOWN:
                            self.vitesse_y_2 = 2   
                        if event.key == pygame.K_z:
                            self.vitesse_y_1 = -2  
                        if event.key == pygame.K_s:
                            self.vitesse_y_1 = 2   

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                            self.vitesse_y_2 = 0  
                        if event.key == pygame.K_DOWN:
                            self.vitesse_y_2 = 0   
                        if event.key == pygame.K_z:
                            self.vitesse_y_1 = 0  
                        if event.key == pygame.K_s:
                            self.vitesse_y_1 = 0  
                        
                self.joueur_1.mouvement(self.vitesse_y_1)
                self.joueur_2.mouvement(self.vitesse_y_2)
                self.joueur_1.rect.clamp_ip(self.rect)
                self.joueur_2.rect.clamp_ip(self.rect)

                self.ecran.fill((0,0,0,))
                self.joueur_1.afficher(self.ecran)
                self.joueur_2.afficher(self.ecran)    
                pygame.display.flip()

if  __name__ == '__main__':
    pygame.init()
    Jeu().boucle_principale()
    pygame.quit()
    