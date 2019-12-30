import requests
import codecs
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import collections 

language  = "english"
url = 'https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/'
search = "Collection"

def frequency(arr): 
    return collections.Counter(arr)  

res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
document = soup.find_all(text=True)

text = ''
blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head', 
	'input',
	'script',
    'style',
]

for t in document:
	if t.parent.name not in blacklist:
		text += '{} '.format(t)
#removing duplicated spaces and puntctiontions
text = " ".join(text.split())
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