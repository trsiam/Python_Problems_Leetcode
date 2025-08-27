#https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    temp_Vtwo=['Hello','You','just','delved','into','python.']
    temp_Vtwo.insert(1,first)
    temp_Vtwo.insert(2,last)
    temp_Vtwo[2]=temp_Vtwo[2]+"!"
    A=" ".join(temp_Vtwo)
    print(A)


first_Name=input()
last_Name=input()
result=print_full_name(first_Name,last_Name)
print(result)