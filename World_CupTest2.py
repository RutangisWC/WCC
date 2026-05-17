import pygame, random, sys,math
from pygame.locals import *
from sys import exit
from pygame.time import get_ticks

pygame.init()
mainClock = pygame.time.Clock()

FPS = 60
screenWidth = 1280
screenHeight = 640
screen = pygame.display.set_mode((screenWidth, screenHeight))
titleFont = pygame.font.Font("RobotoCondensed-VariableFont_wght.ttf", 75)
subTitleFont = pygame.font.Font("RobotoCondensed-VariableFont_wght.ttf", 32)
subSubTitleFont = pygame.font.Font("RobotoCondensed-VariableFont_wght.ttf", 25)
textFont = pygame.font.Font("RobotoCondensed-VariableFont_wght.ttf", 18)
italicFont = pygame.font.Font("RobotoCondensed-Italic-VariableFont_wght.ttf", 32)
pygame.display.set_caption("World Cup Challenge")
greenGrass = (16, 190, 26)
white = (255, 255, 255)
yellowPale = (255, 245, 121)
running = True
rulesRunning = False

def drawText(text, whatFont, color, x, y):
    textObject = whatFont.render(text, True, color)
    textRectangle = textObject.get_rect()
    textRectangle.midtop = (x, y)
    screen.blit(textObject, textRectangle)

def drawText2(text, whatFont, color, x, y):
    textObject = whatFont.render(text, True, color)
    textRectangle = textObject.get_rect()
    textRectangle.topleft = (x, y)
    screen.blit(textObject, textRectangle)


def rules():
    rulesRunning = False
    rulesRunning2 = True
    while rulesRunning:
        screen.fill(greenGrass)
        drawText('World Cup Tournament Structure', titleFont, white, screenWidth/2, 17)
        drawText2('Group Stage', subTitleFont, white, screenWidth/8, 120)
        drawText2('The Group Stage is composed of twelve groups of four teams. (48 teams total)', textFont, white, screenWidth/8, 170)
        drawText2('Each team will play the other three teams in their group once:', textFont, white, screenWidth/8, 203)
        drawText2('Each win is worth three points.', textFont, white, screenWidth/8 + 25, 226)
        drawText2('Each draw is worth one point.', textFont, white, screenWidth/8 + 25, 249)
        drawText2('The two teams with the most points in each group automatically advance to the knockout stage.', textFont, white, screenWidth/8, 282)
        drawText2('The eight third place teams with the most points across all the groups also advance to the knockout stage.', textFont, white, screenWidth/8, 305)
        drawText2('Head-to-head results will be used as a tiebreaker if necessary, followed by a series of other tiebreakers.', textFont, white, screenWidth/8, 338)

        drawText2('Knockout Stage', subTitleFont, white, screenWidth/8, 379)
        drawText2('The Knockout Stage consists of five rounds of single elimination matches, starting with the 32 teams that made it out of the group stage.', textFont, white, screenWidth/8, 429)
        drawText2('The last round consists of both a final (to determine the champion) and a third-place match (between the losing teams of the semi-finals).', textFont, white, screenWidth/8, 462)
        drawText2('If the competing teams of a match-up in the Knockout Stage are tied after regulation time, extra time will take place.', textFont, white, screenWidth/8, 495)
        drawText2('If the teams are still tied after extra time, a penalty shoot-out will take place.', textFont, white, screenWidth/8, 518)
        drawText('Deadline', subTitleFont, white, screenWidth/2, 5*screenHeight/6+ + 20)
        drawText('June 11, 1:00 pm Central Time (1 hour before first match-up)', textFont, white, screenWidth/2, 5*screenHeight/6 + 70)
        pygame.display.flip()

    while rulesRunning2:
        screen.fill(greenGrass)
        drawText('Rool Bracket and Points System', titleFont, white, screenWidth/2, 17)
        drawText2('Group Stage', subTitleFont, white, screenWidth/8, 120)
        drawText2('The Group Stage is composed of twelve groups of four teams. (48 teams total)', textFont, white, screenWidth/8, 170)
        drawText2('Each team will play the other three teams in their group once:', textFont, white, screenWidth/8, 203)
        drawText2('Each win is worth three points.', textFont, white, screenWidth/8 + 25, 226)
        drawText2('Each draw is worth one point.', textFont, white, screenWidth/8 + 25, 249)
        drawText2('The two teams with the most points in each group automatically advance to the knockout stage.', textFont, white, screenWidth/8, 282)
        drawText2('The eight third place teams with the most points across all the groups also advance to the knockout stage.', textFont, white, screenWidth/8, 305)
        drawText2('Head-to-head results will be used as a tiebreaker if necessary, followed by a series of other tiebreakers.', textFont, white, screenWidth/8, 338)

        drawText2('Knockout Stage', subTitleFont, white, screenWidth/8, 379)
        drawText2('The Knockout Stage consists of five rounds of single elimination matches, starting with the 32 teams that made it out of the group stage.', textFont, white, screenWidth/8, 429)
        drawText2('The last round consists of both a final (to determine the champion) and a third-place match (between the losing teams of the semi-finals).', textFont, white, screenWidth/8, 462)
        drawText2('If the competing teams of a match-up in the Knockout Stage are tied after regulation time, extra time will take place.', textFont, white, screenWidth/8, 495)
        drawText2('If the teams are still tied after extra time, a penalty shoot-out will take place.', textFont, white, screenWidth/8, 518)
        drawText('Deadline', subTitleFont, white, screenWidth/2, 5*screenHeight/6+ + 20)
        drawText('June 11, 1:00 pm Central Time (1 hour before first match-up)', textFont, white, screenWidth/2, 5*screenHeight/6 + 70)
        pygame.display.flip()


        
        

def startText():

    drawText('World Cup Challenge', titleFont, white, screenWidth/2, 32)

    #drawText('Leaderboard', subTitleFont, white, screenWidth/2, (screenHeight-250)/4 + 100)
    #drawText('Rules of the Pool', subTitleFont, white, screenWidth/2, (screenHeight-250)/2 + 100)
    #drawText('Pool Brackets', subTitleFont, white, screenWidth/2, (screenHeight-250)*3/4 + 100)
    #drawText('World Cup Bracket', subTitleFont, white, screenWidth/2, (screenHeight-250) + 100)
    pygame.draw.rect(screen,rgb(0,128,0),(30,30,30,30))


    drawText('Pool Brackets', subTitleFont, white, screenWidth/2, (screenHeight-250)/4 + 100)
    drawText('World Cup Standings', subTitleFont, white, screenWidth/2, (screenHeight-250)/2 + 100)
    drawText('Leaderboard', subTitleFont, white, screenWidth/2, (screenHeight-250)*3/4 + 100)
    drawText('Rules of the Pool', subTitleFont, white, screenWidth/2, (screenHeight-250) + 100)



def startDesign():

    pygame.draw.rect(screen,white,(10,10,1260,5))
    pygame.draw.rect(screen,white,(10,10,5,610))
    pygame.draw.rect(screen,white,(10,615,1260,5))
    pygame.draw.rect(screen,white,(1265,10,5,605))

    pygame.draw.rect(screen,white,(10,260,40,5))
    pygame.draw.rect(screen,white,(10,370,40,5))
    pygame.draw.rect(screen,white,(45,260,5,115))
    pygame.draw.rect(screen,white,(10,170,150,5))
    pygame.draw.rect(screen,white,(10,470,150,5))
    pygame.draw.rect(screen,white,(155,170,5,305))

    
    pygame.draw.rect(screen,white,(1230,260,40,5))
    pygame.draw.rect(screen,white,(1230,370,40,5))
    pygame.draw.rect(screen,white,(1230,260,5,115))
    pygame.draw.rect(screen,white,(1120,170,150,5))
    pygame.draw.rect(screen,white,(1120,470,150,5))
    pygame.draw.rect(screen,white,(1120,170,5,305))


    
    pygame.draw.arc(screen, white, (1060,320-100,200,200), math.pi*.62, math.pi*1.37, width=5)
    pygame.draw.arc(screen, white, (120-100,320-100,200,200), math.pi*1.63, math.pi*.37, width=5)
    
    pygame.draw.arc(screen, white, (640-100,320-100,200,200), math.pi/20, math.pi/2.7, width=5)
    pygame.draw.arc(screen, white, (640-100,320-100,200,200), math.pi/1.57, math.pi/1.07, width=5)
    pygame.draw.arc(screen, white, (640-100,320-100,200,200), math.pi*1.03, math.pi*1.32, width=5)
    pygame.draw.arc(screen, white, (640-100,320-100,200,200), math.pi*1.68, math.pi*1.97, width=5)

    pygame.draw.arc(screen, white, (5,5,30,30), math.pi*1.29, math.pi*.2, width=5)
    pygame.draw.arc(screen, white, (5,595,30,30), math.pi*1.8, math.pi*2.7, width=5)
    pygame.draw.arc(screen, white, (1245,595,30,30), math.pi*.3, math.pi*1.2, width=5)
    pygame.draw.arc(screen, white, (1245,5,30,30), math.pi*.9, math.pi*1.7, width=5)
    
def startScreen():
        screen.fill(greenGrass)
        startDesign()
        #subTitle1 = subTitleFont.render('Leaderboard', True, white)
        #subTitle1Rect = subTitle1.get_rect(midtop = (screenWidth/2, (screenHeight-250)/4 + 100))

        #subTitle2 = subTitleFont.render('Rules of the Pool', True, white)
        #subTitle2Rect = subTitle2.get_rect(midtop = (screenWidth/2, (screenHeight-250)/2 + 100))

        #subTitle3 = subTitleFont.render('Pool Brackets', True, white)
        #subTitle3Rect = subTitle3.get_rect(midtop = (screenWidth/2, (screenHeight-250)*3/4 + 100))

        #subTitle4 = subTitleFont.render('World Cup Bracket', True, white)
        #subTitle4Rect = subTitle4.get_rect(midtop = (screenWidth/2, (screenHeight-250) + 100))


        subTitle1 = subTitleFont.render('Pool Brackets', True, white)
        subTitle1Rect = subTitle1.get_rect(midtop = (screenWidth/2, (screenHeight-250)/4 + 100))

        subTitle2 = subTitleFont.render('World Cup Standings', True, white)
        subTitle2Rect = subTitle2.get_rect(midtop = (screenWidth/2, (screenHeight-250)/2 + 100))

        subTitle3 = subTitleFont.render('Leaderboard', True, white)
        subTitle3Rect = subTitle3.get_rect(midtop = (screenWidth/2, (screenHeight-250)*3/4 + 100))

        subTitle4 = subTitleFont.render('Rules of the Pool', True, white)
        subTitle4Rect = subTitle4.get_rect(midtop = (screenWidth/2, (screenHeight-250) + 100))
        

        screen.blit(subTitle1, subTitle1Rect)
        screen.blit(subTitle2, subTitle2Rect)
        screen.blit(subTitle3, subTitle3Rect)
        screen.blit(subTitle4, subTitle4Rect)
    

        #if subTitle1Rect.collidepoint(mousePosition):
            #startText()
            #drawText('Leaderboard', subTitleFont, yellowPale, screenWidth/2, (screenHeight-250)/4 + 100)
            #startDesign()
            #for event in pygame.event.get():
                #if event.type == pygame.MOUSEBUTTONDOWN:
                    #screen.fill(white)

        #elif subTitle2Rect.collidepoint(mousePosition):
            #startText()
            #drawText('Rules of the Pool', subTitleFont, yellowPale, screenWidth/2, (screenHeight-250)/2 + 100)
            #startDesign()
            #for event in pygame.event.get():
                #if event.type == pygame.MOUSEBUTTONDOWN:
                    #rulesRunning = True
                    #rules()

        #elif subTitle3Rect.collidepoint(mousePosition):
            #startText()
            #drawText('Pool Brackets', subTitleFont, yellowPale, screenWidth/2, (screenHeight-250)*3/4 + 100)
            #startDesign()
            #for event in pygame.event.get():
                #if event.type == pygame.MOUSEBUTTONDOWN:
                    #screen.fill(white)
                    
        #elif subTitle4Rect.collidepoint(mousePosition):
            #startText()
            #drawText('World Cup Bracket', subTitleFont, yellowPale, screenWidth/2, (screenHeight-250) + 100)
            #startDesign()
            #for event in pygame.event.get():
                #if event.type == pygame.MOUSEBUTTONDOWN:
                    #screen.fill(white)
        #else:
            #startText()
            #startDesign()


        if subTitle1Rect.collidepoint(mousePosition):
            startText()
            drawText('Pool Brackets', subTitleFont, yellowPale, screenWidth/2, (screenHeight-250)/4 + 100)
            startDesign()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.fill(white)

        elif subTitle2Rect.collidepoint(mousePosition):
            startText()
            drawText('World Cup Standings', subTitleFont, yellowPale, screenWidth/2, (screenHeight-250)/2 + 100)
            startDesign()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.fill(white)

        elif subTitle3Rect.collidepoint(mousePosition):
            startText()
            drawText('Leaderboard', subTitleFont, yellowPale, screenWidth/2, (screenHeight-250)*3/4 + 100)
            startDesign()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.fill(white)
                    
        elif subTitle4Rect.collidepoint(mousePosition):
            startText()
            drawText('Rules of the Pool', subTitleFont, yellowPale, screenWidth/2, (screenHeight-250) + 100)
            startDesign()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    rulesRunning = True
                    rules()
        else:
            startText()
            startDesign()



        

        
                    


while running:
    mousePosition = pygame.mouse.get_pos()
    startScreen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mainClock.tick(FPS)
    pygame.display.flip()

pygame.quit()
sys.exit()

