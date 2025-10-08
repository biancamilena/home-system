import pygame
from datetime import datetime
from gui_elements import Button
from alarm_system import Alarm
from alarm_input import alarmInputScreen

#colors
backgroundCol = pygame.Color("#C3B1E1")
textCol = pygame.Color("#7851A9")
btnCol = pygame.Color("#8e7ea8")
btnTxtCol = pygame.Color("#5f4085")

# initialize
pygame.init()
screen = pygame.display.set_mode((480,320))
pygame.display.set_caption("Clock and Alarm")

#clock setup
font = pygame.font.SysFont(None, 80)
dateFont = pygame.font.SysFont(None,40)
dayFont = pygame.font.SysFont(None, 60)
clock = pygame.time.Clock()
alarm = Alarm()

#buttons
toggleBtn = Button((40,260,100,40), btnCol, "Is Off", btnTxtCol)
setBtn = Button((160,260,120,40), btnCol, "Set Alarm", btnTxtCol)
snoozeBtn = Button((240,230,100,40), btnCol, "Snooze", btnTxtCol)
turnOffBtn = Button((360,230,100,40), btnCol, "Turn Off", btnTxtCol)

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
                    alarm.turnOff()
            else:
                if toggleBtn.is_clicked(event.pos) and alarm.alarmOn == False:
                    alarm.toggle()
                    toggleBtn.text = "Is On"
                elif toggleBtn.is_clicked(event.pos) and alarm.alarmOn == True:
                    alarm.toggle()
                    toggleBtn.text = "Is Off"
                elif setBtn.is_clicked(event.pos):
                    alarmInputScreen(screen, alarm, backgroundCol, textCol)
                
    #update alarm
    alarm.checkAlarm()

    #clear screen
    screen.fill(backgroundCol)
    
    #get time
    now = datetime.now().strftime("%H:%M:%S")
    current_datetime = datetime.now()
    currentDate = current_datetime.date()
    currentDay = current_datetime.strftime("%A")
    
    #time text
    timeTxt = font.render(now,True,textCol)
    time_rect = timeTxt.get_rect(center=(screen.get_width()//2-90, screen.get_height()//2+30))
    screen.blit(timeTxt, time_rect)

    #date text
    dateTxt = dateFont.render(current_datetime.strftime("%b %d, %Y"), True, textCol)
    date_rect = dateTxt.get_rect(center=(screen.get_width()//2-90, screen.get_height()//2-20))
    screen.blit(dateTxt, date_rect)

    #day text
    dayTxt = dayFont.render(currentDay, True, textCol)
    day_rect = dayTxt.get_rect(center=(screen.get_width()//2-90, screen.get_height()//2-60))
    screen.blit(dayTxt, day_rect)

    #pics
    clockPic = pygame.image.load("otherStuff/clock.png")
    clockPic = pygame.transform.scale(clockPic, (300,300))
    alarmPic = pygame.image.load("otherStuff/alarmGoingOff.png")
    alarmPic = pygame.transform.scale(alarmPic, (300,300))
    
    #draw buttons
    if alarm.alarmRinging:
        snoozeBtn.draw(screen)
        turnOffBtn.draw(screen)
        screen.blit(alarmPic, (225,0))
    else:
        toggleBtn.draw(screen)
        setBtn.draw(screen)
        screen.blit(clockPic, (225,0))
    
    pygame.display.flip()
    clock.tick(30) #update seconds
    
pygame.quit()
    
