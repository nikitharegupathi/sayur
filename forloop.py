#Ask the input from the user how many they want to enter
n= int(input("Enter how many marks do you want to enter:"))
#now create a variable and give a initialize value as 0
total=0
#use for loop for run the loop n times
for i in range(1,n+1,1):
	#Ask the input from the user how much mark they obtained
	mark=int(input("Enter the mark you obtained in subject:"))
	#use if condition to check that they enter the correct mark 
	if(mark>0 and mark<=100):
		#now calculate the total mark that the students obtained in all subjects
		total+=mark
print(f"The total mark they obtained is {total}")
#now calculate the average mark 
total/=n
print(f"The average mark is {total}")