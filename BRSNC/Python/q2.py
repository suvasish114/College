# Write a program to display the first n terms of Fibonacci series.
'''
INPUT : a number to print fibonacci series upto it.
OUTPUT : fibonacci series of the given number.
DATA STRUCTURE : variable 'n' to store user input, variable 'a' to store the resultant values.

ALGORITHM :
1. START.
2. INPUT(n)	// store user input into variable n
3. SET: a=0
   SET: b=1
4. Repeat step 4 and 5 until a>n
5. PRINT(a)
   SET: f=a+b
   SET: a=b
   SET: b=f
'''

n = int(input('Enter the number : '))
count,a,b = 0,0,1
print('The fibonacci series upto given number is :', end=" ")
while True: 
    print(a, end=" ")
    f = a+b 
    a = b 
    b = f 
    if a>n :
        break
print('\n')
