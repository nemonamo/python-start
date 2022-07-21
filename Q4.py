a = input('주민번호를 입력하세요 % - 포함 : ')

num = a[7]
print(num)
b = int(num) % 2
if b:
    print("남자입니다")
else:
    print("여자입니다")
