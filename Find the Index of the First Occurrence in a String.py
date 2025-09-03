#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/



# haystack="sadbutsad"
# needle="sad"
# list1=list(haystack)
# list2=list(needle)

# for i in range(len(haystack)-len(needle)+1):
#     if (haystack[i:i+len(needle)] == needle):
#         print(i)
#         break
#     elif (haystack[i:i+len(needle)] != needle):
#         print(-1)
#         break

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            list1=list(haystack)
            list2=list(needle)
            for i in range(len(haystack)-len(needle)+1):
                if (haystack[i:i+len(needle)] == needle):
                    return print(i)
                    break
                elif (haystack[i:i+len(needle)] != needle):
                    return print(-1)
                    break


solution = Solution()
haystack="sadbutsad"
needle="sad"
solution.strStr(haystack,needle)





