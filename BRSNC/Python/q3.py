# Write a program to find sum of the following series for n ns: 1 – 2/2! + 3/3! - - - - - n/n!
'''
INPUT: number of termes in the series.
OUTPUT: sum of the series.
DATA STRUCTURE : a variable 'term' to store the user input, and a variable 'sum' to store the result.
ALGORITHM: 
1. STRAT.
2. INPUT(term)  // user input stored in 'term'
3. Repeat step 3 to 5 until term>0.
4.  If term%2 != 0: Then
    SET: sum = sum + term/ factorial(term)  // factorial() is a function to return the factorial 
5.  Else :
    sum = sum - term/factorial(term)
6. STOP.
'''

def factorial(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact

term = int(input("Enter number of terms in the series: "))
sum = 0
while term > 0:
    if term%2 != 0:
        sum += term/factorial(term)
    else:
        sum -= term/factorial(term)
    term -= 1
print("The Sum of the series is: ",sum)
