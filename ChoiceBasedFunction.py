choice=0
while choice!=3:
    print("Enter 1 for Odd/Even")
    print("Enter 2 for Positive/Negative/Zero")
    print("Enter 3 for Exit")
    choice=int(input("Enter the Choice:"))
    if choice==1:
        num=int(input("Enter the Number:"))
        if(num%2==0):
            print(f'The number {num} is ODD')
        else:
            print(f'The number {num} is EVEN')
    elif choice==2:
        num=int(input("Enter the Number:"))
        if num>0:
            print(f'The number {num} is positive')
        elif num<0:
            print(f'The number {num} is Negative')
        else:
            print(f'The number {num} is Zero')
    elif choice==3:
        print("Exit")
    else:
        print("Invalid Choice")
