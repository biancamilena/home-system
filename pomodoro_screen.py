import pygame
import datetime
from gui_elements import Button

#colors
backgroundColor = pygame.Color("#FAFADE")
textColor = pygame.Color("#547C31")
btnColor = pygame.Color("#AAC877")
btnTxtColor = pygame.Color("#9AC559")

#button
homeBtn = Button((screen.get_width()//2-300, screen.get_height()//2), btnColor, "Home", btnTxtColor)
pomodoroBtn = Button((screen.get_width()//2-300, screen.get_height()//2+150, 120,40), btnColor, "pomodoro", btnTxtColor)
shortBreakBtn = Button((screen.get_width()//2-300, screen.get_height()//2, 160,40), btnColor, "short break", btnTxtColor)
longBreakBtn = Button((screen.get_width()//2-300, screen.get_height()//2-150, 160,40), btnColor, "long break", btnTxtColor)
restartTimerBtn = 
playTimeBtn =
pauseTimeBtn =
               

def pomodoroScreen():




    #screen fill
    screen.fill(backgroundColor)
    pomodoroPic = pygame.image.load("otherStuff\pomodoroPic.jpg")
    pomodoroPic = pygame.transform.scale(pomodoroPic, (150,150))
    breakPic = pygame.image.load("otherStuff/breakPic.jpg")
    breakPic = pygame.transform.scale(breakPic, (150,150))

    homeBtn.draw(screen)
    pomodoroBtn.draw(screen)
    shortBreakBtn.draw(screen)
    longBreakBtn.draw(screen)
    restartTimerBtn.draw(screen)
    playTimeBtn.draw(screen)
    pauseTimeBtn.draw(screen)
    
    pygame.display.flip()
    
