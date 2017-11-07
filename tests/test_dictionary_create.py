# Test cases for the dictionary_create() function
# and the corp_eval() function both found in
# edurate_gensim.py
# To run these test suites type the following
# into the command line when in the tests/ directory:
# pytest test_dictionary_create.py


import glob
import os
import edurate_gensim
from flake8.api import legacy as flake8


def test_dictionary_create_none_repeat():
    """Testing that the dictionary_create() function will keep
        track of the number of times a particular word occurs.
        In this test, every word has a frequency of 1"""
    tokens = [['testing'], ['test'], ['make', 'tokens']]
    dictionary = edurate_gensim.dictionary_create(tokens)
    corp = [dictionary.doc2bow(token) for token in tokens]
    assert corp == [[(0, 1)], [(1, 1)], [(2, 1), (3, 1)]]


def test_dictionary_create_repeat():
    """Testing that the dictionary_create() function works
        properly when given repeating tokens"""
    tokens = [['testing'], ['testing', 'testing', 'testing'], ['make', 'tokens']]
    dictionary = edurate_gensim.dictionary_create(tokens)
    corp = [dictionary.doc2bow(token) for token in tokens]
    assert corp == [[(0, 1)], [(0, 3)], [(1, 1), (2, 1)]]


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
