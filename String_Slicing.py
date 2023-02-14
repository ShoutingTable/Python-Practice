#String Slicing = create a substring by extracting elements from another string indexing[] or slice() [start:stop:step]

#Indexing
# name = "Bob Todd"

# first_name = name[:3] #no value for start and step 
# last_name = name[4:] #[start at 4 = B, stop at 8 =  , step is = 1]
# funky_name = name[::2]
# reversed_name = name[::-1]

# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)


#Slicing
website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)


print(website1[slice])
print(website2[slice])