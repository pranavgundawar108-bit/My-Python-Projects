num = int(input("Enter the number:"))


if (num <= 1):
    print("Not a prime number")

for i in range(2,num):
    if (num % i == 0):
        print("Not a prime number")
        break

    else:
        print("It is a prime number")