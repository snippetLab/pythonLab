# Exception Handling :
# try :
#     print(empName);
# except :
#     print("An Exception Occured");

# try :
#     print(empName);
# except NameError :
#     print("Not Defined");
# except :
#     print("Unknown Error");


# Else :
# try :
#     print("Try Excepted");
# except NameError :
#     print("Not Defined");
# except :
#     print("Unknown Error");
# else :
#     print("Thumbs Up!");

# try :
#     print(empName);
# except NameError :
#     print("Not Defined");
# except :
#     print("Unknown Error");
# else :
#     print("Thumbs Up!");

# Finally :
# try :
#     print(empName);
# except :
#     print("Uhh!, Not Good");
# finally :
#     print("Try-Except Finished");

# try :
#     fName = open("try-except.txt")
#     try :
#         fName.write("Try Except")
#     except :
#         print("Unknown Error : File not writing")
#     finally :
#         fName.close();
# except :
#     print("Unknown Error : File not opening");

# Raise An Exception :
# xNum = -11;
# if xNum < 0 :
#     raise Exception("Exception Raised");

txt = "Snippets";
if not type(txt) is int :
    raise TypeError("Only Integers Allowed");
