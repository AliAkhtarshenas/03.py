n = int(input("enter the number:"))
list1 = [1,1]
while n != "exit":
    for i in range(1 , n+1):
        if n == 1:
            print(1)
        elif n == 2:
            print(1,1)
        else:
            a = list1[i-1]+list1[i-2]
            list1.append(a)