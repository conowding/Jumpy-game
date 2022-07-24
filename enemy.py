import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, y, sprite_sheet, scale):
        pygame.sprite.Sprite.__init__(self)
        
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        
        self.direction = random.choice([-1, 1])
        if self.direction == 1:
            self.flip = True
        else:
            self.flip = False
        
        animation_steps = 8
        for animation in range(animation_steps):
            image = sprite_sheet.get_image(animation, 32, 32, scale, (0, 0, 0))
            image = pygame.transform.flip(image, self.flip, False)
            image.set_colorkey((0, 0, 0))
            self.animation_list.append(image)
        
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        
        if self.direction == 1:
        	self.rect.x = 0
        else:
            self.rect.x = SCREEN_WIDTH
        self.rect.y = y
        
    def update(self, scroll, SCREEN_WIDTH):
        ANIMATION_COOLDOWN = 50
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0
        
        self.rect.x += self.direction * 2
        self.rect.y += scroll 
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()