# Write a menu-driven program, using user-defined functions to find the area of rectangle, square,
# circle and triangle by accepting suitable input paramters from user.
'''
INPUT: user choice from rectangle, square, circle, triangle and input data as requered.
OUTPUT: area of the given shape.
DATA STRUCTURE: variable 'choice' to make choice from the list, and variable a,b,r,h as requred.
ALGORITHM: 
1. START.
2. INPUT: choice    //show a suitable list, and ask user to enter choice.
3. Repeat step 2 to 7 until user want to exit.
4.  If choice == 1: Then
    INPUT: a    //length of rectangle.
    INPUT: b    //width of rectangle.
    PRINT(a*b)  //area of rectangle

5.  If choice == 2: Then
    INPUT: r    // side of square.
    PRINT(r*r)  //area of square

6.  If choice == 3: Then 
    INPUT: r    // redius of circle
    PRINT(3.14*r*r)     // area of circle

7.  If choice == 4: Then
    INPUT: b    // base of triangle 
    INPUT: h    // height of triangle 
    PRINT((h*b)/2)  // area of triangle 

8. STOP.
'''


while True:
    choice = int(input('''Enter your choice from below list: 
----------------------------------
1. press 1 to find area of rectangle.
2. press 2 to find area of square.
3. press 3 to find area of circle.
4. press 4 to find area of triangle.
5. press any other key to exit.
'''))

    if choice == 1:  # for rectangle
        a = float(input("Enter the length of rectangle: "))
        b = float(input("Enter the width of rectangle: "))
        print("The area of rectangle is: %g" % (a*b))
    elif choice == 2:  # for square
        r = float(input("Enter the side of square: "))
        print("The area of square is: %g" % (r*r))
    elif choice == 3:  # for circle
        r = float(input("Enter the redius of circle: "))
        print("The area of circle is: %g" % (3.14*r*r))
    elif choice == 4:  # for triangle
        b = float(input("Enter the base of triangle: "))
        h = float(input("Enter the height of triangle: "))
        print("The area of triangle is: %g" % ((h*b)/2))
    else:
        break
