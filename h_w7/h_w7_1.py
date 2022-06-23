class Matrix():
    def __init__(self, *args):
        self.my_list = args

    def __str__(self):
        return '\n'.join('\t'.join(str(i) for i in row) for row in self.my_list)

    def __add__(self, other):
        result = [[self.my_list[i][j] + other.my_list[i][j] for j in
                   range(len(self.my_list[0]))] for i in range(len(self.my_list))]
        return '\n'.join('\t'.join(str(i) for i in row) for row in result)



m = Matrix([1,2,3], [5,6,7])
m1 = Matrix([3,2,1], [1,2,3])
print(m,'\n')
print(m1, '\n')
print(m + m1)