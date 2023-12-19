from collections import Counter
# x = [4, 3, 1, 2]

x = [4, 3, 1, 2, -2, 0, -1]

y = sorted(x, key=abs, reverse=True)

# print(y)

document = ["indra", "indra", "wahyu", "afif", "wahyu","wahyu"]

word_counts = Counter(document)

wc = sorted(word_counts.items(), reverse=True)

# print(word_counts.items())
print(wc)
