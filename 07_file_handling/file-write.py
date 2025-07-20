# with open("/workspaces/pythonLab/07_file_handling/file.txt", "a") as f :
#     f.write("A snippet is a small piece or fragment of something, often used to refer to a short excerpt or portion of text, code, or other media.");

# with open("/workspaces/pythonLab/07_file_handling/file.txt") as f :
#     print(f.read());

# Overwrite Existing Content :
# with open("/workspaces/pythonLab/07_file_handling/file.txt", "w") as f :
#     f.write("Opps! Overwritten");

# with open("/workspaces/pythonLab/07_file_handling/file.txt") as f :
#     print(f.read());

# Create New File ;

# f = open("/workspaces/pythonLab/07_file_handling/fileOne.txt", "x")
# print(f);

# f = open("/workspaces/pythonLab/07_file_handling/fileTwo.txt", "a")
# print(f);

f = open("/workspaces/pythonLab/07_file_handling/fileThree.txt", "w")
print(f);