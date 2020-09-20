import pygame

pygame.init()

mark = (175, 255, 100)
white = (255, 255, 255)
black = (0, 0, 0)
background = (0, 155, 225)
green = (0, 150, 75)
light_green = (0, 150, 0)

w = 75
h = 75

def draw_rect(screen, x, y, width, height, color):
   	pygame.draw.rect(screen, color, [x, y, width, height])

def draw_circle(screen, x, y, radius, color):
	pygame.draw.circle(screen, color, [x, y], radius)