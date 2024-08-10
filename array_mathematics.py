import numpy as np

A, B = map(int, input().split())


array1 = np.array([list(map(int, input().split())) for _ in range(A)])


array2 = np.array([list(map(int, input().split())) for _ in range(A)])


addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
integer_division = np.floor_divide(array1, array2)  
modulus = array1 % array2
power = array1 ** array2


print(addition)
print(subtraction)
print(multiplication)
print(integer_division)
print(modulus)
print(power)



