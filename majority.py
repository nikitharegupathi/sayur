# Python Program to Find the Majority Element

# Create a empty list 
list=[]
count=0
major=0
# Now initalize the k value to find the majority element
k=2
majority=[]
n=int(input("Enter the range:"))
#Get the input value from the user
for i in range(n):
    num=int(input("Enter the number:"))
    #now store the number in to the list
    list.append(num)
# Create a empty dictionary
count_dict = {}
for i in range(n):
    if list[i] in count_dict:
        count_dict[list[i]] += 1
    else:
        count_dict[list[i]]=1
majority = []
for key_value in count_dict:
    if count_dict[key_value] > k:
        majority.append(key_value)
print(majority)
        
            