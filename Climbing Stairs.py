#https://leetcode.com/problems/climbing-stairs/description/

# w=2

# print((w-1)+(w-2))



# def climbStairs(n: int) -> int:
#         if (n==0 or n==1 ):
#             return 1
#         if (n==2):
#             return 2
#         return (n-1)+(n-2)

# print(climbStairs(4))


def climbStairs(n: int) -> int:
    memo = {}
    return helper(n, memo)
    
def helper( n: int, memo: dict[int, int]) -> int:
    if n == 0 or n == 1:
        return 1
    if n not in memo:
            memo[n] = helper(n-1, memo) + helper(n-2, memo)
    return memo[n]

print(climbStairs(5))





