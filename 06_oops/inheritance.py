# class EmployeeOne : # Parent/Base Class
#     def __init__(self, empFName, empLName) :
#         self.empFName = empFName
#         self.empLName = empLName

#     def empNames(self) :
#         print(self.empFName, self.empLName);
        
# class EmployeeTwo (EmployeeOne) : # Child/Derived Class
#     pass
# empO = EmployeeOne("Jack", "Lee");
# empO.empNames();
# empT = EmployeeTwo("Joe", "Root");
# empT.empNames();

# Add the __init__() Function ;
# class EmployeeOne : # Parent/Base Class
#     def __init__(self, empFName, empLName) :
#         self.empFName = empFName
#         self.empLName = empLName

#     def empNames(self) :
#         print(self.empFName, self.empLName);
        
# class EmployeeTwo (EmployeeOne) : # Child/Derived Class
#     def __init__(self, empFName, empLName):
#        EmployeeOne.__init__(empFName, empLName)
# empT = EmployeeTwo("Brayn", "Nodwin");
# empT.empNames();

# super() Function :
# class EmployeeOne : # Parent/Base Class
#     def __init__(self, empFName, empLName) :
#         self.empFName = empFName
#         self.empLName = empLName

#     def empNames(self) :
#         print(self.empFName, self.empLName);
        
# class EmployeeTwo (EmployeeOne) : # Child/Derived Class
#     def __init__(self, empFName, empLName):
#        super().__init__(empFName, empLName)
# empT = EmployeeTwo("Mark", "Zukerberg");
# empT.empNames();

# Add Properties :
class EmployeeOne : # Parent/Base Class
    def __init__(self, empFName, empLName) :
        self.empFName = empFName
        self.empLName = empLName

    def empNames(self) :
        print(self.empFName, self.empLName);
        
class EmployeeTwo (EmployeeOne) : # Child/Derived Class
    def __init__(self, empFName, empLName, empSalary):
       super().__init__(empFName, empLName)
    #    self.empSalary = 10000
       self.empSalary = empSalary
empT = EmployeeTwo("Elon", "Musk", 10000); 
empT.empNames();
# print(empT.empSalary);

# Add Methods :
class EmployeeOne : # Parent/Base Class
    def __init__(self, empFName, empLName) :
        self.empFName = empFName
        self.empLName = empLName

    def empNames(self) :
        print(self.empFName, self.empLName);
        
class EmployeeTwo (EmployeeOne) : # Child/Derived Class
    def __init__(self, empFName, empLName, empSalary):
       super().__init__(empFName, empLName)
       self.empSalary = empSalary
    
    def myFunc(self) :
        print("Hey,", self.empFName, self.empLName, "With Salary", self.empSalary)
empT = EmployeeTwo("Jack", "Marnus", 100000);
empT.myFunc();