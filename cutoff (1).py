#Ask the subject1 mark input from the user
subject1=int(input("Enter the mark in subject1:"))
#Ask the subject2 mark input from the user
subject2=int(input("Enter the mark obtained in subject2:"))
#Ask the subject3 mark input from the user
subject3=int(input("Enter the mark obtained in subject3:"))
#Ask the subject4 mark input from the user
subject4=int(input("Enter the mark obtained in subject4:"))
#Ask the subject5 mark input from the user
subject5=int(input("Enter the mark obtained in subject5:"))
#check if the user give the valid mark 
if((subject1>0 and subject2>0 and subject3>0 and subject4>0 and subject4>0))and((subject1<=100 and subject2<=100 and subject3<=100 and subject4<=100 and subject5<=100)):
  #calculate the total mark of the student
  total=float(subject1+subject2+subject3+subject4+subject5)
  #calcuate the average mark of the student
  average=float((total/500)*100)
  #check if the average cutoff is greater than or equal to 93 and less than 97
  if(average>=93 and average<97):
    print(f"Student's average is {average} % , the student is eligible for admission in college-1 and college-2")
  #check if the average cutoff is greater than or equal to 97
  elif(average>=97):
    print(f"student's average is {average} %, the student is eligible for admission in college-3")
  #check if the average is greater than or equal to 89
  elif(average>=89):
    print(f"student's average is {average} %, the student is eligible for admission in college-2")
#if the user did not enter the correct mark than give notify to the user  
else:
  print("Enter the valid mark of the students")