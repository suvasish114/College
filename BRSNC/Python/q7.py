# Write a menu driven program to convert the given temperature from Fahrenheit to Celsius and
# vice versa depending upon users choice.

'''
INPUT : tempareture in celsius or fahrenheit.
OUTPUT : converted tempareture in celsius or fahrenheit.
DATA STRUCTURE : a variable 'c' to store user input, and a variable 'result' to store resultant value.
ALGORITHM : 
1. START.
2. INPUT(c)     // ask user to enter the value
3. If n is in celsius : Then
        SET : result = (c*(9/5))+32
4. If n is in fahrenheit : Then
        SET : result = (c-32)*(5/9)
5. PRINT(result)
6. STOP
'''

c, result = 0,0.0
n = int(input("Enter tempareture :(to fahrenheit press 1, to celsius press 2):"))
if n == 1:
	c = float(input("Enter the tempareture in fahrenheit :"))
	result = (c-32)*(5/9)
	print("The result in celsius is: %g" %result)
else:
	c = float(input("Enter the tempareture in celsius:"))
	result = (c*(9/5))+32
	print("The result in fahrenheit is : %g" %result)

