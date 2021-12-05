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
        self.cell_width = WIDTH//28
        self.cell_height = HEIGHT//30
        
        self._load()

    def run(self):
        while self.running:
            if self.state == 'start':
                self._start_events()
                self._start_update()
                self._start_draw()
            
            elif self.state =='play':
                self._play_events()
                self._play_update()
                self._play_draw()
            else:
                self.running = False

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
        
    def _load(self):
        maze_path = os.path.join(self.dirname, "dependencies/images/background.png")
        self.background = pygame.image.load(maze_path)
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        
    def _draw_grid(self):
        for x in range(WIDTH//self.cell_width):
            pygame.draw.line(self.screen, GREY, (x*self.cell_width, 0), (x*self.cell_width, HEIGHT))
            
        for x in range(HEIGHT//self.cell_height):
            pygame.draw.line(self.screen, GREY, (0, x*self.cell_height), (WIDTH, x*self.cell_height))

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
                    [WIDTH//2 - 100, 0],
                    START_TEXT_SIZES['HIGH_SCORE'],
                    START_TEXT_COLORS['HIGH_SCORE'],
                    START_FONT, center=False)
        
        pygame.display.update()

    # ========= PLAY FUNCTIONS ========= #

    def _play_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'play'

    def _play_update(self):
        pass

    def _play_draw(self):
        self.screen.blit(self.background, (0, 0))
        self._draw_grid()
        pygame.display.update()
        
        