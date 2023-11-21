# Write a program to calculate total marks, percentage and grade of a student. Marks obtained in
# each of the three subjects are to be input by the user. Assign grades according to the following
# criteria :
#	Grade A: Percentage >=80
#	Grade B: Percentage>=70 and <80
#	Grade C: Percentage>=60 and <70
#	Grade D: Percentage>=40 and <60
#	Grade E: Percentage<40

'''
INPUT : student markes of three subject.
OUTPUT : display students total markes percentage and grade
DATA STRUCTURE : variable 'P','C','M' to hold students markes, and a list 'result' to store students result.
ALGORITHM : 
1. START.
2. Repeat step 2 to 4 until user want to output result.
3. SET: P,C,M   // markes of each students physics, chemistry, and mathematics/
4. SET: result[i] = ['total markes', 'percentage', 'grade'] //'i' is student number.
5. PRINT(students number, total markes, percentage, grade)
6. STOP.
'''

def percentage(a):
    b = ''
    if a >= 80:
        b = 'A'
    elif a >= 70:
        b = 'B'
    elif a >= 60:
        b = 'C'
    elif a >= 40:
        b = 'D'
    else:
        b = 'E'
    return b


result = []   # empty list
loop_variable = True
while loop_variable:
    print("Enter the marks of the student - ")
    P = float(input("Physics : "))
    C = float(input("Chemistry : "))
    M = float(input("Mathematics : "))
    if (int(input("Press 1 to add student, press 2 to show result- ")) == 2):
        loop_variable = False
    R = (P+C+M)
    Q = percentage(R/3)
    result.append([R, R/3, Q])

print("The result of students are: ")
print("STUDENT NO \tTOTAL MARKS \tPERCENTAGE \tGRADE")
print("-----------------------------------------------------------------")
for a in range(len(result)):
    print("%d\t\t%.2f\t\t%.2f\t\t%s" %
          (a+1, result[a][0], result[a][1], result[a][2]))
