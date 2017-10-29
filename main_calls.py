import argparse
import os
importsys

import edurate_gensim

DEFAULT_TOPIC_NUMBER = 3
DEFAULT_PASS_NUMBER = 10

SYMMETRIC = "symmetric"
ASYMMETRIC = "asymmetric"
AUTO = "auto"


DEFAULT_ALPHA = SYMMETRIC
DEFAULT_ETA = SYMMETRIC

    edurate_parser.add_argument(
        "--num-topics",
        help="Topics in the LDA model",
        type=int,
        default=DEFAULT_TOPIC_NUMBER,
        required=False)

    edurate_parser.add_argument(
        "--num-passes",
        help="Passes when creating the LDA model",
        type=int,
        default=DEFAULT_PASS_NUMBER,
        required=False)

    edurate_parser.add_argument(
        "--alpha",
        help="Alpha when creating the LDA model",
        choices=[AUTO, ASYMMETRIC, SYMMETRIC],
        default=DEFAULT_ALPHA,
        required=False)

    edurate_parser.add_argument(
        "--eta",
        help="Eta when creating the LDA model",
        choices=[AUTO, SYMMETRIC],
        default=DEFAULT_ETA,
        required=False)
        
 def perform_gensim_analysis(edurate_arguments, response_list):
    """ Use edurate_gensim functions to create and analyze a topic model """
    if edurate_arguments.num_topics is not None:
        num_topics_requested = edurate_arguments.num_topics
    else:
        num_topics_requested = DEFAULT_TOPIC_NUMBER
    gensim_topic_model, topic_model_corpus, topic_model_dictionary, texts_to_analyze = edurate_gensim.create_topic_model(
        edurate_arguments, response_list)
    edurate_gensim.show_topic_model_textually(
        gensim_topic_model,
        topic_model_corpus,
        texts_to_analyze,
        num_topics=num_topics_requested)
        
        edurate_arguments = edurate_parser.parse_args(args)
    return edurate_arguments, seed_parser
        
   if __name__ == '__main__':
   
   elif edurate_arguments.analyze_facts is True:
              edurate_dictionary_list = seed_download.seed_load()                               #The next two lines are where we will 
              fact_response_list = edurate_create.create_fact_answer_list(seed_dictionary_list) #add the data to be analyzed 
 -            print(fact_response_list)
 +            edurate_gensim.create_topic_model(fact_response_list)
