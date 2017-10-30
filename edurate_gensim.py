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
    #list_responses.lower()
    #print(list_responses)
    stoplist = set('poop high fuck yeah'.split())
    #print(stoplist)
    texts = []
    for i in list_responses:
        texts.append(i.lower())
    texts = [[word for word in texts.split()]for texts in texts]
    tokens = []
    for i in texts:
        if len(i)>3:
            temp = []
            for i in i:
                if i not in stoplist:
                    #if i.isnumeric() == False:
                        #print(i)
                    temp.append(i)
            tokens.append(temp)
    print(tokens)
    dictionary = corpora.Dictionary(tokens)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    print(dictionary.token2id)

#def corp_eval():
