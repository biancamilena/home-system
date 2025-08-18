import pygame

class Button:
    def __init__(self,rect,color,text,textCol):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.text = text
        self.textCol = textCol
        self.font = pygame.font.SysFont(None, 36)
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius = 30)
        txt_surf = self.font.render(self.text, True, self.textCol)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surface.blit(txt_surf, txt_rect)
        
    def is_clicked(self,pos):
        return self.rect.collidepoint(pos)


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x,y,w,h)
        self.color_inactive = pygame.Color("#7851A9")
        self.color_active = pygame.Color("#5f4085")
        self.color = self.color_inactive
        self.text = text
        self.txt_surface = pygame.font.SysFont(None, 40).render(text, True, (0,0,0))
        self.active = False

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = pygame.font.SysFont(None,40).render(self.text,True, (0,0,0))
        return None

    def draw(self,screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
