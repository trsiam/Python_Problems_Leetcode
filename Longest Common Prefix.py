#https://leetcode.com/problems/longest-common-prefix/description/

# for i in range(min(len(temp_V),len(temp_Vtwo))-1):
#     if(temp_V[i: i+1] == temp_Vtwo[i:i+1]):
#         print("both have simimar prefix ",temp_V[i]+temp_V[i+1])
    




strs=list(input().split())

min_lenth=min(len(word) for word in strs )

prefix=""

for i in range(min_lenth):
    current_Char=strs[0][i]
    for words in strs[1:]:
        if (words[i] != current_Char):
            break  
    else:    
        prefix+=current_Char
        continue
    break

print(prefix)