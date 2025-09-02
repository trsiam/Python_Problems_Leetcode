#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# def quicksort(arr):
#         if len(arr) <= 1:
#             return arr
#         pivot = arr[len(arr) - 1]

#         left = [x for x in arr[:-1] if x <= pivot]  
#         right = [x for x in arr[:-1] if x > pivot]  

#         return quicksort(left) + [pivot] + quicksort(right)


num=[0,0,1,1,1,2,2,3,3,4]
i=0
while i < len(num)-1:
    if num[i] == num[i+1]:
        num.pop(i+1)
    else:
        i+=1
k=len(num)
print(num)


























