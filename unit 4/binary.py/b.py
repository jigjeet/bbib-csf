'''# problem 1 
#given an input string with just open and close 

####input_str = ("(((")
"""alien = 0
for  string in range(float(input_str)):
    print (string)
    if string == "(":
        print(alien -string )
    else:
        string == ')'
        print (alien + string )#####"""

alien = 0
input_str = "))(())"

#go through each charahcter of the inout string
for i in input_str:
    if i == "(":
        print (alien + 1 )
    else:
        i == ")"
        print (alien - 1)



input_str = "((())())()(((((()()(()())())(()((((((((()))()(())(()())((()))())(((()())))()))(((()))()())()((()(())))((())())())()))))(((())()))()(()((()))(())()())))()()())(()(())))()))((())())()(((()()()()(()(()(((())((((()))))))(())((()(()())())()(())))()()(((((()))))(()))()))(())())))((()))((())))()))()))()(()(()))(()()())(()((((()())((()((()(()))))(()))())((())(((()()()))((((((()()()(()(())(()()()))()()()((((((())()))())()())()))()(())()())(()())()((()))()))))((((())))))())(())((((())))())((())()))(()))())))((())))()))))))((())(())))((())))(())))(())()(()()))(((())()((()()(((()))((()(()))()))))))()))))(()()(((()()((((((())()))()(((((((())())))()()((()))())())(((()(())()((((((())))))))()))))(())((((()((()()(()(())))()((((((())(()))(()))))((()(((()))()))))))(((((())()))(((((((()(()()((()))(())((()())((((()(((()))((()(()))))())())))())())(()))))(())(((())))())))((()(()(((((())))()())()()(((()()))()(()(((((())(())(())))(()())()(()))()((()())))()))())())(()(())()))())(())))(((((()())))()(()))(()()(()(()"

floor_index = 0 #? variable to keep track of the ans
for i in input_str: #! go through each character 
    if i == "(": #? if ( add one to the answer
        floor_index = floor_index + 1
    if i == ")": #? if ) sub one to the answer
        floor_index = floor_index - 1
# print the final answer
print('the final floor is', floor_index)'''






#task 2


nput_str = ")))"
stack = []
for char in input_str:
    if char == "(":
        stack.append(char)
    if char == ")":
        stack.pop()
length = len(stack)
if length == 0:
    print('True')
else:
    print("False")