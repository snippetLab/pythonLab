# empName = ("Mark", "Elon", "Root", "Jack");
# emps = next(empName);
# print(next(emps));
# print(next(emps));
# print(next(emps));
# print(next(emps));

# channelName = "Snippets";
# name = next(channelName);

# print(next(name));
# print(next(name));
# print(next(name));
# print(next(name));
# print(next(name));
# print(next(name));
# print(next(name));
# print(next(name));

# Create Iterator :
# class Numbers :
#     def __iter__(self) :
#         self.numOne = 1
#         return self
    
#     def __next__(self) :
#         numTwo = self.numOne
#         self.numOne += 1
#         return numTwo
# nums = Numbers();
# round = iter(nums);
# print(next(round));
# print(next(round));
# print(next(round));
# print(next(round));
# print(next(round));

# StopIteration :
class Numbers :
    def __iter__(self) :
        self.numOne = 1
        return self
    
    def __next__(self) :
        if self.numOne <= 20 :
            numTwo = self.numOne
            self.numOne += 1
            return numTwo
        else :
            raise StopIteration
nums = Numbers();
round = iter(nums);

for num in round :
    print(num);