import numpy as np

array = [
    "tom",
    "tom",
    '0',
    '0'
]
#1
my_array = np.array(array)
my_string = np.array2string(my_array)

print(my_string)

#2
my_string = ', '.join(array)
print(my_string)
