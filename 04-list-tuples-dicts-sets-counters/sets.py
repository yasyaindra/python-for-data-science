primes = {2,3,5,7}
s = set()

s.add(1)
s.add(2)
s.add(3)

word_list = ["a", "an", "at", "yet", "you"]
print("zip" in word_list) # False, but have to check every element

stopwords_set = set(word_list)
print("zip" in stopwords_set) # very fast to check