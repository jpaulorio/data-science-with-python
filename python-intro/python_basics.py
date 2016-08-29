#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
========================
Python3 básico
=======================
"""

# Tipos básicos...
an_integer = 2
a_float_number = 2.3
a_string = "Eu sou uma string"
another_string = 'Strings também podem usar aspas simples'
multiline_string = '''Strings podem ocupar
                      várias linhas'''

# Operações aritméticas
a, b = 2, 3
sum_ab = a + b
sub_ab = a - b
prod_ab = a * b
div_ab = a / b
pow_ab = a ** b
mod_ab = a % b

# Comparadores
a_greater_than_b = a > b
a_greater_than_or_equal_to_b = a >= b
a_less_than_b = a < b
a_less_than_or_equal_to_b = a <= b
a_equals_b = a == b
a_not_equals_b = a != b
is_a_none = a is None
is_a_not_none = a is not None
a_between_zero_and_b = 0 <= a <= b

# Operadores booleanos
and_example = a < b and a > 0
or_example = a < b or a > 0
not_example = not a < b

# Constantes booleanas
true_constant = True
false_constant = False

# Arrays e tuplas
an_array = [1, 2, 'a string']
a_tuple = (1, 2, 'a string')
first_array_element = an_array[0]
last_array_element = an_array[2]
first_tuple_element = a_tuple[0]
last_tuple_element = a_tuple[2]
array_length = len(an_array)
tuple_length = len(a_tuple)

# Adição de elementos a arrays
an_array.append(3)
array_with_new_elements = an_array + [4, 5]

# Dicionários
a_dict = {'key1': 1, 'key2': 'value2'}
value1_from_dict = a_dict['key1']

# Adição de elementos a um dicionário
a_dict['key3'] = 3

# Interpolação de strings
name = 'Fulana'
greeting = 'Oi, eu sou a {}'.format(name)
another_greeting ='Oi, eu sou a {nome}.'.format(nome=name)

# Condicionais
if a < b:
    print('{} é menor do que {}'.format(a, b))
elif a == b:
    print('{} é igual a {}'.format(a, b))
else:
    print('{} é maior do que {}'.format(a, b))

# Laços e iterações
for i in range(10):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(2, 10):
    print(i)

for array_element in an_array:
    print(array_element)

for key in a_dict:
    print(key)

for key, value in a_dict.items():
    print('{}: {}'.format(key, value))

# Funções
def my_function(arg1, arg2=5):
    return 'Recebidos argumentos {} e {}'.format(arg1, arg2)

print(my_function(3))
print(my_function(arg1=4))

# List comprehensions
powers_of_two = [2 ** i for i in range(10)]
even_powers_of_two = [2 ** i for i in range(10) if i % 2 == 0]
