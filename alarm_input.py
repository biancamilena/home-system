import pygame
from gui_elements import InputBox

def alarmInputScreen(screen, alarm, backgroundCol,textCol):
    clock = pygame.time.Clock()
    inputBox = InputBox(screen.get_width()//2 - 100, screen.get_height()//2, 200, 50)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            result = inputBox.handleEvent(event)
            if result is not None:
                alarm.alarmTime = result
                done = True

        screen.fill(backgroundCol)
        font = pygame.font.SysFont(None, 50)
        title = font.render("Set Alarm (HH:MM)", True, textCol)
        title_rect = title.get_rect(center=(screen.get_width()//2, screen.get_height()//2 - 100))
        screen.blit(title,title_rect)

        inputBox.draw(screen)
        pygame.display.flip()
        clock.tick(30)
        
