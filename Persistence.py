number = int(input("Enter Your Number: "))
def persistence(per):
    count = 0
    total = 0 
    OG_Num = 0 
    numbers = []
    for i in len(str(per)):
        i.append(numbers)
    for s in int(numbers):
        if count == 0:
            count += 1 
        test = (s * count)
        if count == 1:
            count += (s - 1)
        else:
            count += test
    return (count) 

print (persistence(number))
        
         
        