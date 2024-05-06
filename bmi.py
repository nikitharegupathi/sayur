#Ask the input weight from the user
weight=float(input("Enter the weight of the person:"))
#Ask the input height from the user
height=int(input("Enter the height of the person:"))
#now convert the height in centimeter to height in meter
if(weight>0 and height>0) :
	height_meter=float(height/100)#now calculate the square value of the height
	sqr_height=float(height_meter*height_meter)#now calculate the bmi value
	cal=float(weight/sqr_height)#now round off the bmi value
	bmi=round(cal,2)
else:
 	print("Enter the valid weight and height")
#check the bmi value is less than 18.5
if(bmi<18.5):
	print(f"Your bmi is {bmi},you are underweight")
#check the bmi value is between 18.5 -24.9
elif(bmi>=18.5 and bmi<=24.9):
	print(f"your bmi is {bmi},you have a normal bmi range")
#check the bmi value is between 25 -29.9
elif(bmi>25 and bmi<=29.9):
		print(f"your bmi is {bmi}, you are overweight")
#check the bmi value is greater than 30.0
elif(bmi>30.0):
	print(f"your bmi is {bmi} ,you have obese bmi range")