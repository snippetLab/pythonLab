# weekDay = 5;
# match weekDay :
#     case 1 :
#         print("Monday")
#     case 2 :
#         print("Tuseday")
#     case 3 :
#         print("Wenesday")
#     case 4 : 
#         print("Thursady")
#     case 5 :
#         print("Friday")
#     case 6 :
#         print("Saturday")
#     case 7 :
#         print("Sunday")
    # Default Case : 
#     case _ : 
#         print("No Found")

# weekDay = 5;
# match weekDay :
#     case 1 | 2 | 3 | 4 | 5 :
#         print("Weekdays")
#     case 6 | 7 :
#         print("Weekend")

weekMonth = 3;
weekDay = 5;
match weekDay :
    case 1 | 2 | 3 | 4 | 5 if weekMonth == 3:
        print("March Weekdays")
    case 6 | 7 if weekMonth == 4:
        print("April Weekend")
