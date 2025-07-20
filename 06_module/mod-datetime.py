import datetime;

xTime = datetime.datetime.now();
# print(xTime);
# print(xTime.strftime("%A"));

# Creating Date Objects :
# xTime = datetime.datetime(2025, 7, 19);
# print(xTime);

# strftime() Method :
xTime = datetime.datetime(2025, 7, 20);

print("Weekday - Short Version : "+ xTime.strftime("%a")); 
print("Weekday - Full Version : "+ xTime.strftime("%A")); 
print("Weekday - Number 0-6 : "+ xTime.strftime("%w")); 
print("Day of Month - 01-31 : "+ xTime.strftime("%d")); 
print("Month Name - Short Version : "+ xTime.strftime("%b"));
print("Month Name - Full Version : "+ xTime.strftime("%B")); 
print("Month as a Number - 01-12 : "+ xTime.strftime("%m")); 
print("Year - Short Version, Without Century : "+ xTime.strftime("%y")); 
print("Year - Full Version : "+ xTime.strftime("%Y")); 
print("Hour - 00-23 : "+ xTime.strftime("%H")); 
print("Hour - 00-12 : "+ xTime.strftime("%I")); 
print("AM/PM : "+ xTime.strftime("%p")); 
print("Minute - 00-59 : "+ xTime.strftime("%M")); 
print("Second - 00-59 : "+ xTime.strftime("%S"));
print("Microsecond 000000-999999 : "+ xTime.strftime("%f")); 
print("UTC Offset : "+ xTime.strftime("%z")); 
print("Timezone : "+ xTime.strftime("%Z")); 
print("Day Number of Year = 001-366 : "+ xTime.strftime("%j")); 
print("Week Number of Year (Sunday First) - 00-53 : "+ xTime.strftime("%U")); 
print("Week Number of Year (Monday First) - 00-53 : "+ xTime.strftime("%W")); 
print("Local version of date and time : "+ xTime.strftime("%c")); 
print("Century : "+ xTime.strftime("%C"));
print("Local Version of Date : "+ xTime.strftime("%x")); 
print("Local Version of Time : "+ xTime.strftime("%X")); 
print("%A Character : "+ xTime.strftime("%%")); 
print("ISO 8601 Year : "+ xTime.strftime("%G")); 
print("ISO 8601 Weekday - 1-7 : "+ xTime.strftime("%u")); 
print("ISO 8601 Wekknumber - 01-53 : "+ xTime.strftime("%V")); 
