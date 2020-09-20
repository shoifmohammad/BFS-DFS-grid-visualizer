import pygame
import math
from functions import *

pygame.init()

def choose():

	width = 800
	height = 400
	screen = pygame.display.set_mode((width, height))

	while(True):

		screen.fill(background)
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		
		for event in pygame.event.get():
            
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()

		text_font = pygame.font.Font('freesansbold.ttf', 40)
		text = text_font.render('Choose method', True, white)
		screen.blit(text, ((width-text.get_width())/2, 75))

		if(125 < mouse[0] < 325 and 200 < mouse[1] < 250):
			focus = light_green
			if(click[0] == 1):
				return 1

		elif(math.sqrt((mouse[0]-125)**2 + (mouse[1]-225)**2) < 25):
			focus = light_green
			if(click[0] == 1):
				return 1

		elif(math.sqrt((mouse[0]-325)**2 + (mouse[1]-225)**2) < 25):
			focus = light_green
			if(click[0] == 1):
				return 1

		else:
			focus = green

		draw_rect(screen, 125, 200, 200, 50, focus)
		draw_circle(screen, 125, 225, 25, focus)
		draw_circle(screen, 325, 225, 25, focus)
		
		text_font = pygame.font.Font('freesansbold.ttf', 30)
		text = text_font.render("BFS", True, black)
		screen.blit(text, (125+(200-text.get_width())/2, 205+(50-text.get_height())/2))

		if(475 < mouse[0] < 675 and 200 < mouse[1] < 250):
			focus = light_green
			if(click[0] == 1):
				return 2

		elif(math.sqrt((mouse[0]-475)**2 + (mouse[1]-225)**2) < 25):
			focus = light_green
			if(click[0] == 1):
				return 2

		elif(math.sqrt((mouse[0]-675)**2 + (mouse[1]-225)**2) < 25):
			focus = light_green
			if(click[0] == 1):
				return 2

		else:
			focus = green

		draw_rect(screen, 475, 200, 200, 50, focus)
		draw_circle(screen, 475, 225, 25, focus)
		draw_circle(screen, 675, 225, 25, focus)
		
		text_font = pygame.font.Font('freesansbold.ttf', 30)
		text = text_font.render("DFS", True, black)
		screen.blit(text, (475+(200-text.get_width())/2, 205+(50-text.get_height())/2))

		if(300 < mouse[0] < 500 and 300 < mouse[1] < 350):
			focus = light_green
			if(click[0] == 1):
				quit()

		elif(math.sqrt((mouse[0]-300)**2 + (mouse[1]-325)**2) < 25):
			focus = light_green
			if(click[0] == 1):
				quit()

		elif(math.sqrt((mouse[0]-500)**2 + (mouse[1]-325)**2) < 25):
			focus = light_green
			if(click[0] == 1):
				quit()

		else:
			focus = green

		draw_rect(screen, 300, 300, 200, 50, focus)
		draw_circle(screen, 300, 325, 25, focus)
		draw_circle(screen, 500, 325, 25, focus)
		
		text_font = pygame.font.Font('freesansbold.ttf', 30)
		text = text_font.render("Exit", True, black)
		screen.blit(text, (300+(200-text.get_width())/2, 305+(50-text.get_height())/2))


		pygame.display.update()

def set_screen(grid, n, m):

	width = (w+2)*m-2
	height = (h+2)*n-2

	screen = pygame.display.set_mode((width, height))
	screen.fill(white)

	for i in range(1, n):
		draw_rect(screen, 0, i*(h+2), width, 2, black)
	for i in range(1, m):
		draw_rect(screen, i*(w+2), 0, 2, height, black)

	text_font = pygame.font.Font('freesansbold.ttf', 30)
	
	for i in range(n):
		for j in range(len(grid[i])):
			text = text_font.render(str(grid[i][j]), True, black)
			text = pygame.transform.scale(text, (w, h))
			screen.blit(text, (j*(w+2), i*(h+2)))			

	pygame.display.update()

	return screen