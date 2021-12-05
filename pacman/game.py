import pygame
import sys
import os
from settings import *

pygame.init()
# vec = pygame.math.Vector2
# print(vec)


class Game:
    def __init__(self):
        self.dirname = os.path.dirname(__file__)
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        img_path = os.path.join(self.dirname, PACMAN_ICON)
        img_surface = pygame.image.load(img_path)
        pygame.display.set_icon(img_surface)
        pygame.display.set_caption('Pacman')
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'

    def run(self):
        while self.running:
            if self.state == 'start':
                self._start_events()
                self._start_update()
                self._start_draw()
            else:
                pass

            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

    # ========= HELPER FUNCTIONS ========= #

    def render_text(self, text, pos, size, color, font_name, center=True):
        """ Render Text on to the center of the screen """

        # get font from dependencies
        font_path = os.path.join(self.dirname, font_name)

        # create message object from
        font = pygame.font.Font(font_path, size)
        message = font.render(text, False, color)
        message_size = message.get_size()

        # render message
        if center:
            pos[0] = pos[0] - message_size[0]//2
            pos[1] = pos[1] - message_size[1]//2
        
        self.screen.blit(message, pos)

    # ========= START FUNCTIONS ========= #

    def _start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'play'

    def _start_update(self):
        pass

    def _start_draw(self):
        self.screen.fill(BLACK)

        # Render Text
        self.render_text('PRESS  SPACE  TO  START',
                         [WIDTH//2, HEIGHT//2],
                         START_TEXT_SIZES['START'],
                         START_TEXT_COLORS['START'],
                         START_FONT)
        
        self.render_text('1 PLAYER ONLY',
                         [WIDTH//2, HEIGHT//2 + 72],
                         START_TEXT_SIZES['1P'],
                         START_TEXT_COLORS['1P'],
                         START_FONT)

        self.render_text('© SATWIK SRIVASTAVA',
                    [WIDTH//2, HEIGHT//2 + 144],
                    START_TEXT_SIZES['CREATED'],
                    START_TEXT_COLORS['CREATED'],
                    START_FONT)

        self.render_text('HIGH SCORE',
                    [WIDTH//2, HEIGHT//2 + 144],
                    START_TEXT_SIZES['CREATED'],
                    START_TEXT_COLORS['CREATED'],
                    START_FONT, center=False)
        
        pygame.display.update()
