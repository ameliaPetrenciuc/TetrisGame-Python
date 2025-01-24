import shape
import pygame
import numpy as np
from tile import Tile
import random
from collision_detector import CollisionDetector
from ground import Ground
#am folosit aceasta biblioteca pt a lucra mai eficient cu matricile

class Board:
    def __init__(self, screen, height=20, width=10):
        self._screen = screen
        self.height = height
        self.width = width
        self._ground=Ground(width,height)
        self._matrix = np.zeros([width,height],dtype=int)#se initializeaza matricea
        self._current_tile=None
        self.score=0
        self._colours=shape.generate_colours()
        self._shapes=shape.generate_shapes()
        self._collision_detector=CollisionDetector(self,self._ground)
        #'_' in fata numelor de variabila este folista pt a indica ca aceste variabile sunt considerate private

    def draw(self):
        blockSize=35
        x_offset=100
        y_offset=50
        for x in range(self.width):
            for y in range(self.height):
                rectangle=pygame.Rect(x_offset+x*blockSize,y_offset+y*blockSize,blockSize,blockSize)
                pygame.draw.rect(self._screen,self._colours[self._matrix[x,y]],rectangle,1 if self._matrix[x,y]==0 else 0)

    def draw_tile(self,tile):
        matrix=tile.get_coordinates()
        for pos in matrix:
            if pos[1]<self.height:
                self._matrix[pos[0],pos[1]]=tile.get_color()


    def update(self, on_timer=True):
        if self._current_tile is None:
            self.create_tile()
        if on_timer:
            self.drop_tile()
        self._matrix[:,:]=0
        self.draw_tile(self._current_tile)
        self.draw_ground(self._ground)

    def draw_ground(self, ground):
        self._matrix = np.maximum(self._matrix, ground.get_matrix())

    def create_tile(self):
        self._current_tile=Tile(self._collision_detector,self.get_shape(),self.get_color(), random.randint(0,6))

    def get_color(self):
        return random.randint(1,len(self._colours)-1)

    def get_shape(self):
        return self._shapes[random.randint(0,len(self._shapes)-1)]

    def move_up(self):
        self._current_tile.rotate(1)
        self.draw()

    def move_down(self):
        self._current_tile.move(0,1)
        self.draw()

    def move_left(self):
        self._current_tile.move(-1,0)
        self.draw()

    def move_right(self):
        self._current_tile.move(1, 0)
        self.draw()

    def drop_tile(self):
        is_locked=self._current_tile.move(0,1)
        if is_locked:
            self._ground.merge(self._current_tile)
            self.score=self.score+self._ground.expire_rows()
            self.create_tile()




