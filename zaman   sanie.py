
while True:
    h = int(input("Enter hours: " ))
    m = int(input("Enter minuts: " ))
    s = int(input("Enter seconds: " ))
    if h<0 or m<0 or m>60 or s<0 or s>60:
       print("error")
    else:
       print("you enter:" , h, ":" , m, ":" , s)
       time = (h*3600) + (m*60) + s
       print("second:" , time)
       message = input("you want exit(No or Yes): ")
       if message == "y" or "message" == "Y" or message =="Yes" or message == "yes":
           exit()