def multiplyFunc(x):
    result = x * x
    return result

print (multiplyFunc(5))

#call the function
print(multiplyFunc(3))
print (multiplyFunc(9))


def multiplyxyfunc(x,y):
    result = x * y
    return result
print(multiplyxyfunc(5,6))

print (multiplyxyfunc (7,3))


def multiplytFunc(t):
    result = t * t
    return result

print (multiplytFunc(9))


def multiplywzFunc(w,z):
    result = w % z
    return result

print (multiplywzFunc(4,3))

#return many values
def multiplyyxyFunc (x,y):
    multiply = x * y
    sum = x + y
    divide = x/y
    return multiply, sum, divide

def multiplyzzzFunc (f,g):
    multiply = f * g
    sum = f + g
    divide = f/g
    return multiply, sum, divide
