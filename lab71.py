import math

def bubble_sort_columns(matrix):
    """
    Сортує кожен стовпець матриці за зростанням методом обміну.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    for col in range(cols):
        for i in range(rows - 1):
            for j in range(rows - 1 - i):
                if matrix[j][col] > matrix[j + 1][col]:
                    matrix[j][col], matrix[j + 1][col] = matrix[j + 1][col], matrix[j][col]

    return matrix


def geometric_mean(row):
    """
    Обчислює середнє геометричне значень рядка.
    Враховується модуль чисел, щоб уникнути проблем з від'ємними значеннями.
    """
    product = 1
    for x in row:
        product *= abs(x)   
    return product ** (1 / len(row))


def arithmetic_mean(f_values):
    """
    Обчислює середнє арифметичне списку чисел.
    """
    return sum(f_values) / len(f_values)


A = [
    [66, 21, -3, -1, 90],
    [1, 74, -2, 80, -1],
    [10, 30, 20, -50, 91],
    [2, 4, 5, 81, 0],
    [33, 69, -5, 51, 24]
]

if __name__ == "__main__":
    print("Початкова матриця:")
    for row in matrix:
        print(row)

    bubble_sort_columns(matrix)

    print("Матриця після сортування стовпців:")
    for row in matrix:
        print(row)

    f_values = [geometric_mean(row) for row in matrix]

    print("Середні геометричні значення рядків:")
    for i, value in enumerate(f_values, start=1):
        print(f"f({i}) = {value}")

    F_value = arithmetic_mean(f_values)
    print("Середнє арифметичне значень f(i):", F_value)
