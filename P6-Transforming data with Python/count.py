import read
from collections import Counter

df = read.load_data()

s = ""

for headline in df["headline"].tolist():
    s += str(headline)

head2word = s.lower().split(" ")

cnt = Counter()

for word in head2word:
    cnt[word] += 1

most_100_words = []
for item in cnt.most_common(100):
    most_100_words.append(item[0])
    
print(most_100_words)
