import pygame
import random

def main():
    pygame.init() # initializing pygame

    window = pygame.display.set_mode((400, 600)) # window size
    pygame.display.set_caption("Dice Roll Simulator") # window title
    pygame.display.set_icon(pygame.image.load("assets/icon.png")) # window icon

    answ = input("Do you want to roll the dice? (y/n):") # asking user in console

    # checking if the user wants to roll the dice
    if answ.lower() == "y":
        roll_dice()
    elif answ.lower() == "n":
        print("Not rolling the dice")
    else:
        print("Invalid input, enter 'y' or 'n'")

    running = True
    # inifite loop to keep window open
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill("white") # clearing the window
        pygame.display.flip() # updating the window
    
    pygame.quit() # uninitializing pygame

# function to choose a random number between 1-6
def roll_dice():
    result = random.randint(1, 6) 
    print(f"Dice rolled: {result}")
    
if __name__ == "__main__": main()