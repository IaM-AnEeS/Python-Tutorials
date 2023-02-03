# EXERCISE2
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
print("0->For Addition\n1->For Subtraction\n2->For Multiplication\n3->Division\n4->For Modolus")
user_choice=int(input("Enter the number"))
if(user_choice==2 and num1==45 and num2==3):
    Mul=num1*num2+420
    print(num1,"*",num2,"=",Mul)
if(user_choice==0 and num1==56 and num2==9):
    sum=num1+num2+12
    print(num1,"+",num2,"=",sum)
if(user_choice==3 and num1==56 and num2==6):
    Div=56/6-5
    print(num1,"/",num2,"=",Div)
if(user_choice==0):
    sum=num1+num2
    print(num1," + ",num2,"=",sum)
elif(user_choice==1):
    Sub=num1-num2
    print(num1," - ",num2,"=",Sub)
elif(user_choice==2):
    Mul=num1*num2
    print(num1," * ",num2,"=",Mul)
elif(user_choice==2):
    Div=num1/num2
    print(num1," / ",num2,"=",Div)
elif(user_choice==3):
    Mod=num1%num2
    print(num1," % ",num2,"=",Mod)
