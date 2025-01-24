import numpy as np
from collision_detector import CollisionType
class Tile:

    def __init__(self, collision_detector,shape, color, pos_x=5,pos_y=0, rotation=0):
        self._shape = shape
        self._color = color
        self._position=np.array([pos_x,pos_y])
        self._rotation=rotation
        self._collision_detector=collision_detector
        self._is_locked=False

    def render(self, board):
        matrix=self.get_coordinates()
        board.draw_tile(matrix,self._color)


    def get_coordinates(self):
        return self._shape.get_matrix_with_offset(self._rotation,self._position)

    def get_color(self):
        return self._color

    def rotate(self, direction):
        new_rotation=np.abs(np.mod(self._rotation+direction,self._shape._nr_rotations))
        new_matrix=self._shape.get_matrix_with_offset(new_rotation,self._position)

        collision=self._collision_detector.check(new_matrix,0,0)
        if collision is CollisionType.BOTTOM:
            self._is_locked=True
        if collision is CollisionType.NONE:
            self._rotation = new_rotation
        return self._is_locked

    def move(self,dx,dy):
        next_pos=self._position+np.array([dx,dy])
        new_matrix=self._shape.get_matrix_with_offset(self._rotation,next_pos)
        collision=self._collision_detector.check(new_matrix,dx,dy)
        if collision == CollisionType.BOTTOM:
            self._is_locked = True
        if collision== collision.NONE:
            self._position=next_pos
        return self._is_locked

