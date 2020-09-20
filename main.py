import pygame
import time
from windows import *
from dfs import *
from bfs import *

def visualize():

	grid = [
				[1, 1, 0, 0, 1, 1],
				[1, 1, 1, 0, 1, 0],
				[0, 1, 1, 0, 0, 0, 1],
				[0, 0, 0, 1, 1, 0],
				[1, 1, 1, 0, 1, 1, 1, 1],
				[0, 1, 0, 1, 1, 1, 1, 1],
				[0, 0, 0, 0, 1, 1, 1, 1],
				[0, 1, 0, 0, 1, 1, 1, 1]
			]
	
	n = len(grid)
	m = -1
	for i in range(n):
		m = max(m, len(grid[i]))

	if(n == 0 or m == 0):
		quit()

	vis = []
	for i in range(n):
		vis.append([])
		for j in range(m):
			vis[i].append(False)

	ret = choose()

	screen = set_screen(grid, n, m)

	if(ret == 1):
		BFS(grid, screen, vis)
	elif(ret == 2):
		DFS(grid, screen, vis)

	time.sleep(3)


if __name__ == '__main__':
	visualize()