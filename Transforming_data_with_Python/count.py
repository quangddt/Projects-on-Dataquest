from read import load_data
import pandas as pd
from collections import Counter

df = load_data()

#Remove missing value in headline
headline = df['headline'].dropna()

#Combine all of the headlines into one long string
headline_full = ' '.join(headline.tolist())

#Remove special characters
special_chars = "!@#$%^&*()+-?:|[]'\"_"
for char in special_chars:
    headline_full = headline_full.replace(char, "")

headline_full = headline_full.lower().split()
     
#Count words in headline
c = Counter(headline_full)
if __name__ == "__main__":
    print(c.most_common(100))
