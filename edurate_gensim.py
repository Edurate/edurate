from gensim import corpora, models
from profanity import profanity
from stop_words import get_stop_words
from six import iteritems, viewitems
from colorama import Fore, Style
import logging
import pyLDAvis
import pyLDAvis.gensim
import gensim
import warnings
""" Uses gensim to analyze the text of the responses to the edurate evaluation """

#from nltk.tokenize import RegexpTokenizer
#from stop_words import get_stop_words
#from nltk.stem.porter import PorterStemmer
#from nltk.stem import WordNetLemmatizer


def gensim_analysis(list_responses, q_count):
    """Completes the analysis for each answer"""
    warnings.filterwarnings('ignore')
    tokens = create_tokens(list_responses)
    dictionary = dictionary_create(tokens)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    # print(corpus)
    corp_eval(dictionary, tokens, corpus, q_count)

    logging.info("Analyzes gensim and returns the repeated words")


def create_tokens(list_responses):
    """Takes in the list of responses and makes each word a token"""
    stoplist = get_stop_words('en')
    texts = []
    tokens = []
    for i in list_responses[1:]:
        texts.append(i.lower())
    texts = [[word for word in document.split()]
             for document in texts]
    for i in texts:
        if len(i) > 2:
            temp = []
            for i in i:
                if profanity.contains_profanity(i) is False:
                    if i not in stoplist:
                        temp.append(i)
            tokens.append(temp)
    # print(tokens)
    return(tokens)

    logging.info("creates tokens from the responses")


def dictionary_create(tokens):
    """Creates the dictionary from the tokens of the answer"""
    dictionary = corpora.Dictionary(tokens)
    #corpus = [dictionary.doc2bow(token) for token in tokens]
    # print(dictionary.token2id)
    # print(corpus)
    # print(dictionary)
    # print(corpus)
    logging.info("creates a dictionary using the tokens")
    return(dictionary)


def corp_eval(dictionary, tokens, corpus, q_count):
    i = len(tokens)
    lda = gensim.models.ldamodel.LdaModel(
        corpus,
        id2word=dictionary,
        num_topics=3,
        passes=1,
        alpha='symmetric',
        eta=None)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    # print(dictionary.token2id)
    # print(viewitems(dictionary.dfs))
    print(
        Fore.GREEN +
        "This is the lda analysis for Question: ",
        q_count,
        Style.RESET_ALL)
    print(lda)
    vis = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
    print(Fore.YELLOW + "These are the current topics:" + Style.RESET_ALL)
    print(lda.print_topics(i))
    print(
        Fore.CYAN +
        "Showing the lda visually, please hit control+c to access the next set of responses:",
        Style.RESET_ALL)
    pyLDAvis.show(vis)
    logging.info("Evaluates the dictionary to see if words are repeated")
    return(dictionary.dfs)
