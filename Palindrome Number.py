
#https://leetcode.com/problems/palindrome-number/

# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
        
# class Solution(object):
#     def isPalindrome(self, x):
#         if(x<0):
#             return False    
#         if(0<= x <10):
#             return True
#         if(10 <= x <=99):
#             f_Value=x//10
#             t_Value=x%10
#         if (100 <= x < 999):
#             f_Value=x//100
#             t_Value=x%10
#         if(f_Value == t_Value):
#             return True
#         else:
#             return False

# Solution=Solution()
# result=Solution.isPalindrome(1111)
# print(result)
 
class Solution(object): 
    def isPalindrome(self, x) -> bool:
        if(x<0 or(x%10==0 and x!= 0)):
            return False
        reverse_Half=0
        while(x > reverse_Half):
            reverse_Half=reverse_Half*10 + (x//10)
            x//=10
        return x==reverse_Half or x== reverse_Half //10

Solution=Solution()
result=Solution.isPalindrome(123)
print(result)


