import math 
triangle = int(input("\nThis program will find the missing angle using SOHCAHTOA\nWhat are you solving for (Hypotenuse(1),adjacent(2),opposite(3),missing angle(4)): "))
decimal_place = int(input("How Many decimal places would you like? : "))
if triangle == 1 :
    abc = input("What letter is your angle (c being the right angle and counting backwards from left to right): ")
    angle1 = float(input("Enter Your Angle value: "))
    type1 = int(input("What do you have:(adjacent(1),opposite(2)): "))
    side1 = float(input("Enter Your Side value: "))
    if abc == "a" or abc == "A" and type1 == 1 :
        part1 = (math.cos(math.radians(angle1)))
        part2 = (side1/part1)
        rounding = round(part2,decimal_place)
        print (("The Hypotenuse is %s ") %(rounding))
    if abc == "b" or abc == "B" and type1 == 1:
        part1 = (math.sin(math.radians(angle1)))
        part2 = (side1/part1)
        rounding = round (part2,decimal_place)
        print (("The Hypotenuse is %s")%(rounding))
    if abc == "a" or abc == "A" and type1 == 2 :
        part1 = (math.sin(math.radians(angle1)))
        part2 = (side1/part1)
        rounding = round(part2,decimal_place)
        print (("The Hypotenuse is %s ") %(rounding))
    if abc == "b" or abc == "B" and type1 == 2:
        part1 = (math.cos(math.radians(angle1)))
        part2 = (side1/part1)
        rounding = round(part2,decimal_place)
        print (("The Hypotenuse is %s ") %(rounding))
    if abc == "c" or abc == "C":
        print ("You will not get the answer with this.")
if triangle == 2: 
    abc = input("What letter is your angle (c being the right angle and counting backwards from left to right): ")
    angle1 = float(input("Enter Your Angle value: "))
    type1 = int(input("What do you have:(Hypotenuse(1),opposite(2)): "))
    side1 = float(input("Enter Your Side value: "))
    if abc == "a" or abc == "A" and type1 == 1:
        part1 = (math.cos(math.radians(angle1)))
        part2 = (part1*side1)
        rounding = round(part2,decimal_place)
        print (("The Adjacent is %s ") %(rounding))
    if abc == "a" or abc == "A" and type == 2:
        part1 = (math.tan(math.radians(angle1)))
        part2 = (side1/part1)
        rounding = round(part2,decimal_place)
        print (("The Adjacent is %s ") %(rounding))
    if abc == "b" or abc == "B" and type1 == 1:
        part1 = (math.sin(math.radians(angle1))) 
        part2 = (part1*side1)
        rounding = round(part2,decimal_place)
        print (("The Adjacent is %s ")%(rounding))
    if abc == "B" or abc == "b" and type1 == 2:
        part1 = (math.tan(math.radians(angle1)))
        part2 = (part1*side1)
        rounding = round(part2,decimal_place)
        print (("The Adjacent is %s ")%(rounding))
    if abc == "c" or abc == "C":
        print ("You will not get the answer with this.")
if triangle == 3:
    abc = input("What letter is your angle (c being the right angle and counting backwards from left to right): ")
    angle1 = float(input("Enter Your Angle value: "))
    type1 = int(input("What do you have:(Hypotenuse(1),adjacent(2)): "))
    side1 = float(input("Enter Your Side value: "))
    if abc == "b" or abc == "B" and type1 == 1:
        part1 = (math.cos(math.radians(angle1)))
        part2 = (part1*side1)
        rounding = round(part2,decimal_place)
        print (("The Opposite is %s ")%(rounding))
    if abc == "a" or abc == "A" and type1 == 1: 
        part1 = (math.sin(math.radians(angle1)))
        part2 = (part1*side1)
        rounding = round(part2,decimal_place)
        print (("The Opposite is %s ")%(rounding))
    if abc == "a" or abc == "A" and type1 == 2:
        part1 = (math.tan(math.radians(angle1)))
        part2 = (side1*part1)
        rounding = round(part2,decimal_place)
        print (("The Opposite is %s ")%(rounding))
    if abc == "b" or abc == "B" and type1 == 2:
        part1 = (math.tan(math.radians(angle1)))
        part2 = (side1/part1)
        rounding = round(part2,decimal_place)
        print (("The Opposite is %s ")%(rounding))
    if abc == "c" or abc == "C":
        print ("You will not get the answer with this.")
if triangle == 4:
    abc = input("Enter Your missing angle (a or b)(c being the right angle and counting backwards from left to right):")
    type1 = int(input("Which side values are known (Opposite(1), Hypotenuse(2),Adjacent(3) : "))
    if type1 == 1:
        type2 = int(input("Which side values are known (Hypotenuse(1), Adjacent(2)): "))
        if type2 == 2: 
            side1 = int(input("Enter Your Value for Your Opposite: "))
            side2 = int(input("Enter Your Value for Your Adjacent: "))
            if abc == "a" or abc == "A":
                part1 = (side1/side2)
                part2 = math.degrees(math.atan(part1))
                rounding = round(part2,decimal_place)
                print (("The Missing angle is %s ")%(rounding))
            if abc == "b" or abc == "B":
                part1 = (side1/side2)
                part2 = math.degrees(math.atan(part1))
                rounding = round(part2,decimal_place)
                print (("The Missing angle is %s ")%(rounding))
        if type2 == 1:
            side1 = int(input("Enter Your Value for Your Opposite: "))
            side2 = int(input("Enter Your Value for Your Hypotenuse: "))
            if abc == "a" or abc == 'A':
                part1 = (side1/side2)
                part2 = math.degrees(math.acos(part1))
                rounding = round(part2,decimal_place)
                print (("The Missing angle is %s ")%(rounding))
            if abc == "b" or abc == 'B':
                part1 = (side1/side2)
                part2 = math.degrees(math.acos(part1))
                rounding = round(part2,decimal_place)
                print (("The Missing angle is %s ")%(rounding))
            if side1 >= side2:
                print("It won't Work, Hypotenuse is longer or the same size as the opposite.")
        if type2 >= 3:
            print ("Invalid")
    if type1 == 2:
        type2 = int(input("Which Side values are known (Opposite(1),Adjacent(2)): "))
        if type2 == 2:
            side1 = int(input("Enter Your Value for Your Adjacent: "))
            side2 = int(input("Enter Your Value for Your Hypotenuse: "))
            if abc == "a" or abc == "A":
                part1 = (side1/side2)
                part2 = math.degrees(math.asin(part1))
                rounding = round(part2,decimal_place)
                print (("The Missing angle is %s ")%(rounding)) 
            if abc == "b" or abc == "B":
                part1 = (side1/side2)
                part2 = math.degrees(math.asin(part1))
                rounding = round(part2,decimal_place)
                print (("The Missing angle is %s ")%(rounding))
        if type2 == 1:
            side1 = int(input("Enter Your Value for Your Opposite: "))
            side2 = int(input("Enter Your Value for Your Hypotenuse: "))
            if abc == "a" or abc == "A":
                part1 = (side1/side2)
                part2 = math.degrees(math.acos(part1))
                rounding = round(part2,decimal_place)
                print (("The Missing angle is %s ")%(rounding)) 
            if abc == "b" or abc == 'B':
                part1 = (side1/side2)
                part2 = math.degrees(math.acos(part1))
                rounding = round(part2,decimal_place)
                print (("The Missing angle is %s ")%(rounding))
        if type2 >= 3:
            print ("Invalid")
    if type1 == 3:
        type2 = int(input("Which Side values are known (Hypotenuse(1),Opposite(2)): "))
        if type2 == 1:
            side1 = int(input("Enter Your Value for Your Adjacent: "))
            side2 = int(input("Enter Your Value for Your Hypotenuse: "))
            if abc == "a" or abc == "A":
                part1 = (side1/side2)
                part2 = math.degrees(math.asin(part1))
                rounding = round(part2,decimal_place)
                print (("The Missing angle is %s ")%(rounding)) 
            if abc == "b" or abc == "B":
                part1 = (side1/side2)
                part2 = math.degrees(math.asin(part1))
                rounding = round(part2,decimal_place)
                print (("The Missing angle is %s ")%(rounding))
        if type2 == 2:
            side1 = int(input("Enter Your Value for Your Opposite: "))
            side2 = int(input("Enter Your Value for Your Adjacent: "))
            if abc == "a" or abc == "A":
                part1 = (side1/side2)
                part2 = math.degrees(math.atan(part1))
                rounding = round(part2,decimal_place)
                print (("The Missing angle is %s ")%(rounding))
            if abc == "b" or abc == "B":
                part1 = (side1/side2)
                part2 = math.degrees(math.atan(part1))
                rounding = round(part2,decimal_place)
                print (("The Missing angle is %s ")%(rounding))
        if type2 >= 3:
            print ("Invalid")
if triangle >= 5:
    print ("Invalid") 