f = int(input("Enter a number: "));
s = [0,1];
#for x in range(f):s.append(s[-2]+s[-1]); utilizes more memory
while s[-1] < f:s.append(s[-2]+s[-1]);
if f in s:print(s,"Number found in fibonacci sequnce!");
#9mins 28/05/2022