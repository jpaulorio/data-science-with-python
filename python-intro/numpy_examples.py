#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np


"""
==========================
Exemplos de Numpy
==========================
"""

# Criação de arrays
array_a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
array_b = np.array(range(9))
all_zeros = np.zeros(9)
all_ones = np.ones(9)
random_ints_array = np.random.randint(0, 10, size=9)
random_array_from_normal_distribution = np.random.randn(9)

# Indexação de arrays
first_element = array_a[0]
last_element = array_a[8] or array_a[-1]
elements_starting_from_second = array_a[1:]
elements_from_second_to_fifth = array_a[1:6]
every_second_element = array_a[0::2]
every_second_element_until_sixth= array_a[0:7:2]

# Arrays bidimensionais(matrizes)
matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
all_zeros_matrix = np.zeros((9, 9))
all_ones_matrix= np.ones((9, 9))
random_ints_matrix = np.random.randint(0, 10, size=(9, 9))
random_matrix_from_normal_distribution = np.random.randn(9, 9)

# Indexação de arrays bidimensionais
top_left_element = matrix_a[0, 0]
bottom_right_element = matrix_a[1, 2]
first_row_elements = matrix_a[0, :]
first_column_elements = matrix_a[:, 0]
first_and_second_columns = matrix_a[:, 0:2]

# Transformação de array em matriz
array_a_to_matrix = array_a.reshape(3, 3)

# Operações aritméticas entre arrays
pointwise_sum = matrix_a + matrix_b
pointwise_sub= matrix_a - matrix_b
pointwise_multiplication=  matrix_a * matrix_b
pointwise_division =  matrix_a / matrix_b
scalar_multiplication = 3 * matrix_a
scalar_power= matrix_a ** 2
matrix_transpose = matrix_a.transpose()
array_scalar_product = array_a.dot(array_b)
matrix_product = matrix_a.dot(matrix_b)
matrix_array_product = matrix_a.dot(array_a[0:3])

# Multiplicação matricial usando operador @ disponível a partir do Python 3.5
array_scalar_product = array_a @ array_b
matrix_product = matrix_a @ matrix_b
matrix_array_product = matrix_a @ array_a[0:3]

