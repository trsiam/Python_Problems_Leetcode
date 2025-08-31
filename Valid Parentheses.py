#https://leetcode.com/problems/valid-parentheses/description/


# s="([)]"

# #B=str(input())
# Brackets=list(s)
# closed=True
# stack=[]
# for i in range(len(Brackets)):
#     current_char=Brackets[i]
#     if(current_char == "("):
#         if ")" not in Brackets:
#             closed=False

#     if(current_char == "{"):
#         if "}" not in Brackets:
#             closed=True


#     if(current_char == "["):
#         if "]" not in Brackets:
#             closed=True


# print(closed)      
      
      

s="([)]"
Brackets=list(s)
closed=True
stack=[]


for i in range(len(Brackets)):
    current_char=Brackets[i]

    if current_char in "({[":
        stack.append(current_char)
    elif (current_char == ")"):
        if stack and stack[-1] == "(":
            stack.pop()
        else:
            closed=False
            break
    elif(current_char =="}"):
        if stack and stack[-1]== "{":
            stack.pop()
        else:
            closed=False
            break
    elif(current_char == "]"):
        if stack and stack[-1]=="[":
            stack.pop()
        else:
            closed=False
            break

if stack:
    closed=False
    
print(closed)
    




























