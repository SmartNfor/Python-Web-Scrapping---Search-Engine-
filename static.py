import codecs
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import collections 

language  = "english"
search = "I"
f = codecs.open("index.html", 'r', 'utf-8')

def frequency(arr): 
    return collections.Counter(arr)  

# the html parser is specified to ensure uniformity in all systems
document= BeautifulSoup(f.read(),features="html.parser").get_text()

#removing duplicated spaces and puntctiontions
text = " ".join(document.split())
text = text.translate(str.maketrans('', '', string.punctuation))

#unfortunate this quotes resisted
text = text.replace('”','')
text = text.replace(' “','')

stop_words = set(stopwords.words(language)) 
  
word_tokens = word_tokenize(text) 
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
# print (filtered_sentence)

freq = frequency(word_tokens) 
for key, value in freq.items(): 
       if(key==search):
         print (key, " -> ", value)

