"""
The following code is for the Famous Game "ROCK PAPER SCISSORS".
Its a single player game to be played against computer.
"""

import random
import pygame
Cscore=0
Pscore=0

# logic code of the game
def game(player):
    global Cscore
    global Pscore
    choices = ["Rock", "Paper", "Scissors"]
    #Computer randomly makes an choice
    computer = random.choice(choices)
    if player == computer:
            #return"It's a tie!"
            return"Tie.png"
    elif player == "Rock":
        if computer == "Paper":
            Cscore+=1
            #returns "You lose... paper covers rock"
            return "L_PR.png"
        else:
            Pscore+=1
            #returns "You win! rock smashes scissors"
            return "W_RS.png"
    #Similarly for others....
    elif player == "Paper":
        if computer == "Scissors":
            Cscore += 1
            #returns "You lose... scissors cut paper"
            return "L_SP.png"
        else:
            Pscore += 1
            #returns "You win! paper covers rock"
            return "W_PR.png"
    elif player == "Scissors":
        if computer == "Rock":
            Cscore += 1
            #returns "You lose... rock smashes scissors"
            return "L_RS.png"
        else:
            Pscore += 1
            #return "You win! scissors cuts paper"
            return "W_SP.png"
    elif player=='End':
        print("Final Scores:")
        print("computer score: ",Cscore)
        print("player score: ",Pscore)
        if Cscore>Pscore:
            #Result="COMPUTER WINS"
            print("COMPUTER WINS")
        elif Pscore>Cscore:
            #Result = "YOU WIN"
            print("YOU WIN")
        else:
            #Result = "TIE"
            print("Tie")
        return 'end.png'

#intializing pygame
pygame.init()
white=(255, 255, 255)
X=800
Y=500
screen = pygame.display.set_mode([X, Y])
pygame.display.set_caption('Rock-Paper-Scissor')

#Pending: Display final scores in game interface
'''
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(str(Cscore), True, white)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)
'''

# Function to call image
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def bg():
    screen.fill(white)
    BackGround = Background('Start.png', [0, 0])
    screen.blit(BackGround.image, BackGround.rect)

running=True
while running==True:
    bg()
    pygame.display.update()
    pygame.display.flip()
    for event in pygame.event.get():
        font = pygame.font.Font('freesansbold.ttf', 32)
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                display=game("Rock")
                def bg():
                    screen.fill(white)
                    BackGround = Background(display, [0, 0])
                    screen.blit(BackGround.image, BackGround.rect)
            elif event.key == pygame.K_RIGHT:
                display=game("Scissors")
                def bg():
                    screen.fill(white)
                    BackGround = Background(display, [0, 0])
                    screen.blit(BackGround.image, BackGround.rect)
            elif event.key == pygame.K_LEFT:
                display = game("Paper")
                def bg():
                    screen.fill(white)
                    BackGround = Background(display, [0, 0])
                    screen.blit(BackGround.image, BackGround.rect)
            elif event.key == pygame.K_ESCAPE:
                display = game("End")
                def bg():
                    screen.fill(white)
                    BackGround = Background(display, [0, 0])
                    screen.blit(BackGround.image, BackGround.rect)
                    #screen.blit(text, textRect) (try for final scores)
        pygame.display.update()





