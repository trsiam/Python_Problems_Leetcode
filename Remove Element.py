#https://leetcode.com/problems/remove-element/description/


# nums = [0,1,2,2,3,0,4,2]
# val=2
# k=0
# for i in range(len(nums)-3):
#     if nums[i]!=val:
#         nums[k]=nums[i]
#         k+=1
      
# print(nums[:k])

nums = [0,1,2,2,3,0,4,2]
val=2
k=0
for i in nums:
    if i !=val:
        nums[k]=i
        k+=1
k=len(nums[:k])
print(k)

