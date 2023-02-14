#Logical Operators (and, or, not) = used to check if two or more conditional statements are true

temp = int(input("What is the temp outside: "))

if not(temp >= 0 and temp <= 30): #both conditions must be true #not turns true into false and fasle into true-2
    print("The temp is great")
    print("Stay inside ya nasty")
elif temp < 0 or temp > 30:
    print("The temp is cold as fuck")
    print("Get yo ass outside")