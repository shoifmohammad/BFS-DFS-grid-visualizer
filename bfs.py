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

	q = [[i, j]]
	vis[i][j] = True

	text_font = pygame.font.Font('freesansbold.ttf', 30)
	while(len(q) != 0):

		time.sleep(0.5)
		for pos in q:
			draw_rect(screen, pos[1]*(w+2), pos[0]*(h+2), w, h, mark)
			text = text_font.render(str(grid[pos[0]][pos[1]]), True, black, mark)
			text = pygame.transform.scale(text, (w, h))
			screen.blit(text, (pos[1]*(w+2), pos[0]*(h+2)))
			pygame.display.update()

		l = len(q)
		for i in range(l):
			v = q.pop(0)
			
			m = v[0]-1
			n = v[1]
			if(isOk(grid, m, n)):
				if(grid[m][n] == 1 and vis[m][n] == False):
					vis[m][n] = True
					q.append([m, n])

			m = v[0]+1
			n = v[1]
			if(isOk(grid, m, n)):
				if(grid[m][n] == 1 and vis[m][n] == False):
					vis[m][n] = True
					q.append([m, n])

			m = v[0]
			n = v[1]-1
			if(isOk(grid, m, n)):
				if(grid[m][n] == 1 and vis[m][n] == False):
					vis[m][n] = True
					q.append([m, n])

			m = v[0]
			n = v[1]+1
			if(isOk(grid, m, n)):
				if(grid[m][n] == 1 and vis[m][n] == False):
					vis[m][n] = True
					q.append([m, n])

def BFS(grid, screen, vis):

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if(grid[i][j] == 1 and vis[i][j] == False):
				recursion(grid, screen, vis, i, j)