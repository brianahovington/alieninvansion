import sys
import pygame

class PracticeGame:

    def __init__ (self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Practice Game")
        self.bg_color = (0, 0, 255)
        self.ship = Mario(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.ship.blitme()

            pygame.display.flip()

class Mario:
    def __init__(self,p_g):
        self.screen = p_g.screen
        self.screen_rect = p_g.screen.get_rect()

        self.image = pygame.image.load('images/mariorun.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    pg = PracticeGame()
    pg.run_game()