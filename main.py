import pygame
import datetime
from gui_elements import Button
from alarm_system import Alarm

#colors
backgroundCol = pygame.Color("#C3B1E1")
textCol = pygame.Color("#7851A9")
btnCol = pygame.Color("#301934")
btnTxtCol = pygame.Color("#702670")

# initialize
pygame.init()
screen = pygame.display.set_mode((480,320))
pygame.display.set_caption("Clock and Alarm")

#clock setup
font = pygame.font.SysFont(None, 80)
clock = pygame.time.Clock()
alarm = Alarm("7:30")

#buttons
toggleBtn = Button((20,260,100,40), btnCol, "Is Off", btnTxtCol)
setBtn = Button((140,260,100,40), btnCol, "Set Alarm", btnTxtCol)
snoozeBtn = Button((260,260,100,40), btnCol, "Snooze", btnTxtCol)
turnOffBtn = Button((380,260,100,40), btnCol, "Turn Off", btnTxtCol)

#--------------------------------------------------

#logic
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if alarm.alarmRinging:
                if snoozeBtn.is_clicked(event.pos):
                    alarm.snooze()
                elif turnOffBtn.is_clicked(event.pos):
                    alarm.turnOff
            else:
                if toggleBtn.is_clicked(event.pos) and alarm.alarmOn == False:
                    alarm.toggle()
                    toggleBtn.text = "Is On"
                elif toggleBtn.is_clicked(event.pos) and alarm.alarmOn == True:
                    alarm.toggle()
                    toggleBtn.text = "Is Off"
                elif setBtn.is_clicked(event.pos):
                    #implement text input
                    pass
                
    #update alarm
    alarm.checkAlarm()
    
    #get time
    now = datetime.datetime.now().strftime("%H:%M:%S")
    
    #text
    timeTxt = font.render(now,True,textCol)
    time_rect = timeTxt.get_rect(center=(screen.get_width()//2, screen.get_height()//2))
    screen.blit(timeTxt, time_rect)
    
    #alarm time
    alarm_font = pygame.font.SysFont(None,40)
    alarmTxt = alarm_font.render(f"Alarm: {alarm.alarmTime}", True, textCol)
    alarm_rect = alarmTxt.get_rect(center=(screen.get_width()//2, screen.get_height()//2 + 60))
    screen.blit(alarmTxt, alarm_rect)
    
    #draw buttons
    if alarm.alarmRinging:
        snoozeBtn.draw(screen)
        turnOffBtn.draw(screen)
    else:
        toggleBtn.draw(screen)
        setBtn.draw(screen)
    
    pygame.display.flip()
    clock.tick(30) #update seconds
    
pygame.quit()
    
