# class EmpOne : # Parent/Base Class
#     def __init__(self, empFName, empLName) :
#         self.empFName = empFName
#         self.empLName = empLName

#     def empNames(self) :
#         print(self.empFName, self.empLName);
        
# class EmpTwo (EmpOne) : # Child/Derived Class
#     pass
# empO = EmpOne("Jack", "Lee");
# empO.empNames();
# empT = EmpTwo("Joe", "Root");
# empT.empNames();

# Add the __init__() Function ;
# class EmpOne : # Parent/Base Class
#     def __init__(self, empFName, empLName) :
#         self.empFName = empFName
#         self.empLName = empLName

#     def empNames(self) :
#         print(self.empFName, self.empLName);
        
# class EmpTwo (EmpOne) : # Child/Derived Class
#     def __init__(self, empFName, empLName):
#        EmpOne.__init__(empFName, empLName)
# empT = EmpTwo("Brayn", "Nodwin");
# empT.empNames();

# super() Function :
# class EmpOne : # Parent/Base Class
#     def __init__(self, empFName, empLName) :
#         self.empFName = empFName
#         self.empLName = empLName

#     def empNames(self) :
#         print(self.empFName, self.empLName);
        
# class EmpTwo (EmpOne) : # Child/Derived Class
#     def __init__(self, empFName, empLName):
#        super().__init__(empFName, empLName)
# empT = EmpTwo("Mark", "Zukerberg");
# empT.empNames();

# Add Properties :
class EmpOne : # Parent/Base Class
    def __init__(self, empFName, empLName) :
        self.empFName = empFName
        self.empLName = empLName

    def empNames(self) :
        print(self.empFName, self.empLName);
        
class EmpTwo (EmpOne) : # Child/Derived Class
    def __init__(self, empFName, empLName, empSalary):
       super().__init__(empFName, empLName)
    #    self.empSalary = 10000
       self.empSalary = empSalary
empT = EmpTwo("Elon", "Musk", 10000); 
empT.empNames();
# print(empT.empSalary);

# Add Methods :
class EmpOne : # Parent/Base Class
    def __init__(self, empFName, empLName) :
        self.empFName = empFName
        self.empLName = empLName

    def empNames(self) :
        print(self.empFName, self.empLName);
        
class EmpTwo (EmpOne) : # Child/Derived Class
    def __init__(self, empFName, empLName, empSalary):
       super().__init__(empFName, empLName)
       self.empSalary = empSalary
    
    def myFunc(self) :
        print("Hey,", self.empFName, self.empLName, "With Salary", self.empSalary)
empT = EmpTwo("Jack", "Marnus", 100000);
empT.myFunc();