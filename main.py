import nltk
import nltk.corpus
from nltk.corpus import stopwords
import re

# nltk.data.path.append('%USERPROFILE%\\Downloads\\nltk_data')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
# print(nltk.corpus.brown)

from nltk.stem.wordnet import WordNetLemmatizer

text = "Professor Abdolmalek, please report your absences promptly."
text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
words = text.split()
print(words)

print(stopwords.words("english"))

words = [w for w in words if w not in stopwords.words("english")]
print(words)

# Reduce words to their root form
lemmed = [WordNetLemmatizer().lemmatize(w) for w in words]
print(lemmed)