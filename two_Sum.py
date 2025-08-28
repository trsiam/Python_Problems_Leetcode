#https://leetcode.com/problems/two-sum/description/

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
        

# temp_V=[]
# nums=list(map(int,input().split()))
# target=int(input())
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if(nums[i]+nums[j] == target):
#             temp_V.append(i)
#             temp_V.append(j)

# print(temp_V)
            



# tem=[]
# i=5
# j=4
# tem.append(i)
# tem.append(j)
# print(tem)




# class Solution:
#     def two_Sum(self,nums:list[int],target:int):
#         temp_V=[]
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if(nums[i]+nums[j] == target):
#                     temp_V.append(i)
#                     temp_V.append(j)

#         return temp_V
    


# solution = Solution()
# print(solution.two_Sum([2, 7, 11, 15], 9))


class Solution(object):
    def twoSum(self, nums, target):
        temp_V=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j] == target):
                    temp_V.append(i)
                    temp_V.append(j)

        return temp_V
    

solution = Solution()
print(solution.two_Sum([2, 7, 11, 15], 9))
