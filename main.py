import pygame,os,time,sys,random
from sys import exit
from random import randint, choice

pygame.init()
screen = pygame.display.set_mode((800,400))

class player(pygame.sprite.Sprite):#function for our player
	def __init__(self):
		super().__init__()
		player_walk_1 = pygame.image.load('images/walk1.png').convert_alpha()#graphics of our player 
		player_walk_2 = pygame.image.load('images/walk2.png').convert_alpha()
		self.player_walk = [player_walk_1,player_walk_2]#walking animation
		self.player_index = 0
		self.player_jump = pygame.image.load('images/jump.png').convert_alpha()

		self.image = self.player_walk[self.player_index]#17-19 is what defines for our gravity when player jumps
		self.rect = self.image.get_rect(midbottom = (80,300))
		self.gravity = 0

	def player_input(self):#key event for jumping
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
			self.gravity = -20
			self.jump_sound.play()

	def apply_gravity(self):#brings the player back down after jumping
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 300:
			self.rect.bottom = 300

	def animation_state(self):#function animation to make our player walk
		if self.rect.bottom < 300: 
			self.image = self.player_jump
		else:
			self.player_index += 0.1
			if self.player_index >= len(self.player_walk):self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]

	def update(self):
		self.player_input()
		self.apply_gravity()
		self.animation_state()
		
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
      


pygame.display.update()

