#to swap the two numbers
#ask num1 and num2 input from the user
num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
#now print the number1 and number2 before swapping
print("Before swapping")
print(num1)
print(num2)
#now create a temporary variable to store the num1
temp=0
#now swap the numberss
temp=num1 #store the number1 in the temp 
num1=num2 # store the number2 in the number1
num2=temp #store the temp value in the number2
#now print the numbers
print("After Swapping")
print(num1)
print(num2)