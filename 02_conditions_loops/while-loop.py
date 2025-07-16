# num = 1;
# while num < 6 :
#     print(num)
#     num += 1;

# break Statement :
# num = 1;
# while num < 11 :
#     print(num)
#     if num == 8 :
#         break
#     num += 1;

# continue Statement :
num = 1;
while num < 11 :
    num += 1
    if num == 6 :
        continue
    print(num)

# else Statement :
num = 1;
while num < 11 :
    print(num)
    num += 1;
else :
    print("Num not <= 11");