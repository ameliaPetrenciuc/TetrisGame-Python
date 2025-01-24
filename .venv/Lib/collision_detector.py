from enum import Enum

import numpy as np

class CollisionType(Enum):
    NONE=0
    BOTTOM=1
    LEFT=2
    RIGHT=3
    ROTATIONS=4

class CollisionDetector:
    def __init__(self, board, ground):
        self._board = board
        self._ground = ground

    def check(self, tile_coordinates,dx, dy):
       board_collison=self.check_board(tile_coordinates)
       ground_collison=self.check_ground(tile_coordinates,dx,dy)
       if board_collison!=CollisionType.NONE:
           return board_collison
       return  ground_collison

    def check_board(self, shape_coordinates):
        if np.max(shape_coordinates[:,1])>=self._board.height:
            return CollisionType.BOTTOM
        if np.max(shape_coordinates[:,0])>=self._board.width:
            return CollisionType.LEFT
        if np.max(shape_coordinates[:,0])<=0:
            return CollisionType.RIGHT
        return CollisionType.NONE

    def check_ground(self, tile_coordinates, dx, dy):
        ground_coordinates = self._ground.get_coordinates()
        for ground_coord_1 in ground_coordinates:
            for tile_coord_1 in tile_coordinates:
                if np.all(ground_coord_1 == tile_coord_1):
                    if dy > 0:
                        return CollisionType.BOTTOM
                    if dx > 0:
                        return CollisionType.RIGHT
                    if dx < 0:
                        return CollisionType.LEFT
                    if dx == 0 and dy == 0:
                        return CollisionType.ROTATION
                    return Collision.NONE
        return CollisionType.NONE

