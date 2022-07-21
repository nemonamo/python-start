a = input('주민번호를 입력하세요 % - 포함 : ')

a = a.replace("-","").strip()
print(a[0:6])
print(a[6:13])
