a = int(input("enter number"))
c = 0
list1 = []
for i in range(1 , a+1):
    b = float(input("enter number"))
    list1.append(b)
    c = c+b
min = min(list1)
max = max(list1)
d = c/a
print("min:",min,"miangin:",d,"max:",max)