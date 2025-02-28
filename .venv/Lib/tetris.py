import pygame.display
from board import Board

class Tetris:

    def __init__(self):
        self._screen=pygame.display.set_mode((720,770))
        self._board=Board(self._screen)
        self._running=True
        self._speed=40
        self._clock=pygame.time.Clock()
        pygame.font.init()
        self._score_font=pygame.font.SysFont("Arial", 30)
        self.run()

    def run(self):
        counter=0
        while self._running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self._running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        self._board.move_up()
                    if event.key==pygame.K_DOWN:
                        self._board.move_down()
                    if event.key==pygame.K_LEFT:
                        self._board.move_left()
                    if event.key==pygame.K_RIGHT:
                        self._board.move_right()
                    self._screen.fill((0, 0, 0))
                    self._board.update(False)
                    self._board.draw()

            if counter%self._speed==0:
                self._board.update()
                counter=1
                self._screen.fill((0, 0, 0))
                self._board.draw()

            pygame.display.flip()
            counter+=1
            self._clock.tick(40)
            text_surface=self._score_font.render('Score: '+str(self._board.score),False,(255,255,255))
            self._screen.blit(text_surface,(500,150))
        pygame.quit()


