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