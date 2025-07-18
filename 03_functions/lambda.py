# xNum = lambda numOne : numOne + 8;
# print(xNum(13));

# xNum = lambda numOne, numTwo : numOne * numTwo;
# print(xNum(3, 11));

def myFunc(n) :
    return lambda num : n * num;
numDouble = myFunc(2);
print(numDouble(13));