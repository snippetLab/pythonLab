def try_recusrion(num) :
    if (num > 0) :
        result = num + try_recusrion(num - 1)
        print(result)
    else :
        result = 0
    return result;
print("Recursion Example");
try_recusrion(8);