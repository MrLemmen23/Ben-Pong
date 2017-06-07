import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 65])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()

# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Instruction Screen")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Starting position of the rectangle
ellipse_x = 50
ellipse_y = 50

rect_x = 15
rect_y = 200

rect1_x = 673
rect1_y = 200
 
# Speed and direction of rectangle
ellipse_change_x = 5
ellipse_change_y = 5
 
# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)
 
display_instructions = True
instruction_page = 1
name = ""

allspriteslist = pygame.sprite.Group()
paddle_list = pygame.sprite.Group()
ball = Ball(50, 50)
player_one = Paddle(15, 200)
player_two = Paddle(673, 200)
allspriteslist.add(ball)
allspriteslist.add(player_one)
paddle_list.add(player_one)
allspriteslist.add(player_two)
paddle_list.add(player_two)

# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                name += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif event.key == pygame.K_RETURN:
                instruction_page += 1  
                if instruction_page == 3:
                    display_instructions = False
 
    # Set the screen background
    screen.fill(BLACK)
 
    if instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
 
        text = font.render("Instructions", True, WHITE)
        screen.blit(text, [10, 10])
       
        text = font.render("Enter your name: ", True, WHITE)
        screen.blit(text, [10, 40])    
       
        text = font.render(name, True, WHITE)
        screen.blit(text, [220, 40])        
 
        text = font.render("Hit enter to continue", True, WHITE)
        screen.blit(text, [10, 80])
       
        text = font.render("Page 1", True, WHITE)
        screen.blit(text, [10, 120])
 
    if instruction_page == 2:
        # Draw instructions, page 2
        text = font.render("This game is pong, move the paddle and hit the ball", True, WHITE)
        screen.blit(text, [10, 10])    
 
        text = font.render("Hit enter to continue", True, WHITE)
        screen.blit(text, [10, 40])
 
        text = font.render("Page 2", True, WHITE)
        screen.blit(text, [10, 80])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
   
    score_one = 0
    score_two = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_one.velocity = -7
            elif event.key == pygame.K_DOWN:
                player_one.velocity = 7
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_one.velocity = 0

 
    # Set the screen background
    screen.fill(BLACK)
    
    player_one.rect.y += player_one.velocity
    
    # Draw the rectangle
    pygame.draw.ellipse(screen, WHITE, [ellipse_x, ellipse_y, 25, 25])
    
 
    # Move the rectangle starting point
    ball.rect.x += ellipse_change_x
    ball.rect.y += ellipse_change_y
 
    # Bounce the ball if needed
    if ball.rect.y > 475 or ball.rect.y < 0:
        ellipse_change_y *= -1
    if ball.rect.x > 675:
        ellipse_change_x *= -1
        score_two += 1
    if ball.rect.x < 0:
        ellipse_change_x *= -1
        score_one += 1
    if pygame.sprite.spritecollide(ball, paddle_list, False):
        ellipse_change_x *= -1
 
    scoretext = "P1: " + str(score_one) + "     P2: " + str(score_two)
    text = font.render(scoretext, True, WHITE)
    screen.blit(text, [10, 10])
    allspriteslist.draw(screen)
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()