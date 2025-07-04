#음식 비용을 입력하여 팁(10%)을 포함한 전체 금액을 계산
price = int(input("음식 비용: "))
print(f"""
가격 : {price}원
부가세 : {price*0.1:.0f}원
합산액 : {price*1.1: .0f}원
""")