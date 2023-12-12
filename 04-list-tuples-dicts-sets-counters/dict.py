from collections import defaultdict

empty_dict = {}
empty_dict2 = dict()
grades = {"Joel":80, "Tim":95}

# print(grades["Joel"])
# print(grades["Tim"])

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("Key not found")

has_joel_grade = "Joel" in grades
has_kate_grade = "Kate" in grades

# print(has_joel_grade)
# print(has_kate_grade)

# .get(key, default value)
tim_grade = grades.get("Tim", 0)
kate_grade = grades.get("Kate", "Tidak ada")
no_ones_grade = grades.get("No one")

# print(tim_grade)
# print(kate_grade)
# print(no_ones_grade)

grades["Tim"] = 199         # replace
grades["Albert"] = 200      # add

num_students = len(grades)

# print(grades)
# print(num_students)

tweet = {
"user" : "joelgrus",
"text" : "Data Science is Awesome",
"retweet_count" : 100,
"hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

for key, value in tweet_items:
    print(f"Key: {key}, Value: {value}")


# print("id" in tweet_keys)

# Default Dict
# Adalah dictionary kosong yang digunakan sebagai penyimpanan dari data data yang ingin dimasukkan dalam sebuah proses pemograman
document = ["randomize", "randomly", "randomized", "randomness", "randomization", "randomly", "nonrandom", "pseudorandom", "randomizer", "randomly"]

def count_word(document):
    words_counts = {}
    for word in document:
        if word in words_counts:
            words_counts[word] += 1
        else:
            words_counts[word] = 1
    return words_counts

print(count_word(document))


def count_word_int(document):
    word_counts = defaultdict(int)
    for word in document:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

# print(count_word_plus(document))

def count_word_int(document):
    word_counts = defaultdict(int)
    for word in document:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

dd_list = defaultdict(list)
dd_dict = defaultdict(dict)
dd_lambda = defaultdict(lambda: [0,0])

dd_list[2].append(1)
dd_dict["Joel"]["City"] = "Tangerang Barat"
dd_lambda[1][1] = 5

# print(dd_list)
# print(dd_dict)
# print(dd_lambda)