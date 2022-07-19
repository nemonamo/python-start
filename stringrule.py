print('>>> multiline = "Life is too short\\nYou need python" ')
print(">>> multiline='''\n... Life is too short\n... You need python\n... '''")


print(">>> head = \"Python\" ")
print(">>> head = \" is fun!\" ")
print(">>> head + tail")
b = "'"

head = "Python"
tail = " is fun!"
a = "head tail is  %s " % (head+tail)
print(a)

a = " 고래는 사건의 {keyword}이 아닙니다.".format(keyword = "핵심")
print(a)

print(">>> a = \"Python\" ")
a = "Python"

print(">>> a * 2")
b = "\'%s\'" % (a*2)
print(b)


print('>>> a = "Life is too short, You Python"')
a = "Life is too short, You Python"
print(">>> a[0]")

b = "\'%c\'" % (a[0])
print(b)

print(">>> a[12]")
b = "\'%c\'" % (a[12])
print(b)

print(">>> a[-1]")
b = "\'%c\'" % (a[-1])
print(b)

a = """>>> multiline = '''
... Life is too short
... You need python
... ''' """
print(a)

a = "20171510kimnamho"
code = a[:8]
name = a[8:]

print(code)
print(name)


name = "int"
a = f"내 이름은 {name}입니다"

print(a)

a = "%0.2f" % 3.14159274
print(a)

a = "hobby"
print(a.count('b'))

a = "Python is best choice"
print(a.find('b'))

print(a.find('i',2))

print(a.find('x'))

a = "Life is too short"
print(a.index('t',10))

print(a.index('i'))

a = "," .join("abcdefg")
print(a)

print(a.upper())
b = a.upper()
print(b.lower())

a = " h i "
print(a.strip())