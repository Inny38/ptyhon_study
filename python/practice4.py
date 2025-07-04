#사용자로부터 시간과 분을 받아서 초로 변환하는 프로그램
hour,minit = map(int, input("시간과 분을 입력하세요").split())
sec = hour*3600 + minit*60
print(f'{hour}:{minit} = {sec}')