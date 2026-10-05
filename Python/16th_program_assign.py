word = input("Enter a word:")
result = ""
index = 0

for char in word:
    if (index % 3 != 0):
        result = result + char

    index = index + 1

print("Original text:",word)
print("Modified text:",result)

