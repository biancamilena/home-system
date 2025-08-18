import pygame
import datetime
from gui_elements import InputBox

def alarmInputScreen(screen, alarm, backgroundCol,textCol):
    clock = pygame.time.Clock()
    inputBox = InputBox(screen.get_width()//2 - 40, screen.get_height()//2, 200, 50)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            result = inputBox.handleEvent(event)
            if result is not None:
                clean = result.strip()
                try:
                    parsed = datetime.datetime.strptime(clean, "%H:%M")
                    alarm.setTime(parsed.strftime("%H:%M"))
                    done = True
                except ValueError:
                    print("Invalid format")

        screen.fill(backgroundCol)
        pic = pygame.image.load("otherStuff/setalarm.png")
        pic = pygame.transform.scale(pic, (150, 150))
        screen.blit(pic, (40,100))
        font = pygame.font.SysFont(None, 50)
        title = font.render("Set Alarm (HH:MM)", True, textCol)
        title_rect = title.get_rect(center=(screen.get_width()//2, screen.get_height()//2 - 100))
        screen.blit(title,title_rect)

        inputBox.draw(screen)
        pygame.display.flip()
        clock.tick(30)
        
