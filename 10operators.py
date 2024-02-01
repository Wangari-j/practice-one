#comparison operators
x = 2
y = 4
print(x == y)
print (x != y)
print (x <= y)

#logical operators

print(x<3 and x<5)
print(x<1 and x<5)

print(not True)
print(not False)
print(not(x<3 and x<9))

#additional operators
list1 = ["fig", "cherry"]
list2 = ["fig", "cherry"]
list3 = list2
print(list1 is list2)
print(list2 is list3)
print(list2 is not list3)
print("cherry" in list1)
print ("apple" in list3)
print("apple" is not list1)

#conditional statements
x = 22
y = 100

if y < x:
    print("This is True, y is not greater than x")
elif y > x:
    print("This is True, y is greater than x!")
else:
    print("Anything else!")
print("completed")

