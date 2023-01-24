def rotate_ring(matrix, offset):
    dim = len(matrix[0])
    last_element = matrix[offset][offset]
    for j in range(1+offset, dim-offset):
        matrix[offset][j-1] = matrix[offset][j]
    matrix[offset][dim-1-offset] = matrix[1+offset][dim-1-offset]
    for i in range(1+offset, dim-offset):
        matrix[i-1][dim-1-offset] = matrix[i][dim-1-offset]
    matrix[dim-1-offset][dim-1-offset] = matrix[dim-1-offset][dim-2-offset]
    for j in range(1+offset, dim-offset):
        matrix[dim-1-offset][dim-j] = matrix[dim-1-offset][dim-j-1]
    matrix[dim-1-offset][offset] = matrix[dim-2-offset][offset]
    for i in range(1+offset, dim-offset):
        matrix[dim-i][offset] = matrix[dim-i-1][offset]
    matrix[1+offset][offset] = last_element

def rotate_matrix(matrix):#matrix to be given to this function
    dim = len(matrix[0])
    for offset in range(0, int(dim/2)):
        rotate_ring(matrix, offset)

mat=[['a','b','c'],['d','e','f'],['g','h','i']]
rotate_matrix(mat)
import numpy as np
print(np.array(mat))