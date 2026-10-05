date = int(input("Enter the date"))
month = int(input("Enter the month"))
year = int(input("Enter the year"))

if(date>=1 and date<=31 and month in [1,3,5,7,8,12]  and year>=1):
    print("Date is valid")

elif(date>=1 and date<=30 and month in [4,6,9,11] and year>=1):
    print("Date is valid")

elif(date <= 29 and month == 2 and year % 4 == 0 and year % 100 != 0 and year % 400 == 0 ):
    print("Date is valid")

elif(date>=1 and date<=28 and month in [2] and year>=1):
    print("Date is valid")

else:
    print("Date is invalid")
    