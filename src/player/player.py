import pygame

from src.settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(*groups)
        self.image = pygame.Surface((48,56)) #taille du player (de l'image)
        self.image.fill('red')

        #rect
        self.rect = self.image.get_frect(topleft = pos)
        self.old_rect = self.rect.copy()

        #movement
        self.direction = vector()
        self.speed = 200
        self.gravity = 1300

        #collision
        self.collision_sprites = collision_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_d]:
            input_vector.x += 1
        if keys[pygame.K_q]:
            input_vector.x -= 1
        self.direction = input_vector.normalize() if input_vector else input_vector

    def move(self, dt):
        #horizontale
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')

        #vertical
        self.direction.y += self.gravity * dt
        self.rect.y += self.direction.y
        self.collision('vertical')

    def collision(self, axis):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if axis == 'horizontal':
                    #left
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        # Si le côté gauche du joueur est entré en collision avec le côté droit du sprite
                        # ET que dans la position précédente le joueur était encore à droite du sprite (donc il venait de la droite)
                        # alors on considère que le joueur percute le sprite par la gauche.
                        self.rect.left = sprite.rect.right

                    #right
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                else:
                    pass

    def update(self, dt):
        self.old_rect = self.rect.copy()

        self.input()
        self.move(dt)
