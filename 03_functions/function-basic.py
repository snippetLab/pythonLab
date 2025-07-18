# Function Creation :
# def myFunc() : # Function Creation
#     print("Yey! Function Created");

# Function Call :
# def myFunc() :
#     print("Yey! Function Created");
# myFunc(); # Function Call


# Function Arguments :
# def myFunc(empName) :
#     print("Employee Name : " + empName);
# myFunc("Joe Root");

# Number of Arguments :
# def myFunc (empId, empName) :
#     print(f"Employee Id {empId}, Employee Name {empName}");
# myFunc("1", "Joe Root");

# Function with less argumetns :
# def myFunc (empId, empName) :
#     print(f"Employee Id {empId}, Employee Name {empName}");
# myFunc("1");

# Function with more argumetns :
# def myFunc (empId, empName) :
#     print(f"Employee Id {empId}, Employee Name {empName}");
# myFunc("1", "Joe Root", "10000");

# Arbitary Arguments :
# def myFunc(*empName) :
#     print("Yougnest Employee : " + empName[3]);
# myFunc("Mark", "Elon", "Root", "Jack", "Ryan");

# Keyword Arguments :
# def myFunc(empOne, empTwo, empThree, empFour, empFive) :
#     print("Oldest Employee : " + empTwo);
# myFunc(empOne = "Mark", empTwo = "Elon",empThree = "Root", empFour = "Jack",empFive = "Ryan");

# Arbitray Keyword Arguments :
# def myFunc(**empExp) :
#     print("Root's Experience : " + empExp["exp"]);
# myFunc(exp = "5 Years");

# Default Parameter Value :
# def myFunc(empName = "Jack") :
#     print("Employee Name : " + empName);
# myFunc("Mark");
# myFunc(); # Default Parameter Value
# myFunc("Elon");
# myFunc("Root");

# List As An Argument :
# def myFunc(empName) :
#     for emp in empName :
#         print(emp);
# empName = ["Mark", "Elon", "Root"];
# myFunc(empName);

# Return Value :
# def myFunc(num) :
#     return 3 * num;
# print(myFunc(8));
# print(myFunc(9));
# print(myFunc(11));

# Pass Statement :
# def myFunc() :
#     pass

# Positional-Only Arguments :
# def myFunc(num, /) : # Keyword Argument Not Allowed
# def myFunc(num) : # Keyword Argument Allowed
#     print(num);
# myFunc(11); 
# myFunc(num = 8);

# Keyword-Only Arguments :
# def myFunc(*, num) : # Postional Argument Not Allowed
# def myFunc(num) : # Positional Argument Allowed
#     print(num);
# myFunc(num = 3);
# myFunc(13);

# Combine Postional-Only and Keyword-Only :
def myFunc(numOne, numTwo, /, *, numThree, numFour) :
    print(numOne + numTwo + numThree + numFour);
myFunc(1, 3, numThree = 9, numFour = 11);
