#https://leetcode.com/problems/plus-one/description/

digits = [1,2,3]
num=''.join(map(str,digits))
num2=int(num)
num3=num2+1
num4=list(map(int,str(num3)))
print(num4)




