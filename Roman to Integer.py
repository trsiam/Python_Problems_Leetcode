#https://leetcode.com/problems/roman-to-integer/description/



# class Solution:
#     def romanToInt(self, s: str) -> int:
        


# I- 1
# II- 2
# III-3
# IV-4
# V-5
# VI-6
# VII-7
# VIII-8
# IX-9
# X-10
# XI-11
# XII-12
# XIII-13
# XIV-14
# XV-15
# XVI-16
# XVII-17
# XVIII-18
# XIX-19
# XX-20
# XXI-21
roman=str(input())
count=0
temp_Vone=0
temp_Vtwo=0
temp_Vthree=0



roman_Values={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "H":1000}
keys=list(roman_Values.keys())

for i in range(len(roman)):
    for j in range(len(keys)):
        key=keys[j]
        if(roman[i]==keys[j]):
            temp_Vone+=roman_Values[key]
            if (roman_Values[key] > temp_Vtwo):
                temp_Vone -= 2* temp_Vtwo
            
            temp_Vtwo = roman_Values[key]


print(temp_Vone)



    




    












# print(roman)




















