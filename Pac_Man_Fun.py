import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 560, 620
ROWS, COLS = 31, 28
TILE_SIZE = 20

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Pac-Man")
clock = pygame.time.Clock()

# Maze layout: 0 = dot, 1 = wall, 2 = empty
maze = [
    [1]*28,
    [1]+[0]*26+[1],
    [1]+[0]+[1]*24+[0]+[1],
    [1]+[0]*26+[1],
    [1]*28,
] + [[1]+[0]*26+[1] for _ in range(26)] + [[1]*28]  # Just a placeholder maze

# Pac-Man position
pacman_x = 14
pacman_y = 23
direction = (0, 0)

def draw_maze():
    for y, row in enumerate(maze):
        for x, tile in enumerate(row):
            if tile == 1:
                pygame.draw.rect(screen, BLUE, (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif tile == 0:
                pygame.draw.circle(screen, WHITE, (x*TILE_SIZE+TILE_SIZE//2, y*TILE_SIZE+TILE_SIZE//2), 3)

def draw_pacman(x, y):
    pygame.draw.circle(screen, YELLOW, (x*TILE_SIZE+TILE_SIZE//2, y*TILE_SIZE+TILE_SIZE//2), TILE_SIZE//2)

def move_pacman(x, y, dx, dy):
    if maze[y+dy][x+dx] != 1:
        return x+dx, y+dy
    return x, y

# Game loop
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (1, 0)
            elif event.key == pygame.K_UP:
                direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                direction = (0, 1)

    pacman_x, pacman_y = move_pacman(pacman_x, pacman_y, *direction)

    if maze[pacman_y][pacman_x] == 0:
        maze[pacman_y][pacman_x] = 2  # Eat the dot

    draw_maze()
    draw_pacman(pacman_x, pacman_y)

    pygame.display.flip()
    clock.tick(10)
