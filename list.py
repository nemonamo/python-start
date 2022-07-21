a = [1,2,"int", "조찬희" , ["김현민", "김남호"]]

print(a[4][1])


print("a = [1,2,3]")
a = [1,2,3]
print("a[0]")
print(a[0])

print("a[0] + a[2]")
print(a[0] + a[2])

print("a[-1]")
print(a[-1])

b = [4,5,6]
c = a+b
print(c)
print(c[0:5])
c[1:3] = []
print(c)

c= a+b
print(c)
del c[1]
print(c)
c= a+b
c.reverse() #거꾸로 쓰기
print(c)

print(c.index(2)) #위치찾기

c.insert(0,7)      #원하는 위치에 추가
print(c)

c.remove(3)
print(c)

print(c.pop())
a = [1,2,1,1,1,3]
print(a.count(1))

a.extend([4,5,3]) #리스트 요소 추가
print(a)

b = [5,6]
a.extend(b) #리스트에 리스트 추가
print(a)