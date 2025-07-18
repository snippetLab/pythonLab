# def empFunc() :
#     empName = "Jack"
#     print(empName)
# empFunc();

# def empFunc() :
#     empName = "Root"
#     def empFuncTwo() :
#         print(empName)
#     empFuncTwo()
# empFunc();

# empName = "Steve";
# def empFunc() :
#     print(empName)
# empFunc();
# print(empName);

# empName = 3;
# def empFunc() :
#     empName = "Cook"
#     print(empName)
# empFunc();
# print(empName);

# def empFunc() :
#     global empName
#     empName = "Henry"
# empFunc();
# print(empName);

# empName = "Marnus";
# def empFunc() :
#     global empName 
#     empName = "Magnus"
# empFunc();
# print(empName);

def empFuncOne() :
    empName = "Elon"
    def empFuncTwo() :
        nonlocal empName
        empName = "Mark"
    empFuncTwo()
    return empName
print(empFuncOne())