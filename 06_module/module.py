# import mods;
# import mods as m; # An alias for module Country
# mods.myFunc("Neon");
# m.myFunc("Neon");
# mod = dir(mods);
# print(mod);

# emp = mods.empOne["Country"];
# emp = m.empOne["Country"];
# print(emp);

# Built-in Modules :
# import platform;
# mod = platform.system();
# print(mod);

# dir() Function : List all function and variable names in module
# import platform;
# mod = dir(platform);
# print(mod);

# Import From Module :
from mods import empOne;
print(empOne["Name"]);