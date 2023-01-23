import time;

h,m,s = int(input("Enter the hours: ")),int(input("Enter the minutes: ")),int(input("Enter the seconds: "));

t = h * 3600 + m * 60 + s;

while t > 0:
    h,s = divmod(t,3600);
    m,s = divmod(s,60);
    t-=1;
    time.sleep(1);
    print("{:02d}:{:02d}:{:02d}".format(h,m,s));
    
print("*RING*");
#25mins 08/05/2022