list=[]
n=int(input("Enter the number of values do you want to store in the list:"))
sum=0
for i in range(n):
    numbers=int(input("Enter the numbers:"))
    #print(numbers[i])
    list.append(numbers)
    sum+=numbers
    average=sum/n
print(sum)
print(list)
print(average)
temp=0
for i in range(1,len(list),1):
    for j in range(i+1,len(list),1):
        temp=list[0]
        if(list[i]<list[j]):
            temp=list[j]
print(temp)