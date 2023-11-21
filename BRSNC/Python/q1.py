'''
INPUT: A number to factorial.
OUTPUT: Print the factorial of that number or suitable error message.
DATA STRUCTURE: a variable 'a' to hold the user input and another variable 'factorial' to hold the desire result.

ALGORITHM:

1. START
2. INPUT(a) // a is a variable to hold user input
3. IF a<0 THEN:
	print FACTORIAL IS NOT POSSIBLE
4. ELSE :
'''

a = int(input("Enter the number you want to factorial:"))
factorial = 1
if a<0 :
	print("The number is less than 0. factorial is not possible")
else:
	for b in range(a):
		factorial = factorial * a
		a = a-1
	print("The factorial of given number is : %g" %factorial)
