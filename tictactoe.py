import pygame
pygame.init()

screen_height = 500
screen_width = 500

screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Tic Tac Toe")

#colour definitions
white = (255,255,255)
black = (0,0,0)
background_colour = (20,20,25)

#grid definitions
class Grid:
    grid_rect_height = 450
    grid_rect_width = 50

    def draw_grid(self, screen):

#X definitions


#O definitons

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill(background_colour)
    pygame.display.flip()

pygame.quit()