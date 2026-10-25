# Exp No: 4 - Count the frequency of occurrence of a word in a body of text
import ssl
import certifi
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import gutenberg

# Use certifi's certificates so nltk.download works on macOS
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

# Download the gutenberg corpus if not already installed
nltk.download('gutenberg')
nltk.download('punkt')  # Ensure the punkt tokenizer models are also downloaded
nltk.download('punkt_tab')  # Needed by newer NLTK versions

# Load the text from the gutenberg corpus
sample = gutenberg.raw("austen-emma.txt")

# Tokenize the sample text
token = word_tokenize(sample)

# Create a list of the first 50 tokens
wlist = []
for i in range(50):
    wlist.append(token[i])

# Calculate the frequency of each word in the list
wordfreq = [wlist.count(w) for w in wlist]

# Print the word-frequency pairs
print("Pairs\n" + str(list(zip(wlist, wordfreq))))
