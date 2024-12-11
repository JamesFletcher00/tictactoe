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
    
        self.squares = [
            pygame.Rect(self.x + col * (self.width / 3), self.y + row * ( self.height / 3), self.width / 3, self.height / 3)
        for row in range(3)
        for col in range(3)
        ]

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

        self.rect1 = None
        self.rect2 = None

    def draw_x(self, screen):
        rotated_surface1 = pygame.transform.rotate(self.surface, self. angle)
        rect1 = rotated_surface1.get_rect(center=(self.x, self.y))

        rotated_surface2 = pygame.transform.rotate(self.surface, -self. angle)
        rect2 = rotated_surface2.get_rect(center=(self.x, self.y))

        screen.blit(rotated_surface1, rect1.topleft)  
        screen.blit(rotated_surface2, rect2.topleft)   

    def is_in_square(self, square):
        if self.rect1 and self.rect2:
            return square.colliderect(self.rect1) or square.colliderect(self.rect2)
        return False

#(x, y, angle, height, width, colour)
x = X(255, 255, 45, 10, 75, white)

#O definitons
class O:
    def __init__(self, x, y, outer_rad, hole_rad, color, hole_color):
        self.x = x
        self.y = y
        self.outer_rad = outer_rad
        self.hole_rad = hole_rad
        self.color = color
        self.hole_color = hole_color
        self.bounding_box = pygame.Rect(x - outer_rad, y - outer_rad, 2 * outer_rad, 2 * outer_rad)

    def draw_o(self, screen):
        #draws the bigger circle and the circle to display the hole
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.outer_rad)
        pygame.draw.circle(screen, self.hole_color, (self.x, self.y), self.hole_rad)

    def is_in_square(self, square): 
        return square.colliderect(self.bounding_box)

o = O(0, 120, 40, 30, white, background_colour)

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
    o.draw_o(screen)

    for i, square in enumerate(grid.squares):
        if o.is_in_square(square):
            print(f"0 is in square {i + 1}")
        if x.is_in_square(square):
            print(f"X is in Square {i + 1}")

    pygame.display.flip()

pygame.quit()