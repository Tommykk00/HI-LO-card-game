import pygame, sys, random

#this function displays the score
def score_display():
    score_surface = smallfont.render("SCORE: " + str(int(score)), True, (255, 255, 255))
    score_rect = score_surface.get_rect(center = (500, 100))
    screen.blit(score_surface, score_rect)

pygame.init()
background_colour = (34, 156, 67)
button_color = (245, 190, 10)
width = 1000
height = 700

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('HI-LO Card Game')
screen.fill(background_colour)

smallfont = pygame.font.SysFont('Corbel',45)
higher_text = smallfont.render('HIGHER' , True , (255, 255, 255))
lower_text = smallfont.render('LOWER' , True , (255, 255, 255))

#list of all the cards
card_list = ["PNG/2C.png", "PNG/2D.png", "PNG/2H.png", "PNG/2S.png", "PNG/3C.png", "PNG/3D.png", "PNG/3H.png", "PNG/3S.png",
                      "PNG/4C.png", "PNG/4D.png", "PNG/4H.png", "PNG/4S.png", "PNG/5C.png", "PNG/5D.png", "PNG/5H.png", "PNG/5S.png",
                      "PNG/6C.png", "PNG/6D.png", "PNG/6H.png", "PNG/6S.png", "PNG/7C.png", "PNG/7D.png", "PNG/7H.png", "PNG/7S.png",
                      "PNG/8C.png", "PNG/8D.png", "PNG/8H.png", "PNG/8S.png", "PNG/9C.png", "PNG/9D.png", "PNG/9H.png", "PNG/9S.png",
                      "PNG/10C.png", "PNG/10D.png", "PNG/10H.png", "PNG/10S.png", "PNG/AC.png", "PNG/AD.png", "PNG/AH.png", "PNG/AS.png",
                      "PNG/JC.png", "PNG/JD.png", "PNG/JH.png", "PNG/JS.png", "PNG/QC.png", "PNG/QD.png", "PNG/QH.png", "PNG/QS.png",
                      "PNG/KC.png", "PNG/KD.png", "PNG/KH.png", "PNG/KS.png"]

#card_img = None

random_card = random.choice(card_list)
card_img = pygame.image.load(random_card)
card_img = pygame.transform.scale(card_img, (200, 350))

back_card = pygame.image.load("PNG/blue_back.png")
back_card = pygame.transform.scale(back_card, (200, 350))

score = 0

while True:
    for event in pygame.event.get():
        #if user closes the window it actually closes the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if h_button.collidepoint(event.pos):
                    print("HIGHER")
                    random_card = random.choice(card_list)
                    card_img = pygame.image.load(random_card)
                    card_img = pygame.transform.scale(card_img, (200, 350))
                    
                elif l_button.collidepoint(event.pos):
                    print("LOWER")
                    random_card = random.choice(card_list)
                    card_img = pygame.image.load(random_card)
                    card_img = pygame.transform.scale(card_img, (200, 350))

    if card_img != None:
        screen.blit(card_img, (100,100))

    #lower button
    l_button = pygame.Rect(400, 350, 200, 100)
    pygame.draw.rect(screen, button_color, l_button)
    screen.blit(lower_text, (450, 380))

    #higher button
    h_button = pygame.Rect(400, 150, 200, 100)
    pygame.draw.rect(screen, button_color, h_button)
    screen.blit(higher_text, (450, 180))

    score_display()
    
    screen.blit(back_card, (700,100))

    pygame.display.update()

        
