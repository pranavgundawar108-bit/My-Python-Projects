cards = [1,2,3,4,5,6,7,9,10]

len_deck = 0
for i in cards: 
    len_deck += 1

n = len_deck + 1
total = (n*(n+1))/2
x = sum(cards)

result = total - x
print("missing card is:",result)