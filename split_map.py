# A, B, C = map(int, input("Enter 3 numbers: ").split())
# print(A, B, C)



# EXAMPLE WITH INTEGERS

# A, B = map(int, input("Enter two numbers: ").split())
# C, D, E = map(int, input("Enter three numbers: ").split())
# F, G, H, I = map(int, input("Enter four numbers:").split())

# print(A, B, C, D, E, F, G, H, I)


# EAMPLE WITH STRINGS

# A, B = input("Enter two words: ").split()
# C, D, E = input("Enter three words: ").split()
# F, G, H, I = input("Enter four words: ").split()
# print(A, B, C, D, E, F, G, H, I)



# CODECHEF EXAMPLE

# t = int(input("Number of test cases: "))

# for i in range(t):
#     A, B = map(int, input("Enter two numbers: ").split())
#     C, D, E = map(int, input("Enter three numbers: ").split())
#     print(A, B, C, D, E)
    


# CODECHEF EXAMPLE

t = int(input("Enter the number of test cases: "))

for i in range(t):
    A, B = map(int, input("Enter two numbers: ").split())
    C = input("Enter a word: ")
    print(A, B, C)