print("Guessing Number Game:")
count=0
val=0
guess_num=10
while val!=guess_num:
    val=int(input("Enter The Number:"))
    if val>guess_num:
        print("Too High")
        count+=1
    elif val<guess_num:
        print("Too Low")
        count+=1
    else:
        print("Yes,Your are Correct")
        count+=1
print("User Attempt:",count)

    




        
 




      

