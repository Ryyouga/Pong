import pygame
import sys
import random
import math
from balle import Balle
from joueur import Joueur

class Jeu:
        
        def __init__(self):       
            self.ecran = pygame.display.set_mode((1920, 1080))
            pygame.display.set_caption('Ping/Pong')
            self.clock = pygame.time.Clock()
            self.jeu_encours = True
            self.rect = pygame.Rect(0, 0, 1920, 1080)
            self.joueur_1_x, self.joueur_1_y = 20, 450
            self.joueur_2_x, self.joueur_2_y = 1880, 450
            self.joueur_taille = [20,130]
            self.vitesse_y_1, self.vitesse_y_2 = 0,0
            self.joueur_1 = Joueur(self.joueur_1_x, self.joueur_1_y, self.joueur_taille)
            self.joueur_2 = Joueur(self.joueur_2_x, self.joueur_2_y, self.joueur_taille)
            self.balle_direction = [-1, 1]
            self.balle = Balle(960, 540, [10, 10], random.choice(self.balle_direction))
            self.balle_tire = False
            self.balle_vitesse_x, self.balle_vitesse_y = 10, 2

        def boucle_principale(self):
            while self.jeu_encours:
                for event in pygame.event.get():
                    
                    if event.type == pygame.QUIT:
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.vitesse_y_2 = -10  
                        if event.key == pygame.K_DOWN:
                            self.vitesse_y_2 = 10   
                        if event.key == pygame.K_z:
                            self.vitesse_y_1 = -10  
                        if event.key == pygame.K_s:
                            self.vitesse_y_1 = 10  
                        if event.key == pygame.K_SPACE:
                            self.balle_tire = True

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
                if self.balle_tire:
                    self.balle.mouvement(self.balle_vitesse_x, self.balle_vitesse_y)
                if self.joueur_1.rect.colliderect(self.balle.rect) or self.joueur_2.rect.colliderect(self.balle.rect):
                    self.balle_vitesse_x = self.changement_direction_balle(self.balle_vitesse_x, 0)
                    self.balle_vitesse_y = self.changement_direction_balle(self.balle_vitesse_y, 60)
                    self.balle.vitesse_aleatoire_y = random.randint(1, 7)
                if self.balle.rect.top <= 0 or self.balle.rect.bottom >= 1080:
                    self.balle_vitesse_y = self.changement_direction_balle(self.balle_vitesse_y, 0)
                
                self.balle.rect.clamp_ip(self.rect)

                self.ecran.fill((0,0,0,))
                self.joueur_1.afficher(self.ecran)
                self.joueur_2.afficher(self.ecran)
                self.balle.afficher(self.ecran)
                self.clock.tick(60)    
                pygame.display.flip()
        def changement_direction_balle(self, vitesse,angle):
            vitesse = - (vitesse * math.cos(angle))
            return vitesse

if  __name__ == '__main__':
    pygame.init()
    Jeu().boucle_principale()
    pygame.quit()
    