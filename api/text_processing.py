import numpy as np
from nltk.corpus import stopwords
import string
import gensim.downloader as api
from keras_preprocessing.sequence import pad_sequences

word2vec_transfer = api.load('glove-wiki-gigaword-100')

def clean(text):
    text = text.split()
    words_only = [word for word in text if word.isalpha()]
    for punctuation in string.punctuation:
        words_only = [word.replace(punctuation, ' ').lower() for word in words_only] # Remove Punctuation
    # lowercased = text.lower() # Lower Case
    #tokenized = word_tokenize(lowercased) # Tokenize
    # words_only = [word for word in tokenized if word.isalpha()] # Remove numbers
    stop_words = set(stopwords.words('english')) # Make stopword list
    without_stopwords = [word for word in words_only if not word in stop_words] # Remove Stop Words
    # lemma=WordNetLemmatizer() # Initiate Lemmatizer
    # lemmatized = [lemma.lemmatize(word) for word in without_stopwords] # Lemmatize
    return without_stopwords

def text_cleaner(list_text):
    list_clean_text=[]
    for text in list_text:
        cleen_txt=clean(text)#[0]
        list_clean_text.append(cleen_txt)
    return list_clean_text

def embed_sentence_with_TF(word2vec, sentence):
    embedded_sentence = []
    for word in sentence:
        if word in word2vec:
            embedded_sentence.append(word2vec[word])

    return embedded_sentence

# Function that converts a list of sentences into a list of matrices
def embedding(word2vec, sentences):
    embed = []

    for sentence in sentences:
        embedded_sentence = embed_sentence_with_TF(word2vec, sentence)
        embed.append(embedded_sentence)

    return embed


def preprocess_pad(list_text):
    list_ = text_cleaner(list_text)


    list_ = embedding(word2vec_transfer, list_)
    list_ = pad_sequences(list_, dtype='float32', padding='post', maxlen=200)
    return list_
