# Test cases for the create_tokens() function
# that is found in edurate_gensim.py
# To run these test suites type the following
# into the command line when in the tests/ directory:
# pytest test_create_tokens.py


import glob
import os
import edurate_gensim
from flake8.api import legacy as flake8


def test_create_tokens_with_no_repeating_words():
    """Testing that the create_tokens function will create tokens
        from a list of strings. A given word must have a length
        of at least 3 characters to be considered a token. In this
        test, we have zero repeating words"""
    list_responses = ['I am testing', 'this is a test', 'make my tokens']
    check = edurate_gensim.create_tokens(list_responses)
    assert check == [['testing'], ['test'], ['make', 'tokens']]
    assert ("am" in check) is False
    assert ("my" in check) is False


def test_create_tokens_with_repeating_words():
    """Testing the create_tokens function works properly when
        given a list with repeating words."""
    list_responses = ['I am testing', 'testing testing testing', 'make my tokens']
    check = edurate_gensim.create_tokens(list_responses)
    assert check == [['testing'], ['testing', 'testing', 'testing'], ['make', 'tokens']]
    assert ("I" in check) is False
    assert ("am" in check) is False
    assert ("my" in check) is False


def test_create_tokens_with_profanity():
    """Testing that the create_tokens function will not create
        a token from profanity"""
    list_responses = ['test this code', ' for bad words', 'such as shit']
    check = edurate_gensim.create_tokens(list_responses)
    assert check == [['test', 'code'], ['bad', 'words']]
    assert ("shit" in check) is False


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
