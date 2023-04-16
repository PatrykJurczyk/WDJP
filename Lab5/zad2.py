from random import random

matrix = [ [random() for y in range(4)] for x in range(4)]
diagonal = [ matrix[i][i] for i in range(4)]
print(matrix, diagonal, sep='\n')

