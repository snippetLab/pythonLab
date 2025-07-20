# Create Variable :
numOne = 11; # Variable Name : numOne, Value : 11
print(numOne);

empName = "Jack"; # Variable Name : empName, Value : "Jack"
print(empName);

# Casting :
numOne = str(30);
numTwo = int(30);
numThree = float(30);

# Single or Double Quotes ?
empName = "Mark";
empName = 'Mark'; # "Mark" = 'Mark'

# Case Sensitive :
x = 11;
X = "Elon"; # x != X

# Variable Name Rules :
# print("Legal Variable Names : ");
# print("\tempname");
# print("\temp_Name");
# print("\t_emp_Name");
# print("\tempName");
# print("\tEMPNAME");
# print("\tempname1");

# print("Illegal Variable Name :");
# print("\t1empname");
# print("\temp-name");
# print("\temp name");


# Multi Word Variable Names :
# print("Camel Case : newEmployeeName"); # Camel Case
# print("Pascal Case : NewEmployeeName"); # Pascal Case
# print("Snake Case : new_variable_name") # Snake Case

# Many Values to Multiple Variables ;
# empOne, empTwo, empThree = "Mark", "Elon", "Root";
# print(empOne);
# print(empTwo);
# print(empThree);

# One Value to Multiple Varibales :
# empOne = empTwo = empThree = "Joe Root";
# print(empOne);
# print(empTwo);
# print(empThree);

# Unpack Collection :
empName = ["Mark", "Elon", "Root", "Jack"];
empOne, empTwo, empThree, empFour = empName;
# print(empOne);
# print(empTwo);
# print(empThree);
# print(empFour);