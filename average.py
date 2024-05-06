#problem statement
#calculate the average in the numbers in the list
#now initialize the empty list
list=[]
#ask the input from the user
n=int(input("Enter the number of values do you want to store in the list:"))
#now initialize the sum variable as 0
sum=0
for i in range(n)
#now ask the input from the user
    numbers=int(input("Enter the numbers:"))
    #print(numbers[i])
    #now store all the number in the list
    list.append(numbers)
    #now sum all the numbers in to the list
    sum+=numbers
    #now calculate the average numbers
    average=sum/n
print(sum)
#now print the list
print(list)
#now print the average
print(average)