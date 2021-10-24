from math import sqrt




formula__list = ["1. Pythagorean Theorem", "2. Area of an object", "3. Perimeter of an object", "4. Quadratic Formula", ]


print("Welcome to Formula Calculator!")
print(*formula__list, sep="\n")

choice = input("Which formula would you like to choose? (Choose a number corresponding to formula, if you wish to quit type 'quit') ").lower()

while choice != "quit":
    if choice == "1":
        print("Pythagorean Theorem:")
        formula = input('Which side (a, b, c) do you wish to calculate? side> ')
        
        if formula == 'c':
        	side_a = float(input('Input the length of side a: '))
        	side_b = float(input('Input the length of side b: '))
        
        	side_c = sqrt(side_a * side_a + side_b * side_b)
        	
        	print('The length of side c is: ' )
        	print(side_c)
        
        elif formula == 'a':
            side_b = float(input('Input the length of side b: '))
            side_c = float(input('Input the length of side c: '))
            
            side_a = sqrt((side_c * side_c) - (side_b * side_b))
            
            print('The length of side a is' )
            print(side_a)
        
        elif formula == 'b':
            side_a = float(input('Input the length of side a: '))
            side_b = float(input('Input the length of side c: '))
                
            side_c = sqrt(side_c * side_c - side_a * side_a)
            
            print('The length of side b is')
            print(side_c)
        
        else:
        	print('Please select a side between a, b, c')
        	
    
    
    if choice == "4":
        print("Quadratic Formula: ")
        value_a = float(input('Input the value for a: '))
        value_b = float(input('Input the value for b: '))
        value_c = float(input('Input the value for c: '))
        
        if value_a == 0:
            print("a can not = 0!!!")
            value_a = float(input('Input the value for a: '))
        
        
        x1 = (-value_b + (sqrt((value_b**2) - (4 * value_a * value_c))))/ (2 * value_a)
        
        x2 = (-value_b - (sqrt((value_b**2) - (4 * value_a * value_c))))/ (2 * value_a)

        print("x = " + str(x1) + "\nx = " + str(x2))
        
    #Area of an object
    if choice == "2": 
        area_shape = input("Which shape would you like to use?(Square, Rectangle, Triangle) ").lower()
        if area_shape == 'square':
            side_a = float(input("Input the length of side a: "))
            
            area_of_square = side_a * side_a
            
            print("The area of the square is: ")
            print(area_of_square)
        
        if area_shape == 'rectangle':
            length = float(input("Input the length of the rectangle: "))
            width = float(input("Input the width of the rectangle: "))
            
            area_of_rectangle = length * width 
            
            print("The area of the rectangle is: ")
            print(area_of_rectangle)
    
        if area_shape == 'triangle':
            height = float(input("Input the height of the triangle: "))
            base = float(input("Input the base of the triangle: "))
            
            area_of_triangle = (height * base) * 0.5
            
            print("The area of the triangle is: ")
            print(area_of_triangle)
    ##############################################################################################################################################################################################################################################
    #Perimeter of an object
    if choice == "3": 
        perimeter_shape = input("Which shape would you like to use?(Square, Rectangle, Triangle) ").lower()
        if perimeter_shape == 'square':
            side_a = float(input("Input the length of side a: "))
            
            perimeter_of_square = side_a * 4
            
            print("The perimeter of the square is: ")
            print(perimeter_of_square)
        
        if perimeter_shape == 'rectangle':
            length = float(input("Input the length of the rectangle: "))
            width = float(input("Input the width of the rectangle: "))
            
            perimeter_of_rectangle = (length + width) * 2
            
            print("The perimeter of the rectangle is: ")
            print(perimeter_of_rectangle)
    
        if perimeter_shape == 'triangle':
            side1 = float(input("Input side 1 of the triangle: "))
            side2 = float(input("Input side 2 of the triangle: "))
            base = float(input("Input the base of the triangle: "))
            
            perimeter_of_triangle = side1 + side2 + base
            
            print("The perimeter of the triangle is: ")
            print(perimeter_of_triangle)    
   
   
    choice = input("Which formula would you like to choose? (Choose a number corresponding to formula, if you wish to quit type 'quit') ").lower()
    
    
   
        	