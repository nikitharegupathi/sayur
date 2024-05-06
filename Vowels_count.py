#Count the vowels['a','e','i'.'o','u'] in the given string
# get the input from the user
string=input("Enter the input string:")
#now initialize the count variable
count=0
#use for loop to run till the length of the string
for i in string:
    #check if the string has the vowels 
    if(i=='a') or (i=='e') or (i=='o') or (i=='i') or (i=='u'):
        # if the string has the vowels count the each vowel char
        count+=1
        #then finally print the total count
print(count)