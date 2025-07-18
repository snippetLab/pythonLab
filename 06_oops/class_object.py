# Create Class :
# class Employee :
#     empName = "Joe Root";
# Create Object :
# emp = Employee();
# print(emp.empName);

# __init__() Function :
# class Employee :
#     def __init__(self, empName, empAge) :
#         self.empName = empName
#         self.empAge = empAge
# emp = Employee("Jack", 28);
# print(emp.empName);
# print(emp.empAge);

# __str__ Function :
# class Employee :
#     def __init__(self, empName, empAge):
#         self.empName = empName
#         self.empAge = empAge
#     def __str__(self):
#         return f"{self.empName} {self.empAge}"
# emp = Employee("Jack", 28);
# print(emp);

# Object Methods :
# class Employee :
#     def __init__(self, empName, empAge) :
#         self.empName = empName
#         self.empAge = empAge
    
#     def myFunc(self) :
#         print("Emplyee Name : " + self.empName);
# emp = Employee("Jack", 28);
# emp.myFunc();

# self Parameter :
# class Employee :
#     def __init__(emps, empName, empAge) :
#         emps.empName = empName
#         emps.empAge = empAge
    
#     def myFunc(ems) :
#         print("Emplyee Name : " + ems.empName);
# emp = Employee("Jack", 28);
# emp.myFunc();

# Modify Object Properties :
# class Employee :
#     def __init__(self, empName, empAge) :
#         self.empName = empName
#         self.empAge = empAge
# emp = Employee("Jack", 28);
# print("Old Age : " , emp.empAge);
# emp.empAge = 31;
# print(emp.empName);
# print(emp.empAge);

# Delete Object Properties :
# class Employee :
#     def __init__(self, empName, empAge) :
#         self.empName = empName
#         self.empAge = empAge
# emp = Employee("Jack", 28);
# del emp.empAge;
# print(emp.empName);

# The pass Statement :
class Employee :
    pass