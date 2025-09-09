my_list = ["apple", "banana", "cherry"]
txt = "I love apples, apple are my favorite cherry fruit apple gas Apple Banana"
total = 0
for word in txt.lower().split():
    count = my_list.count(word)
    total += count
print(total)