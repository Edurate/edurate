import gensim
import read_responses
from gensim import corpora
from pprint import pprint
""" Uses gensim to analyze the text of the responses to the edurate evaluation """

#from nltk.tokenize import RegexpTokenizer
#from stop_words import get_stop_words
#from nltk.stem.porter import PorterStemmer
#from nltk.stem import WordNetLemmatizer
from gensim import corpora, models
import gensim

def create_tokens(list_responses):
    """Takes in the list of responses and makes each word a token"""
    texts = [[word for word in list_responses.lower().split()]
        for list_responses in list_responses]
    #print(texts)
    dictionary = corpora.Dictionary(texts)
    #print(dictionary.token2id)
    corpus = [dictionary.doc2bow(text) for text in texts]
    print(corpus)
    return(corpus)

#def corp_eval():
