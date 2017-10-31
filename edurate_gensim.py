import gensim
import read_responses
from gensim import corpora
from pprint import pprint
from collections import defaultdict
from profanity import profanity
from stop_words import get_stop_words
""" Uses gensim to analyze the text of the responses to the edurate evaluation """

#from nltk.tokenize import RegexpTokenizer
#from stop_words import get_stop_words
#from nltk.stem.porter import PorterStemmer
#from nltk.stem import WordNetLemmatizer
from gensim import corpora, models
import gensim
def gensim_analysis(list_responses):
    tokens = create_tokens(list_responses)
    corpus_create(tokens)
def create_tokens(list_responses):
    """Takes in the list of responses and makes each word a token"""
    stoplist = get_stop_words('en')
    texts = []
    for i in list_responses:
        texts.append(i.lower())
    texts = [[word for word in texts.split()]for texts in texts]
    tokens = []
    for i in texts:
        if len(i)>3:
            temp = []
            for i in i:
                if profanity.contains_profanity(i) == False:
                    if i not in stoplist:
                        temp.append(i)
            tokens.append(temp)
    return(tokens)

def corpus_create(tokens):
    dictionary = corpora.Dictionary(tokens)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    #print(dictionary.token2id)
    #print(corpus)

   # "Removes elements that were not repeated"
    frequency = defaultdict(int)
    for token in tokens:
        for i in token:
            frequency[i] += 1

    texts = [[token for token in tokens if frequency[token] > 1]
             for token in tokens]
    dict = corpora.Dictionary(texts)
    corpus = [dict.doc2bow(i) for i in texts]
    print(corpus)
#def corp_eval():
