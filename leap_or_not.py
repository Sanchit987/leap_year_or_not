year = int(input())

if year % 400 == 0:
    print("is a leap year")
elif year % 100 == 0:
    print("not a leap year")
elif year % 4 == 0:
    print("is a leap year")
