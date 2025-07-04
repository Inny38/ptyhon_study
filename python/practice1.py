#두 개의 정수를 받아서 정수의 합, 차, 곱, 평균, 큰수, 작은수를 계산하고 화면에 출력하는 프로그램을 작성.

x = int(input("첫 번째 정수를 입력하시오"))

y = int(input("두 번째 정수를 입력하시오"))

sum = x+y  #합
sub = x-y  #차
mul = x*y  #곱
mean = (x+y)/2 #평균
max2 = max(x,y) #최대
min2a = min(x,y)
massage = "x= %d, y= %d"
print(massage %(x,y))
print(sum, sub, mul, mean, max2, min2a)