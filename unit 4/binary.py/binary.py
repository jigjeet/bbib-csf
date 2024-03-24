#binary search
#inph the target 
arry = [3,4,5,6,7,8,9]
target = 9

low = 0
high = len(arry) - 1
#loop
while low< high:
    #divide
    mid = (low +high)//2#(this is the middel index (not the value of the arry))
    # comparen the middel with
    if arry[mid] == target:
        print("found")

        