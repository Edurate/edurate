# Run pytest tests to run the program and check code
# Install autopep8 and pep8
# pip install autopep8
# pip install pep8
# pip install pytest-flake8
# To fix many issues, type the following into the terminal
# autopep8 --in-place  --aggressive --aggressive  *.py
# If it still fails, go to the code that is specified and change it
import glob
import os
from flake8.api import legacy as flake8
import parse_arguments
import logging
import edurate_gensim
import gensim


def test_parse_arguments1():
    args = []
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.logging_level == logging.ERROR


def test_parse_arguments2():
    args = ['--file', 'data.csv', '--debug']
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.file == 'data.csv'
    assert parsed_args.logging_level == logging.DEBUG


def test_parse_arguments3():
    args = ['--file', 'data.csv', '--confidential']
    parsed_args = parse_arguments.parse_arguments(args)
    assert parsed_args.confidential


# Linting Tests
def test_flake8():

    # list of all file names to be checked for PEP8
    filenames = list()

    # fill list with all python files found in all subdirectories
    for root, dirs, files in os.walk("edurate", topdown=False):
        pyFiles = glob.glob(root + "/*.py")
        filenames.extend(pyFiles)

    style_guide = flake8.get_style_guide(ignore=["E265", "E501", "F405"])
    report = style_guide.check_files(filenames)
    assert report.get_statistics('E') == [], 'Flake8 found violations'


def test_create_tokens_none_repeat():
    list_responses = ['I am testing', 'this is a test', 'make my tokens']
    check = edurate_gensim.create_tokens(list_responses)
    assert check == [['testing'], ['test'], ['make', 'tokens']]


def test_create_tokens_repeated():
    list_responses = ['I am testing', 'testing testing testing', 'make my tokens']
    check = edurate_gensim.create_tokens(list_responses)
    print(check)
    assert check == [['testing'], ['testing', 'testing', 'testing'], ['make', 'tokens']]


def test_dictionary_create_none_repeat():
    tokens = [['testing'], ['test'], ['make', 'tokens']]
    dictionary = edurate_gensim.dictionary_create(tokens)
    corp = [dictionary.doc2bow(token) for token in tokens]
    assert corp == [[(0, 1)], [(1, 1)], [(2, 1), (3, 1)]]


def test_dictionary_create_repeat():
    tokens = [['testing'], ['testing', 'testing', 'testing'], ['make', 'tokens']]
    dictionary = edurate_gensim.dictionary_create(tokens)
    corp = [dictionary.doc2bow(token) for token in tokens]
    print(corp)
    assert corp == [[(0, 1)], [(0, 3)], [(1, 1), (2, 1)]]


def test_corp_eval_none():
    tokens = [['testing'], ['test'], ['make', 'tokens']]
    dictionary = edurate_gensim.dictionary_create(tokens)
    dict = edurate_gensim.corp_eval(dictionary, tokens)
    assert dict == {}


def test_corp_eval_none():
    tokens = [['testing'], ['testing', 'testing', 'testing'], ['make', 'tokens']]
    dictionary = edurate_gensim.dictionary_create(tokens)
    dict = edurate_gensim.corp_eval(dictionary, tokens)
    print(dict)
    assert dict == {0: 2}
