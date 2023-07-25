def rotate(matrix):
        
        n = len(matrix)

        for i in range(n-1):
            for j in range(i+1,n):
                temp = matrix[i][j]
                matrix[i][j] =  matrix[j][i]
                matrix[j][i] = temp 
        for i in range(n):
            matrix[i].reverse()
a = [[1,2,3],[4,5,6],[7,8,9]]
print(a)
rotate(a)
print(a)