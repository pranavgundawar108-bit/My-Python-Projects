h1 = int(input("Enter in hours:"))
m1 = int(input("Enter in minutes:"))
s1 = int(input("Enter in seconds:"))

h2 = int(input("Enter in hours:"))
m2 = int(input("Enter in minutes:"))
s2 = int(input("Enter in seconds:"))

time_1 = (h1*3600)+(m1*60)+s1
time_2 = (h2*3600)+(m2*60)+s2
diff = time_2-time_1
print("Difference in seconds is:",diff)
