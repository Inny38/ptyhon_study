#사용자로부터 두 점의 좌표 (x1,x2)와 (y1, y2)를 입력받아서 두 점 사이의 거리를 계산하라.
import math
x1, x2, y1, y2 =map(int,input("두 점의 좌표를 입력하시오").split())

result = math.sqrt(pow(x1-y1,2) + pow(x2-y2,2))
print(result)