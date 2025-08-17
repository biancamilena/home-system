import pygame
from datetime import datetime, timedelta

class Alarm:
    def __init__(self, time="7:30"):
        self.alarmTime = time
        self.alarmOn = False
        self.alarmRinging = False
        pygame.mixer.init()
        pygame.mixer.music.load("otherStuff/alarm.mp3")
        
    def toggle(self):
        self.alarmOn = not self.alarmOn
        
    def checkAlarm(self):
        if self.alarmOn and not self.alarmRinging:
            now = datetime.now().strftime("%H:%M")
            if now == self.alarmTime:
                self.alarmRinging = True
                pygame.mixer.music.play(-1) #loop
    
    def turnOff(self):
        self.alarmRinging = False
        pygame.mixer.music.stop()
        
    def snooze(self, minutes=5):
        now = datetime.now()
        newTime = (now + timedelta(minutes=minutes)).strftime("%H:%M")
        self.alarmTime = newTime
        self.alarmRinging = False
        pygame.mixer.music.stop()
