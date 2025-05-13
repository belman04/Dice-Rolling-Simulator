import pygame
import random

def main():

    history = [] # list of previous rolls

    pygame.init() # initializing pygame

    window = pygame.display.set_mode((400, 500)) # window size
    pygame.display.set_caption("Dice Roll Simulator") # window title
    pygame.display.set_icon(pygame.image.load("assets/icon.png")) # window icon

    #setting font size and style
    font_title = pygame.font.SysFont("Albert Sans", 35)
    font_subtitle = pygame.font.SysFont("Albert Sans", 22)
    font_history = pygame.font.SysFont("Albert Sans", 20, italic=True)

    # rendering text
    text_title = font_title.render("CLICK TO ROLL", True, "black")
    text_subtitle = font_subtitle.render("Previous Results", True, (50, 50, 85))

    title_rect = text_title.get_rect(center=(200, 80))
    subtitle_rect = text_subtitle.get_rect(center=(100, 400))

    # rendering and positioning images
    dice_img = pygame.image.load("assets/dice.png")
    dice_img = pygame.transform.scale(dice_img, (310, 220)) # scaling image
    dice_rect = dice_img.get_rect(center=(200, 220))

    dice_1 = pygame.image.load("assets/dice_1.png")
    dice_1 = pygame.transform.scale(dice_1, (200, 215)) # scaling image
    dice_1_rect = dice_1.get_rect(center=(200, 220))

    dice_2 = pygame.image.load("assets/dice_2.png")
    dice_2 = pygame.transform.scale(dice_2, (200, 215)) # scaling image
    dice_2_rect = dice_2.get_rect(center=(200, 220))

    dice_3 = pygame.image.load("assets/dice_3.png")
    dice_3 = pygame.transform.scale(dice_3, (200, 215)) # scaling image
    dice_3_rect = dice_3.get_rect(center=(200, 220))

    dice_4 = pygame.image.load("assets/dice_4.png")
    dice_4 = pygame.transform.scale(dice_4, (200, 215)) # scaling image
    dice_4_rect = dice_4.get_rect(center=(200, 220))

    dice_5 = pygame.image.load("assets/dice_5.png")
    dice_5 = pygame.transform.scale(dice_5, (200, 215)) # scaling image
    dice_5_rect = dice_5.get_rect(center=(200, 220))

    dice_6 = pygame.image.load("assets/dice_6.png")
    dice_6 = pygame.transform.scale(dice_6, (200, 215)) # scaling image
    dice_6_rect = dice_6.get_rect(center=(200, 220))

    game_state = "waiting"

    # function to choose a random number between 1-6
    def roll_dice(history):
        nonlocal game_state
        
        game_state = "playing"

        result = random.randint(1, 6) 
        # print(f"Dice rolled: {result}") # printing in console
        history.append(result) # adding result to history
        # print(f'Previous results: {history}') # printing in console
        
        return result

    # answ = input("Do you want to roll the dice? (y/n):").lower() # asking user in console

    # # checking if the user wants to roll the dice in console
    # if answ == "y":
    #     roll_dice(history)
    # elif answ == "n":
    #     print("Not rolling the dice")
    # else:
    #     print("Invalid input, enter 'y' or 'n'")

    running = True
    # inifite loop to keep window open
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if dice_rect.collidepoint(event.pos,):
                    result = roll_dice(history)
                    game_state = "playing"

        window.fill("white") # clearing the window

        if game_state == "waiting": # 
            window.blit(text_title, title_rect)
            window.blit(dice_img, dice_rect)
        elif game_state == "playing":
            window.blit(text_subtitle, subtitle_rect)

            # showing the dice image based on the result
            if result == 1:
                window.blit(dice_1, dice_1_rect)
            elif result == 2:
                window.blit(dice_2, dice_2_rect)
            elif result == 3:
                window.blit(dice_3, dice_3_rect)
            elif result == 4:
                window.blit(dice_4, dice_4_rect)
            elif result == 5:
                window.blit(dice_5, dice_5_rect)
            elif result == 6:
                window.blit(dice_6, dice_6_rect)
            
            # displaying previous results
            for i, num in enumerate(history[-5:][::-1]): # getting las 5 results -5: in reverse order ::-1
                text_history = font_history.render(str(num), True, (205, 65, 65)) # rendering from numers to text
                window.blit(text_history, (100 + i * 50, 430))
                
        pygame.display.flip() # updating the window
    
    pygame.quit() # uninitializing pygame

if __name__ == "__main__": main()