#Ask the mark1 input of the student from the user
mark1=int(input("Enter the mark1 of the student:"))
#Ask the mark2 input  of the student from the user
mark2=int(input("Enter the mark2 of the student:"))
#ask the mark3 input of the student from the user
mark3=int(input("Enter the mark3 of the student:"))
#check if the user give the valid mark
if(mark1 and mark2 and mark3 >0):
#check if anyone of the mark is equal to 100
	if(mark1==100 or mark2==100 or mark3==100):
		print("Grade is A")
#check if anyone of the mark is greater than or equal to 90
	elif(mark1>=90 or mark2>=90 or mark3>=90):
		print("Grade is B")
#check if anyone of the mark is greater than or equal to 60
	elif(mark1>=60 or mark2>=60 or mark3>=60):
		print("Grade is C")
#check if anyone of the mark is 50 or less
	elif(mark1<=50 or mark2<=50 or mark3<=50):
		print("Grade is F")
	else:
		print("Grade is D")
#else give the instruction to give valid marks
else:
	print("Enter the correct mark of the student:")