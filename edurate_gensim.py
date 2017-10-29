""" Uses gensim to analyze the text of the responses to the main questions of the SEED Survey """

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models
import gensim
import pyLDAvis.gensim


def create_topic_model(seed_arguments, list_responses):
    """ Using LDA from gensim, create the topic model from the list of responses """
    topic_model_dictionary, texts_to_analyze = create_topic_model_dictionary(
        list_responses)
    # convert tokenized documents into a document-term matrix, or the corpus
    topic_model_corpus = [
        topic_model_dictionary.doc2bow(text) for text in texts_to_analyze
    ]
    # generate LDA model from the texts_to_analyze and the topic_model_dictionary
    lda_model = gensim.models.ldamodel.LdaModel(
        topic_model_corpus,
        id2word=topic_model_dictionary,
        num_topics=seed_arguments.num_topics,
        passes=seed_arguments.num_passes,
        alpha=seed_arguments.alpha,
        eta=seed_arguments.eta)
    return lda_model, topic_model_corpus, topic_model_dictionary, texts_to_analyze


def create_topic_model_dictionary(list_responses):
    """ Create a topic model dictionary from the list of responses """
    # create the objects needed to prepare the dictionary
    tokenizer = RegexpTokenizer(r'\w+')
    en_stop = get_stop_words('en')
    # p_stemmer = PorterStemmer()
    wordnet_lemmatizer = WordNetLemmatizer()
    texts_to_analyze = []
    # loop through the list of responses
    for i in list_responses:
        # clean and tokenize document string
        raw = i.lower()
        tokens = tokenizer.tokenize(raw)
        # remove the stop words from tokens
        keep_tokens = [i for i in tokens if not i in en_stop]
        keep_tokens = [i for i in keep_tokens if not i.isnumeric()]
        keep_tokens = [i for i in keep_tokens if len(i) > 1]
        # stem the tokens
        # stemmed_tokens = [p_stemmer.stem(i) for i in keep_tokens]
        stemmed_tokens = [
            wordnet_lemmatizer.lemmatize(i) for i in keep_tokens
        ]
        # add tokens to list of texts to analyze
        texts_to_analyze.append(stemmed_tokens)
        # turn the tokenized documents into a id <-> term dictionary
        topic_model_dictionary = corpora.Dictionary(texts_to_analyze)
    return topic_model_dictionary, texts_to_analyze


def show_topic_model_textually(seed_gensim_topic_model, seed_gensim_corpus,
                               texts_to_analyze, num_topics):
    """ Using only textual output provide a basic display of the topic model """
    print("alpha =", seed_gensim_topic_model.alpha)
    print(seed_gensim_topic_model)
    print(seed_gensim_topic_model.print_topics(num_topics))
    print()
