import pygame, random, time, sys, os

#Initializes the Clock
clock = pygame.time.Clock()

# Sets the programs framerate
FPS = 60

# Sets the screen Width and Height
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600

# Opens a window with defined screen size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create variable for background color
bg_color = (250, 248, 239)

# Fills the screen with color defined above
screen.fill(bg_color)


# Sets the window name
pygame.display.set_caption("py2048")
# Draws all changes to the window
pygame.display.update()

#############################
#   FUNCTIONS AND CLASSES   #
#############################

class Tile:
    # set it up so that there is a 90% chance of spawning a 2
    def __init__(self, value = 0):
        self.value = value

    def draw(self):
        if self.value != 0:
            # draw
            pass



def draw_board_bg():
    pygame.draw.rect(screen, (187, 173,160), (0, SCREEN_HEIGHT-500, 500, 500))
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, (205, 193, 180), (15 + 121*i, (SCREEN_HEIGHT - 485) + 121*j, 106, 106))

board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

def spawnTile():
    x = random.randrange(0, 4)
    y = random.randrange(0, 4)
    if board[x][y] == 0:
        board[x][y] = 4 if random.random() > 0.9 else 2


# Create initial tiles at start of game
for i in range(2):
    spawnTile()

def displayTiles():
    for i in range(4):
        for j in range(4):
            print (board[i][j], end = " ")
        print()

def moveTiles(direction):
    """
    Direction Parameter: string
    "left", "right", "up", "down"
    
    This function handles the movement of tiles when keys are pressed
    """
    if direction == "left":
        # Move through rows, then colums
        for j in range(1,4):
            for i in range(0,4):

    if direction == "right":
        pass
    if direction == "up":
        pass
    if direction == "down":
        pass

    # call spawnTile()


displayTiles()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print ("LEFT")
            if event.key == pygame.K_RIGHT:
                print ("RIGHT")
            if event.key == pygame.K_UP:
                print ("UP")
            if event.key == pygame.K_DOWN:
                print ("DOWN")

    draw_board_bg()



    pygame.display.update()
