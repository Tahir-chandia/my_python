import pygame # Import pygame liabrary for using gaming functionalities
import time # Import time liabrary for controlling speed

# Constants
pygame.init()

CANVAS_WIDTH=400
CANVAS_HEIGHT=400
ERASER_SIZE=40
CELL_SIZE=20
WHITE=(255,255,255)
BLUE=(0,0,255)
PINK=(255,193,203)

# # Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((CANVAS_WIDTH,CANVAS_HEIGHT))
pygame.display.set_caption('Eraser')
screen.fill(WHITE)


def grid():
    """Draw a grid of blue squares """""
    for row in range(0,CANVAS_HEIGHT,CELL_SIZE):
        for col in range(0,CANVAS_WIDTH,CELL_SIZE):
            pygame.draw.rect(screen,BLUE,(row,col,CELL_SIZE,CELL_SIZE),0)

def eraser(cell):
    "Erase objects with the eraser by adding white color"
    for row in range(0,CANVAS_HEIGHT,CELL_SIZE):
        for col in range(0,CANVAS_WIDTH,CELL_SIZE):
            eraser_cell= pygame.Rect(col,row,CELL_SIZE,CELL_SIZE)
            if cell.colliderect(eraser_cell):
                pygame.draw.rect(screen,WHITE , eraser_cell,0)

def main():
    grid()
    pygame.display.update()
    eraser_x , eraser_y = CANVAS_WIDTH//2, CANVAS_HEIGHT//2  # Start eraser in center

    running = True
    while running:
        screen.fill(WHITE)
        grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse_x,mouse_y = pygame.mouse.get_pos()
        eraser_rect = pygame.Rect(mouse_x,mouse_y,ERASER_SIZE,ERASER_SIZE)
        eraser(eraser_rect)  # Erase objects that overlap with eraser
        
        pygame.draw.rect(screen,PINK,eraser_rect,0) # Draw eraser
        pygame.display.update()
        time.sleep(0.05)
        
    pygame.quit()

if __name__ == "__main__":
    main() 
