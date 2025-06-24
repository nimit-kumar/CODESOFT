a=int(input("enter the first number\n"))
b=int(input("enter the second number\n"))

x=int(input("for addition press 1\n""for subtraction press 2\n""for division press 3\n""for multiplication press 4\n"))

match x:
    case 1:
        print("your answer is",a+b)
    case 2:
        print("your answer is",a-b)
    case 3: 
        print("your answer is",a/b)
    case 4:
        print("your answer is",a*b)
    
