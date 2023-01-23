year = int(input("Enter a year: "));
print("It's a leap year!")if (year % 100 == 0 and year % 400 == 0) or  (int("".join(list(str(year))[:2])) % 4 == 0) else None;
#10mins 20/05/2022