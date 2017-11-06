"""Use gensim to analyze the text of the responses to the Edurate evaluation."""

from gensim import corpora
from profanity import profanity
from stop_words import get_stop_words
from six import viewitems
from colorama import Fore, Style
import logging
import pyLDAvis
import pyLDAvis.gensim
import gensim
import warnings


def gensim_analysis(list_responses, q_count):
    """Complete the analysis for each answer."""
    warnings.filterwarnings('ignore')
    tokens = create_tokens(list_responses)
    dictionary = dictionary_create(tokens)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    # print(corpus)
    corp_eval(dictionary, tokens, corpus, q_count)

    logging.info("Analyzes gensim and returns the repeated words")


def create_tokens(list_responses):
    """Take in the list of responses and make each word a token."""
    logging.info("Creating tokens")
    stoplist = get_stop_words('en')
    tokens = []

    for res in list_responses:
        temp = []
        for word in res.split():
            if not isinstance(word, int) and not profanity.contains_profanity(word) and word not in stoplist:
                temp.append(word)
        if len(temp) > 0:
            tokens.append(temp)

    return tokens


def dictionary_create(tokens):
    """Create the dictionary from the tokens of the answer."""
    dictionary = corpora.Dictionary(tokens)

    logging.info("Created a dictionary using the tokens")
    return(dictionary)


def corp_eval(dictionary, tokens, corpus, q_count):
    """Evaluate the corpus and produce gensim visualization."""
    i = len(tokens)
    lda = gensim.models.ldamodel.LdaModel(
        corpus,
        id2word=dictionary,
        num_topics=3,
        passes=1,
        alpha='symmetric',
        eta=None)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    logging.debug(dictionary.token2id)
    logging.debug(viewitems(dictionary.dfs))

    print(
        Fore.GREEN +
        "Producing LDA analysis for question: ",
        q_count,
        Style.RESET_ALL)
    print(lda)
    vis = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
    print(Fore.YELLOW + "These are the current topics: " + Style.RESET_ALL)
    print(lda.print_topics(i))
    print(
        Fore.CYAN +
        "Showing the LDA visually, please hit CTRL+C to move to the next question:",
        Style.RESET_ALL)
    pyLDAvis.show(vis)
    logging.info("Evaluated the dictionary to see if words are repeated")
    return dictionary.dfs
