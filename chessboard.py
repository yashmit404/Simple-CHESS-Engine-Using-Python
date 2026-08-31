import pygame
import sys
import main

WIDTH = 800
HEIGHT = 800
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH // COLS

LIGHT_GREY = (180, 180, 180)
DARK_GREY = (100, 100, 100)

IMAGES = {}

def load_images():

    sprite_sheet = pygame.image.load("pieces.png")

    sheet_width = sprite_sheet.get_width()
    sheet_height = sprite_sheet.get_height()
    piece_w = sheet_width // 6
    piece_h = sheet_height // 2

    black_pieces = ["bK", "bQ", "bB", "bN", "bR", "bP"]
    white_pieces = ["wK", "wQ", "wB", "wN", "wR", "wP"]

    for iter in range(6):

        rect = pygame.Rect(iter * piece_w, 0, piece_w, piece_h)
        image = sprite_sheet.subsurface(rect)
        IMAGES[black_pieces[iter]] = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))

    for iter in range(6):
        rect = pygame.Rect(iter * piece_w, piece_h, piece_w, piece_h)
        image = sprite_sheet.subsurface(rect)
        IMAGES[white_pieces[iter]] = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))

def draw_board(screen):

    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT_GREY if (row + col) % 2 == 0 else DARK_GREY
            pygame.draw.rect(screen, color, [col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE])

def draw_pieces(screen, board):

    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece != "0":

                screen.blit(IMAGES[piece], pygame.Rect(col * SQUARE_SIZE + 1, row * SQUARE_SIZE + 1, SQUARE_SIZE - 2, SQUARE_SIZE - 2))

def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Chess Game")

    gs = main.GameState()

    load_images()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                value, result = pygame.mouse.get_pos()
                col = value // SQUARE_SIZE
                row = result // SQUARE_SIZE
                print("You clicked on:", gs.board[row][col])

        draw_board(screen)
        draw_pieces(screen, gs.board)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_loop()