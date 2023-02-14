#User Input

name = input("What is your name: ") #no need for data type
age = int(input("How old are you: ")) #data type float/int since inputting number
height = float(input("How tall are you: "))

print("Hello " + name)
print("You are " + str(age) + " years old") #convert float/int number back to string
print("You are " + str(height) + "cm tall")