#problem to find number of desk requied:

a = 20
b = 21
c = 22

desk_a = a // 2
desk_b = b // 2
desk_c = c // 2
desk_total = desk_a +desk_b +desk_c

total_desk = desk_total + 63 % 2
print("total desk required=",total_desk)
