import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
#from nltk.set.wordnet import WordNet Lemmatizer
import pandas as pd
import numpy as py
import re
from nltk.probability import FreqDist
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import seaborn as sns
from time import sleep

fhand = open('obamatweets.txt', encoding ="cp1252")
inp = fhand.read()

lst = list()
comma = inp.split(",")
spaces = [s.split(" ") for s in comma]

#cleaning data
for lists in spaces:
    for words in lists:
        word = words.split()
        word = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in word]
        lst.append(word)

#filter empty Sets, convert to string
lst = [x for x in lst if x]
stem = []
string_lst= [str(inner_lst) for inner_lst in lst]
string_lst = [re.sub(r'[^A-Za-z0-0]+', '', x) for x in string_lst]

#Stem common related words together
s_stemmer = SnowballStemmer(language= 'english')
for word in string_lst:
    stem.append(s_stemmer.stem(word))

#Remove stop words such as 'a', 'the', etc.
stopwords = open('stopwords.txt')
stopwords = stopwords.read()
stem2 = []
for words in stem:
    if words not in stopwords:
        stem2.append(words)

#count number of repeated words
word_counts = {}
for word in stem2:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

lst = list()

#data visualization for the 15 most frequent Words
def sort_dictionary_by_values(d):
  # Create a list of tuples so that word_counts can be sorted
  sorted_d = sorted(d.items(), key=lambda x: x[1])
  for elements in sorted_d:
      lst.append(elements)


sort_dictionary_by_values(word_counts)
word_counts = dict(lst)
values = list(word_counts.values())[-10:]
keys = list(word_counts.keys())[-10:]

# Create a new dictionary with only the last 10 entries
word_counts = dict(zip(keys, values))

file = 'obama_word_counts'
with open(file, 'w') as f:
    f.write(str(lst))

frequencies = list(word_counts.values())
plotwords = list(word_counts.keys())
plt.figure(figsize = (10,5))
sns.barplot(x=plotwords, y=frequencies)
plt.title('Top Words Overall')
plt.ylabel('Word from Tweet', fontsize = 12)
plt.xlabel('Count of Words', fontsize = 12)
plt.show()
sleep(10)
quit()
