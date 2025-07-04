#사용자로부터 100000에서 999999사이의 숫자를 읽어서 천단위를 구분하는 쉼표를 넣어서 화면에 출력하는 함수
print("100000에서 999999사이의 숫자를 입력하면 쉼표를 찍어주는 함수입니다.")
num = input("숫자를 입력해주세요:")

print(num[:-3]+","+num[-3:])

#front = int(num)//1000
#back = int(num)%1000

#print(str(front)+","+str(back))

"""
if num>= 100000 and num<1000000:
    moreT = num//1000
    lessT = num%1000
    print(moreT,",",lessT)
    print(moreT+lessT)
    print(str(moreT)+","+str(lessT))
    print("%d,%d" %(moreT, lessT))
    print(f"{moreT},{leassT})
"""