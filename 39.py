#A program to add two matrices
#Ze function to add two matrices
def add_matrices(mat1, mat2):
    #Check if dimensions match
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices have the same dimensions for addition"
    
    #Initilize empty result matrix with same dimensions
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result

#Input matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

#Call the add matrices function
result_matrix = add_matrices(matrix1, matrix2)

#Display the result
if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Sum of matrices:")
    for row in result_matrix:
        print(row)
    