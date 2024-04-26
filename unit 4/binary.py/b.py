# problem 1 
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





        