import pygame
import math

pygame.init()

SCREEN_H, SCREEN_W = 680, 1100 

plus_icon = pygame.transform.scale(pygame.image.load("assets/plus-icon.png"), (50, 50))
del_icon = pygame.transform.scale(pygame.image.load("assets/del-icon.png"), (50, 50))
reset_icon = pygame.transform.scale(pygame.image.load("assets/reset.png"), (50, 50))

arial = pygame.font.SysFont("Arial", 30, True)

win_title = input("Window Title: ")

numteams = int(input("Number of teams: "))

# alpha - red, bravo - yellow, charlie - green

default_colors = [(245, 126, 103), (245, 228, 118), (66, 245, 117), (66, 239, 245)]

teams = [input(f"Team {i+1} name: ") for i in range(numteams)]
teamtext = [arial.render(team, True, "black") for team in teams]
team_scores = [0]*numteams
team_colors = (default_colors*math.ceil(numteams/len(default_colors)))[:numteams]
team_height = SCREEN_H//numteams
team_starts = [i*team_height for i in range(numteams)]
team_color_surfs = [pygame.Surface((SCREEN_W, team_height)) for _ in range(numteams)]
team_add_rects = [pygame.Rect(((100+teamtext[i].get_width(), team_starts[i]+10)), (plus_icon.get_width(), plus_icon.get_height())) for i in range(numteams)]
team_del_rects = [pygame.Rect(((170+teamtext[i].get_width(), team_starts[i]+10)), (plus_icon.get_width(), plus_icon.get_height())) for i in range(numteams)]
team_reset_rects = [pygame.Rect(((240+teamtext[i].get_width(), team_starts[i]+10)), (reset_icon.get_width(), reset_icon.get_height())) for i in range(numteams)]

for i, surf in enumerate(team_color_surfs):
	surf.fill(team_colors[i])

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption(win_title)
pygame.display.set_icon(plus_icon)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1: add = 1 # left click
			if event.button == 3: add = 5 # right click
			pos = pygame.mouse.get_pos()

			for i, rect in enumerate(team_add_rects):
				if rect.collidepoint(pos):
					team_scores[i]+=add
					break
			else:
				for i, rect in enumerate(team_del_rects):
					if rect.collidepoint(pos):
						team_scores[i]-=add
						break
				else:
					for i, rect in enumerate(team_reset_rects):
						if rect.collidepoint(pos):
							team_scores[i] = 0
							break

	for i, surf in enumerate(team_color_surfs):
		screen.blit(surf, (0, team_starts[i]))
		screen.blit(teamtext[i], (10, team_starts[i]+10))
		screen.blit(arial.render(str(team_scores[i]), True, "black"), (teamtext[i].get_width()+30, team_starts[i]+10))
		screen.blit(plus_icon, team_add_rects[i])
		screen.blit(del_icon, team_del_rects[i])
		screen.blit(reset_icon, team_reset_rects[i])

	pygame.display.update()