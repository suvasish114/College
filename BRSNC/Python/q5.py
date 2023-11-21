# Write a program to calculate the sum of two compatible matrices A and B.
'''
INPUT : two matrix A and B
OUTPUT : resultent matrix C
DATA STRUCTURE : three list of lists A,B,C to store three matrix
ALGORITHM :
1. INPUT : r,c  // row and column of the matrix
2. INPUT : matrix A, matrix B   // user input of matrix A and B
3. SET : matrix C[i][j] : matrix A[i][j] + matrix B[i][j]   // i and j is row and column strts from 0 to r and c 
4. PRINT( matrix C).
5. STOP.
'''

r, c = map(int, input("Enter the row and column of the matrix: ").split())
A, B, C = [], [], []
print("Enter values in 1st matrix -")
for a in range(r):
    temp = []
    for b in range(c):
        temp.append(int(input("Row %d Column %d : " % (a+1, b+1))))
    A.append(temp)

print("Enter values in 2nd matrix -")
for a in range(r):
    temp = []
    for b in range(c):
        temp.append(int(input("Row %d Column %d : " % (a+1, b+1))))
    B.append(temp)
for a in range(r):
    temp = []
    for b in range(c):
        temp.append(A[a][b]+B[a][b])
    C.append(temp)

print("MATRIX 1 -")
for a in range(r):
    for b in range(c):
        print("%d" % A[a][b], end=" ")
    print('\n')

print("MATRIX 2 -")
for a in range(r):
    for b in range(c):
        print("%d" % B[a][b], end=" ")
    print('\n')

print("MATRIX 1 + MATRIX 2")
for a in range(r):
    for b in range(c):
        print("%d" % C[a][b], end=" ")
    print('\n')
