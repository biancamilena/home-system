import pygame

class Button:
    def __init__(self,react,color,text,textCol):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.text = text
        self.textCol = textCol
        self.font = pygame.font.SysFont(none, 36)
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        txt_surf = self.font.render(self.text, True, self.textColor)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surface.blit(txt_surf, txt_rect)
        
    def is_clicked(self,pos):
        return self.rect.collidepoint(pos)