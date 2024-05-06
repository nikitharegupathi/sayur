import string
#now get the input password from the user
input=input("Enter the password:").lower()
alpha_count=0
digit_count=0
special_count=0
total_count=0
#use for loop to check the conditions
for i in input:
	#check if the given password has char and find how many chars it have
	if i. isalpha():
		alpha_count+=1
	#check if the given password has digit and find how many digits it have
	if i.isdigit():
		digit_count+=1
	#check if the given password has special characteds and find how many digits it have
	if i in string.punctuation:
		special_count+=1
	#now find the length of the password
total_count=int(alpha_count+digit_count+special_count)
#check if the length of the password is greater than 8
if(total_count >=8):
			#if the password contains atleast 3 chars,2 numbers and one special character amd the length of the password is atleast 16-the password is very strong
			if(alpha_count>=3 and digit_count>=2 and special_count>=1 and total_count >=16):
				print("Your password is very strong")
		#if the password contains atleast 3 chars,2 numbers and 1 special character the password is strong
			elif(alpha_count>=3 and digit_count>=2 and special_count>=1):
				print("Your password is strong")
		#if the password contains atleast one char, atleast one number,atleast one special character the password is okay
			elif(alpha_count>=1 and digit_count>=1 and special_count>=1):
				print("your password is ok")
		#if the password is only alphabet or only numbera or only special character the password is weak
			elif ((i.isalpha()) or (i.isdigit()) or ((i in string.punctuation))):
				print("your password is weak")
else:
		print("enter valid password")