#Avg until Enter Zero
sum=0
count=0
avg=0
num=int(input("Enter the Number:"))
while num!=0:
   sum+=num
   count+=1
   avg=sum//count
print(f'The count of the Numbers is {count}')
print(f'The sum of the Numbers is {sum}')
print(f'The average of the Numbers is {avg}')
