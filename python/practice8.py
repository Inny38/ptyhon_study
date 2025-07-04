#사용자로부터 4자리 정수를 받아서 자리수의 합을 계산하는 프로그램

num = int(input("4자리를 입력하세요"))
lst= [3,2,1,0]
nums =[]
for i in lst:
    a = num//(10**i)
    num = num%(10**i)
    nums.append(a)

result = sum(nums)

print(result)

"""
fourth = num//1000
print(fourth)
third = (num%1000)//100
second =(num%100)//10
first = (num%10)

sum = fourth+third +second+first
print(sum)
"""