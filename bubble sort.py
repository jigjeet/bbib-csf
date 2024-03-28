input_arr = [6,8,3,1,5,0]
def bubble_sort(arr):


    n = len (arr)


    for i in range (n): # 0,1,2,3,
        for k in range (0, n):

            element= arr [k]
            elementright = arr [k+1]
            print ("element", element)
            print ("element", elementright)
            print("=========================")
            #swap
            if element > elementright:
                
