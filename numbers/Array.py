# arr1 = [2, 4, 5, 6, 7, 9]
# sum1=0
# arr2 = [3, 5, 6]
# sum2=0
# arr3 = [4, 8, 9, 2, 1]
# sum3=0
# for i in range (len(arr1)):
#     sum1+= arr1[i]
# for w in range (len(arr2)):
#     sum2+= arr2[w]
# for u in range (len(arr3)):
#     sum3+= arr3[u]
# print(sum1+sum2+sum3)

# arr1 = [2, 4, 5, 6, 7, 9]
# sum1=0
# arr2 = [3, 5, 6]
# sum2=0
# arr3 = [4, 8, 9, 2, 1]
# sum3=0
# for i in range (len(arr1)):
#     if arr1[i]%2==1 :
#         print("arr1",arr1[i])
# for w in range (len(arr2)):
#     if arr2[w]%2==1:
#         print("arr2",arr2[w])
# for o in range (len(arr3)):
#     if arr3[o]%2==1:
#         print("arr3",arr3[o])


#ex1
# def sum(array):
#     total=0
#     for i in array:
#         total+= i
#     return total
# arr1 = [2, 4, 5, 6, 7, 9]
# arr2 = [3, 5, 6]
# # sum2=0
# arr3 = [4, 8, 9, 2, 1]
# print(sum (arr1))
# print(sum (arr2))
# print(sum (arr3))

# 2 - Find Odd number difference arrays
# def sum(array):
#     total=[]
#     for i in array:
#         if i%2==1:
#             total.append(i)
#     return total
# arr1 = [2, 4, 5, 6, 7, 9]
# arr2 = [3, 5, 6]
# # sum2=0
# arr3 = [4, 8, 9, 2, 1]
# print(sum(arr1))
# print(sum(arr2))
# print(sum(arr3))

# 3 - Find average difference arrays

# def sum(array):
#     total=0
#     for i in array:
#         total+=i
#     return total
# arr1 = [2, 4, 5, 6, 7, 9]
# arr2 = [3, 5, 6]
# # sum2=0
# arr3 = [4, 8, 9, 2, 1]
# print(sum(arr1)/len(arr1))
# print(sum(arr2)/len(arr2))
# print(sum(arr3)/len(arr3))


# 4 - Find maximum in difference arrays

# def findMax(array):
#     max = array[0]
#     for i in array:
#         if i > max:
#             max=i
#     return max
# arr1 = [2, 4, 5, 6, 7, 9]
# arr2 = [3, 5, 6]
# # sum2=0
# arr3 = [4, 8, 9, 2, 1]
# print(findMax(arr1))
# print(findMax(arr2))
# print(findMax(arr3))

# 5 - Replace even number in difference arrays with value 100

def replaceValue(array, value):
    for i in range (len(array)):
        if array[i]%2 == 0:
            array[i] = value
    return array
arr1 = [2, 4, 5, 6, 7, 9]
arr2 = [3, 5, 6]
# sum2=0
arr3 = [4, 8, 9, 2, 1]
print(replaceValue(arr1 ,100))
print(replaceValue(arr1 ,300))
print(replaceValue(arr1 ,200))
