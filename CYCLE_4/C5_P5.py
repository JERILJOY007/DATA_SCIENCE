import nltk
from nltk import ngrams
from nltk.corpus import stopwords

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')  # Add this line
nltk.download('stopwords')

from nltk.tokenize import sent_tokenize, word_tokenize

text1 = "The data given satisfies the requirement for model generation. This is used in Data Science Lab"
print("Sentence tokenization: ")
print(sent_tokenize(text1))

print("Word tokenization: ")
print(word_tokenize(text1))

text = word_tokenize(text1)
text2 = [word for word in text if word.lower() not in stopwords.words('english')]
print("\nRemoving stop words: ")
print(text2)

print("\nn-grams: ")
unigrams = ngrams(text2, 3)
for grams in unigrams:
    print(grams)
