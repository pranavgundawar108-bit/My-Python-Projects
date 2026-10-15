#Program to add the digits of numbers:
digit_sum = 0
n = int(input("Enter a number:"))
while(n>0):
    digit = n % 10
    digit_sum += digit
    n = n // 10
   
print("Sum of digits is:",digit_sum)
