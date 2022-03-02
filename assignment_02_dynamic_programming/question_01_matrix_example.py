# Driver program to test above function
from assignment_02_dynamic_programming.matrix_chain_multiplication import MatrixChainOrder

arr = [10, 30, 5, 60, 10]
size = len(arr)
m, s = MatrixChainOrder(arr, size)

print("M MATRIX:")
m = [row[1:] for row in m[1:]]
for row in m:
    print(row)

print("S MATRIX:")
s = [row[1:] for row in s[1:]]
for row in s:
    print(row)

print("Minimum number of multiplications is " + str(m[0][-1]))