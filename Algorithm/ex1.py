# We have 3 arrays
# arr1 = [5, 6, 56, 6, 7, 9]
# arr2 = [3, 5, 7, 9, 8]
# arr3 = [4, 8, 3, 2, 1, 7, 3, 9]
# 1- find minimum in array
# 2 - Find some even number difference arrays
# 3 - Reverse all difference arrays
# 4 - add new value to array with : 100
# # 5 - Replace number 7 in arr1 with 10, arr2 with 20 and arr3 with 30


# 1- find minimum in array
def minimumNumber(array):
    Mix=array[0]
    for i in array:
        if i < Mix :
            Mix= i
    return Mix
arr1 = [5, 6, 56, 6, 7, 9]
arr2 = [3, 5, 7, 9, 8]
arr3 = [4, 8, 3, 2, 1, 7, 3, 9]
print(minimumNumber(arr1))


# 2 - Find some even number difference arrays

def evenNumber(array):
    result=[]
    for i in range (len(array)):
            result.append(array[i])
    return  result
arr1 = [5, 6, 56, 6, 7, 9]
arr2 = [3, 5, 7, 9, 8]
arr3 = [4, 8, 3, 2, 1, 7, 3, 9]
evenNumber(arr1)
print(evenNumber(arr2))
print(evenNumber(arr3))

# 3 - Reverse all difference arrays
def reverse_array( array):
    length = len (array) - 1 
    new_array = []
    for i in range (len(array)):
        new_array.append(array[length-i])
    return new_array

arr1 = [5, 6, 56, 6, 7, 9]
arr2 = [3, 5, 7, 9, 8]
arr3 = [4, 8, 3, 2, 1, 7, 3, 9]
print(reverse_array(arr1))
print(reverse_array(arr2))
print(reverse_array(arr3))

# 4 - add new value to array with : 100

arr1 = [5, 6, 56, 6, 7, 9]
new=[]
for num in arr1:
     if num %2==0:
          new.append(num)
print(num)
     
