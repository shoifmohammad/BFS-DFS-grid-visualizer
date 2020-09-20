import pygame
import time
from functions import *

pygame.init()

def isOk(grid, i, j):

	if(i<0 or i >= len(grid)):
		return False
	if(j<0 or j >= len(grid[i])):
		return False

	return True

def recursion(grid, screen, vis, i, j):

	time.sleep(0.5)
	vis[i][j] = True
	draw_rect(screen, j*(w+2), i*(h+2), w, h, mark)
	text_font = pygame.font.Font('freesansbold.ttf', 30)
	
	text = text_font.render(str(grid[i][j]), True, black, mark)
	text = pygame.transform.scale(text, (w, h))
	screen.blit(text, (j*(w+2), i*(h+2)))
	pygame.display.update()

	p = i-1
	q = j
	if(isOk(grid, p, q)):
		if(grid[p][q] == 1 and vis[p][q] == False):
			recursion(grid, screen, vis, p, q)

	p = i+1
	q = j
	if(isOk(grid, p, q)):
		if(grid[p][q] == 1 and vis[p][q] == False):
			recursion(grid, screen, vis, p, q)

	p = i
	q = j-1
	if(isOk(grid, p, q)):
		if(grid[p][q] == 1 and vis[p][q] == False):
			recursion(grid, screen, vis, p, q)

	p = i
	q = j+1
	if(isOk(grid, p, q)):
		if(grid[p][q] == 1 and vis[p][q] == False):
			recursion(grid, screen, vis, p, q)


def DFS(grid, screen, vis):

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if(grid[i][j] == 1 and vis[i][j] == False):
				recursion(grid, screen, vis, i, j)