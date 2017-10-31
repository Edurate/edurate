from gensim import corpora
from profanity import profanity
from stop_words import get_stop_words
from six import iteritems, viewitems
""" Uses gensim to analyze the text of the responses to the edurate evaluation """

#from nltk.tokenize import RegexpTokenizer
#from stop_words import get_stop_words
#from nltk.stem.porter import PorterStemmer
#from nltk.stem import WordNetLemmatizer


def gensim_analysis(list_responses):
    tokens = create_tokens(list_responses)
    dictionary = dictionary_create(tokens)
    corp_eval(dictionary, tokens)


def create_tokens(list_responses):
    """Takes in the list of responses and makes each word a token"""
    stoplist = get_stop_words('en')
    texts = []
    for i in list_responses:
        texts.append(i.lower())
    texts = [[word for word in texts.split()]for texts in texts]
    tokens = []
    for i in texts:
        if len(i) > 2:
            temp = []
            for i in i:
                if profanity.contains_profanity(i) is False:
                    if i not in stoplist:
                        temp.append(i)
            tokens.append(temp)
    return(tokens)


def dictionary_create(tokens):
    dictionary = corpora.Dictionary(tokens)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    # print(dictionary.token2id)
    # print(corpus)
    return(dictionary)


def corp_eval(dictionary, tokens):

    non_repeat = [
        token for token,
        docfreq in iteritems(
            dictionary.dfs) if docfreq == 1]
    dictionary.filter_tokens(non_repeat)
    dictionary.compactify()
    corpus = [dictionary.doc2bow(token) for token in tokens]
    print(dictionary.token2id)
    print(viewitems(dictionary.dfs))
