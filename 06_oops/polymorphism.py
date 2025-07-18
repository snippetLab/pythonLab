# Function Polymorphism
# empNamme = "Joe Root";
# print(len(empNamme));

# empName = ("Mark", "Elon", "Root", "Jack");
# print(len(empName));

# empDet = {
#     "Name" : "Elon Musk",
#     "Company" : "Space-X",
#     "Salary" : 10000
# };
# print(len(empDet));

# Class Polmorphism :
# class EmpOne :
#     def __init__(self, empName, empAge):
#         self.empName = empName
#         self.empAge = empAge

#     def work(self) :
#         print("Analyse");

# class EmpTwo :
#     def __init__(self, empName, empAge):
#         self.empName = empName
#         self.empaAge = empAge
    
#     def work(self) :
#         print("Code");

# class EmpThree :
#     def __init__(self, empName, empAge):
#         self.empName = empName
#         self.empAge = empAge
    
#     def work(self) :
#         print("Test");
# empO = EmpOne("Brook", 40);
# empT = EmpTwo("Root", 38);
# empTh = EmpThree("Henry", 45);

# for emp in (empO, empT, empTh) :
#     emp.work();

# Inheritance Class Polymorphism :
class Company :
    def __init__(self, empName, empAge) :
        self.empName = empName
        self.empAge = empAge
    
    def work(self) :
        print("Work");

class EmpOne(Company) :
    pass

class EmpTwo(Company) :
    def work(self) :
        print("Code")

class EmpThree(Company) :
    def work(self) :
        print("Test")

empO = EmpOne("Henry", 25);
empT = EmpTwo("Brook", 38);
empTh = EmpThree("Root", 30);

for emp in (empO, empT, empTh) :
    print(emp.empName)
    print(emp.empAge)
    emp.work();
