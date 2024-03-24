#there is inbuilt data typees lilke int, bool, string, float.....
#abstract data types are Arry<stack<queues,dict/hashmap

#creationn of Array
array1 = [1,2,3, 'thimphu', 2.5]
print (array1)

#retrieving 
element1 = array1[0]
element2 = array1[4]
last_element = array1[-1]
print (element1)
print(last_element)

#modifying element
array1[0] = 10
print (element1)
print (array1)
 #getting number of elements in an array
no_of_elements = len(array1)
print(no_of_elements)

#slicing 
element = array1[0:2]
print(element1)

#concanate list
arr1 = [1,10]
arr2 = ['thimphu', 'wangudi']

number_to_check = 2
result = number_to_check in arr1
arry3 = arr1 +arr2

#append
arrayvaribale = [1,3,2]
arrayvaribale.append(4)
# insert at a specific index
arrayvaribale.insert(1,10)
arrayvaribale.sort()
print  (arrayvaribale)

stackvar =[]
#adding to stack
stackvar.append(4)
stackvar.append(4)
stackvar.append(3)
print ('after appending', stackvar )
element = stackvar.pop()
print('after p[opping',vars)
print('removed element', element)