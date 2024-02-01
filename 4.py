#Get the type
x = 1
print (type(x))

z = 5.5
print(type(z))

name = "Judy"
print(type(name))

nameConf =  True
print(type (nameConf))

#Get an input
name = input("What's your name?")
print("Your name is", name)

country = input("Kenya")
print("Is a wonderful country", country)

#user defined functions
#Define a function

def multiplyFunc(x):
    result= x * x
    return result

print(multiplyFunc(9))
