class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        return 'Матрица:\n' + '\n'.join('\t'.join(map(str, line)) for line in self.my_matrix)

    def __add__(self, other):
        result = [[self.my_matrix[i][j] + other.my_matrix[i][j] for j in range(len(self.my_matrix[0]))]
                  for i in range(len(self.my_matrix))]
        return result


matrix_1 = [
    [2, 3],
    [4, 5],
    [6, 7],
]

matrix_2 = [
    [7, 8],
    [10, 9],
    [11, 13],
]

a = Matrix(matrix_1)
print(a)
b = Matrix(matrix_2)
print(b)
c = Matrix(a + b)
print(c)
