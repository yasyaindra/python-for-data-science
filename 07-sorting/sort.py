from collections import Counter

x = [4, 3, 1, 2, -2, 0, -1]

document = ["indra", "indra", "wahyu", "afif", "wahyu","wahyu"]

word_counts = Counter(document)

wc = sorted(word_counts.items(), reverse=True)

print(word_counts.items())
print(wc)
