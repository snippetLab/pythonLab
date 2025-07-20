# print("Arithmetic Operators : +, -, *, /, %, **, //");
# print("Assignment Operators : =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=");
# print("Comparison Operators : ==, !=, >, <, >=, <=");
# print("Logical Operators : and, or, not");
# print("Identity Operators : is, is not");
# print("Membership Operators : in, not in");
# print("Bitwise Operators : &(AND), |(OR), ^(XOR), ~(NOT), << , >>");

# Operator Precedence :
# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((8+3) - (8+3));

# Multiplication * has higher precedence than addition +, therefore multiplications are evaluted before additions :
print(8 + 11 *3 );

# If two operators have same precedence, the expression is evaluated from left to right
# Addition + and substraction - has the the same precedence. and therefore we evaluate the expression from left to right :
print(3 + 8 - 13 + 9);

# Oprator Precedence Table : Highest To Lowest 
print("() : Parentheses");
print("** : Exponentiation");
print("+x -x ~x : Unary plus, unary minus, and bitwise NOT");
print("* / // % : Multiplication, division. floor division. and modulus");
print("+ - : Addition and substraction");
print("<< >> : Bitwise left and right shifts");
print("& : Bitwises AND");
print("^ : Bitwise XOR");
print("| : Bitwise OR");
print("== != > >= < <= is is not in not in : Comparisons, identity, and membership operators");
print("not : Logical NOT");
print("and : AND");
print("or : OR");
