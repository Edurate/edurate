
"""Analyze the responses to the Edurate evaluation using Gensim."""

import logging
import warnings
import gensim
from gensim import corpora
from profanity import profanity
from stop_words import get_stop_words
from six import viewitems
from colorama import Fore, Style
import pyLDAvis
import pyLDAvis.gensim
import webbrowser
import inspect


def gensim_analysis(list_responses, q_count, num_of_topics):
    """Complete the analysis for each answer."""
    warnings.filterwarnings('ignore')
    tokens = create_tokens(list_responses)
    dictionary = dictionary_create(tokens)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    # print(corpus)
    corp_eval(dictionary, tokens, corpus, q_count, num_of_topics)

    logging.info("Analyzes gensim and returns the repeated words")


def create_tokens(list_responses):
    """Take in the list of responses and make each word a token."""
    logging.info("Creating tokens")
    stoplist = get_stop_words('en')
    tokens = []

    for res in list_responses:
        temp = []
        for word in res.split():
            if not isinstance(word, int):
                if not profanity.contains_profanity(word):
                    if word not in stoplist:
                        if word != "I":
                            temp.append(word)
        if temp:
            tokens.append(temp)

    return tokens


def dictionary_create(tokens):
    """Create the dictionary from the tokens of the answer."""
    dictionary = corpora.Dictionary(tokens)

    logging.info("Created a dictionary using the tokens")
    return dictionary


def corp_eval(dictionary, tokens, corpus, q_count, num_of_topics):
    """Evaluate the corpus and produce gensim visualization."""
    i = len(tokens)
    lda = gensim.models.ldamodel.LdaModel(
        corpus,
        id2word=dictionary,
        num_topics=num_of_topics,
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
    print(Fore.CYAN +
          "Opening up visualization in a new tab in the browser...",
          Style.RESET_ALL)

    # Writing HTML of visualization to file instead of showing with pyLDAvis show function
    # because the show function starts a server, which allows only one file to be displayed
    # at once.
    vis_html_text = pyLDAvis.prepared_data_to_html(vis)
    vis_html_file_name = "vis" + str(q_count) + ".html"
    vis_html_file = open(vis_html_file_name, "w")
    vis_html_file.write(vis_html_text)

    # Getting path to the edurate_gensim.py module, which is in the same directory
    # as the HTML file. This path will be used to generate the file path to the HTML
    # that is to be displayed.
    MODULE_NAME = "edurate_gensim.py"
    PATH_TO_MODULE = inspect.stack()[0][1]
    # Removing name of module from path so that the path only includes up to the
    # directory where the HTML file is located.
    PATH_TO_HTML = PATH_TO_MODULE[:-len(MODULE_NAME)]
    webbrowser.open("file:///" + PATH_TO_HTML + vis_html_file_name, new=2)

    logging.info("Gensim visualization has been displayed.")
    return dictionary.dfs
