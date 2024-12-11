import pygame
import math
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
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

        self.line_thickness = 10

        # Create the grid as a combination of 4 rectangles (2 horizontal and 2 vertical)
        self.horizontal_rect1 = pygame.Rect(self.x, self.y + self.height / 3, self.width, self.line_thickness)
        self.horizontal_rect2 = pygame.Rect(self.x, self.y + 2 * self.height / 3, self.width, self.line_thickness)
        self.vertical_rect1 = pygame.Rect(self.x + self.width / 3, self.y, self.line_thickness, self.height)
        self.vertical_rect2 = pygame.Rect(self.x + 2 * self.width / 3, self.y, self.line_thickness, self.height)
    
    def draw_grid(self, screen):
        pygame.draw.rect(screen, self.color, self.horizontal_rect1)
        pygame.draw.rect(screen, self.color, self.horizontal_rect2)
        pygame.draw.rect(screen, self.color, self.vertical_rect1)
        pygame.draw.rect(screen, self.color, self.vertical_rect2)

grid = Grid(50, 50, 400, 400, white)

#X definitions
class X:
    def __init__(self, x, y, angle, height, width, color):
        self.x = x
        self.y = y
        self.angle = angle
        self.height = height
        self.width = width
        self.color = color

        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.surface.fill(self.color)

    def draw_x(self, screen):
        rotated_surface1 = pygame.transform.rotate(self.surface, self. angle)
        rect1 = rotated_surface1.get_rect(center=(self.x, self.y))

        rotated_surface2 = pygame.transform.rotate(self.surface, -self. angle)
        rect2 = rotated_surface2.get_rect(center=(self.x, self.y))

        screen.blit(rotated_surface1, rect1.topleft)  
        screen.blit(rotated_surface2, rect2.topleft)   


#(x, y, angle, height, width, colour)
x = X(255, 255, 45, 10, 75, white)

#O definitons

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill(background_colour)

    #Draw game pieces
    grid.draw_grid(screen)
    x.draw_x(screen)

    pygame.display.flip()

pygame.quit()