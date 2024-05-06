#get an  input string from the user. add a space at every 3rd character
#example: abcdefg, output: ab cd ef g
#no get the input string from the user
string=input("enter the input string :")
#now initalize the count value as 0
count=0
# then initialize a empty set
newstring=" "
for i in string:
    newstring+=string[i:i+2]
    newstring+=" "
    i+=2
#now add all chars
newstring=newstring+inputstring[i:]
print(newstring)