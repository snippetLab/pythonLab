# Open File :
# f = open("file.txt");
# print(f.read());

# f = open("/workspaces/pythonLab/07_file_handling/file.txt");
# print(f.read());

# with open("/workspaces/pythonLab/07_file_handling/file.txt") as f :
#     print(f.read());

# Close File :
# f = open("/workspaces/pythonLab/07_file_handling/file.txt");
# print(f.read());
# f.close();

# Read Parts of File :
# with open("/workspaces/pythonLab/07_file_handling/file.txt") as f :
#     print(f.read(3));

# Read Lines :
# with open("/workspaces/pythonLab/07_file_handling/file.txt") as f :
#     print(f.readline());

# with open("/workspaces/pythonLab/07_file_handling/file.txt") as f :
#     print(f.readline())
#     print(f.readline());

with open("/workspaces/pythonLab/07_file_handling/file.txt") as f :
    for i in f :
        print(i);
