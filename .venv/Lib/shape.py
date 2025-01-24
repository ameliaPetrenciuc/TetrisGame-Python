import numpy as np

class Shape:

    def __init__(self, rotations):
        self.rotations = rotations
        self._nr_rotations = len(rotations)

    def get_matrix_with_offset(self, rotation, offset):
            return offset+self.rotations[rotation]

def generate_shapes():

        #shape I
        shape_i_rot1=np.array([[1,0],[1,1],[1,2],[1,3]],np.int32)
        shape_i_rot2=np.array([[0,1],[1,1],[2,1],[3,1]],np.int32)
        shape_i=Shape(np.array([shape_i_rot1,shape_i_rot2]))

        #shape O
        shape_o_rot1=np.array([[1,1],[1,2],[2,1],[2,2]],np.int32)
        shape_o=Shape(np.array([shape_o_rot1]))

        #shape S
        shape_s_rot1=np.array([[1,0],[1,1],[0,1],[0,2]],np.int32)
        shape_s_rot2=np.array([[0,1],[1,1],[1,2],[2,2]],np.int32)
        shape_s=Shape(np.array([shape_s_rot1,shape_s_rot2]))

        #shape Z
        shape_z_rot1=np.array([[0,1],[0,2],[1,2],[1,3]],np.int32)
        shape_z_rot2=np.array([[0,2],[1,2],[1,1],[2,1]],np.int32)
        shape_z=Shape(np.array([shape_z_rot1,shape_z_rot2]))

        #shape L
        shape_l_rot1=np.array([[1,0],[1,1],[1,2],[2,2]],np.int32)
        shape_l_rot2=np.array([[0,2],[1,2],[2,2],[2,1]],np.int32)
        shape_l_rot3=np.array([[1,0],[2,0],[2,1],[2,2]],np.int32)
        shape_l_rot4=np.array([[0,3],[0,2],[1,2],[2,2]],np.int32)
        shape_l=Shape(np.array([shape_l_rot1,shape_l_rot2]))

        # shape J
        shape_j_rot1 = np.array([[2, 0], [2, 1], [2, 2], [1, 2]], np.int32)
        shape_j_rot2 = np.array([[0, 1], [1, 1], [2, 1], [2, 2]], np.int32)
        shape_j_rot3 = np.array([[3, 0], [2, 0], [2, 1], [2, 2]], np.int32)
        shape_j_rot4 = np.array([[0, 1], [0, 2], [1, 2], [2, 2]], np.int32)
        shape_j = Shape(np.array([shape_j_rot1, shape_j_rot2, shape_j_rot3, shape_j_rot4]))

        # shape_T
        shape_t_rot1 = np.array([[0, 2], [1, 2], [2, 2], [1, 1]], np.int32)
        shape_t_rot2 = np.array([[2, 0], [2, 1], [2, 2], [1, 1]], np.int32)
        shape_t_rot3 = np.array([[0, 1], [1, 1], [2, 1], [1, 2]], np.int32)
        shape_t_rot4 = np.array([[1, 0], [1, 1], [1, 2], [2, 1]], np.int32)
        shape_t = Shape(np.array([shape_t_rot1, shape_t_rot2, shape_t_rot3, shape_t_rot4]))

        return list([shape_i, shape_o, shape_s, shape_z, shape_t,shape_j, shape_l])

def generate_colours():
        RED=(255,0,0)
        ORANGE=(255,127,0)
        GREEN=(0,255,0)
        YELLOW=(255,255,0)
        BLUE=(0,0,255)
        OLIVE=(128,128,0)
        WHITE=(125,125,125)
        return list([WHITE,RED,ORANGE,GREEN,YELLOW,BLUE,OLIVE])
