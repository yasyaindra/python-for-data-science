from collections import Counter

c = Counter([0,0,2,3,3,3])

print(c)

document = ["randomize", "randomly", "randomized", "randomness", "randomization", "randomly", "nonrandom", "pseudorandom", "randomizer", "randomly"]

word_counts = Counter(document)

for word, count in word_counts.most_common(3):
    print(word, count)