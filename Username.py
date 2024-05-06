#to print the user name and age
#aask name from the user
name=input("Enter the users name:")
#ask users birth age
birth_year=int(input("Enter the users birth age:"))
#ask the users current age
current_year=int(input("Enter the current_year:"))
if(birth_year>=1920 and birth_year<=2024):
  print("'Hello'",name)
  print(f"'you are {current_year-birth_year} years old'")