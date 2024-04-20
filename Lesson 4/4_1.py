# Урок 4. Функции

# 1. Напишите функцию для транспонирования матрицы


def transpose_matrix(mat):
    rows = len(mat)
    cols = len(mat[0])

    transposed = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = mat[i][j]

    return transposed

# Пример использования функции:
if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [4, 5, 6, 5],
        [7, 8, 9, 9],
        [1, 5, 6, 8]
    ]

    transposed_matrix = transpose_matrix(matrix)
    for row in transposed_matrix:
        print(row)