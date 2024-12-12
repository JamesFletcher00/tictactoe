import pygame
pygame.init()

screen_width = 500
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")

#colour definitions
white = (255,255,255)
black = (0,0,0)
background_colour = (40,40,55)

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
    
        #creates a 3x3 grid 
        self.squares = [
            pygame.Rect(self.x + col * (self.width / 3), self.y + row * ( self.height / 3), self.width / 3, self.height / 3)
        for row in range(3)
        for col in range(3)
        ]

        self.filled_squares = []

    def draw_grid(self, screen):
        pygame.draw.rect(screen, self.color, self.horizontal_rect1)
        pygame.draw.rect(screen, self.color, self.horizontal_rect2)
        pygame.draw.rect(screen, self.color, self.vertical_rect1)
        pygame.draw.rect(screen, self.color, self.vertical_rect2)

    def is_square_filled(self, square):
        return square in self.filled_squares

    def fill_square(self, square):
        if square not in self.filled_squares:
            self.filled_squares.append(square)


#X definitions
class X:
    def __init__(self, x, y, angle, height, width, color):
        self.x = x
        self.y = y
        self.angle = 45
        self.height = 10
        self.width = 75
        self.color = white
        self.piece_type = 'O'

        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.surface.fill(self.color)

        self.rect1 = None
        self.rect2 = None

    def draw_x(self, screen):
        rotated_surface1 = pygame.transform.rotate(self.surface, self. angle)
        self.rect1 = rotated_surface1.get_rect(center=(self.x, self.y))

        rotated_surface2 = pygame.transform.rotate(self.surface, -self. angle)
        self.rect2 = rotated_surface2.get_rect(center=(self.x, self.y))


        screen.blit(rotated_surface1, self.rect1.topleft)  
        screen.blit(rotated_surface2, self.rect2.topleft)   

    def is_in_square(self, square):
        if self.rect1 and self.rect2:
            return square.colliderect(self.rect1) or square.colliderect(self.rect2)
        return False

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
        self.piece_type = 'X'

    def draw_o(self, screen):
        #draws the bigger circle and the circle to display the hole
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.outer_rad)
        pygame.draw.circle(screen, self.hole_color, (self.x, self.y), self.hole_rad)

    def is_in_square(self, square): 
        return square.colliderect(self.bounding_box)

        #Game Function
class Game:
    def __init__(self, screen, grid):
        self.screen = screen
        self.grid = grid
        self.current_player = 1
        self.game_over = False
        self.pieces = []
        self.board = [['' for _ in range(3)] for _ in range(3)]

    def handle_click(self, mouse_pos):
        if self.game_over:
            return

        clicked_square = None
        for i, square in enumerate(self.grid.squares):
            if square.collidepoint(mouse_pos): #and not self.grid.is_square_filled(square):
                clicked_square = square
                row = i // 3
                col = i % 3
                if self.board[row][col] != '':
                    return
                break
        
        if not clicked_square:
            return

        x, y = clicked_square.center

        if self.current_player == 1:
            piece = X(x, y, 10, 75, 45, white)
            self.board[row][col] = 'X'
        else:
            piece = O(x, y, 40, 30, white, background_colour)
            self.board[row][col] = 'O'
        
        self.pieces.append(piece)

        if self.check_win(self.board):
            self.end_game()
        else:
            self.current_player = 1 if self.current_player == 2 else 2

    def get_square_index(self, square):
        idx = self.grid.squares.index(square) + 1
        return idx

    def check_win(self, board):
        winning_combinations = [
            [(0, 0), (0, 1), (0, 2)],  # Row 1
            [(1, 0), (1, 1), (1, 2)],  # Row 2
            [(2, 0), (2, 1), (2, 2)],  # Row 3
            [(0, 0), (1, 0), (2, 0)],  # Column 1
            [(0, 1), (1, 1), (2, 1)],  # Column 2
            [(0, 2), (1, 2), (2, 2)],  # Column 3
            [(0, 0), (1, 1), (2, 2)],  # Diagonal 1
            [(0, 2), (1, 1), (2, 0)],  # Diagonal 2
        ]

        for combination in winning_combinations:
            if all(board[row][col] == 'X' for row, col in combination):
                print(f"Player {self.current_player} wins!")
                return True

            if all(board[row][col] == 'O' for row, col in combination):
                print(f"Player {self.current_player} wins!")
                return True

        if all(board[row][col]!= '' for row in range(3) for col in range(3)):
            self.end_game(draw = True)
            return True

    def end_game(self, draw=False):
        if draw:
            print(f"It's a Draw!")
        self.game_over = True

    def draw_pieces(self):
        # Draw all X and O pieces stored
        for piece in self.pieces:
            if isinstance(piece, X):
                piece.draw_x(self.screen)
            elif isinstance(piece, O):
                piece.draw_o(self.screen)

grid = Grid(50, 250, 400, 400, white)
game = Game(screen, grid)

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            game.handle_click(event.pos)
        
    screen.fill(background_colour)

    #Draw game pieces
    grid.draw_grid(screen)
    game.draw_pieces()

    pygame.display.flip()

pygame.quit()