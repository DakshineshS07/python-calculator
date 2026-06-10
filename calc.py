def calculator():
    num1=int(input("enter 1st number:"))
    num2=int(input("enter 2nd number:"))
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    choice=int(input("enter your choice(1-4):"))
    if(choice==1):
        add=num1+num2
        print("addition:",add)
    elif(choice==2):
        sub=num1-num2
        print("subtraction:",sub)
    elif(choice==3):
        mul=num1*num2
        print("multiplication:",mul)
    else:
        div=num1/num2
        print("division:",div)
calculator()
        
