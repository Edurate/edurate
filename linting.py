
# Run pytest linting.py to run the program and check code
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


# Linting Tests
def test_flake8():

    # list of all file names to be checked for PEP8
    filenames = list()

    # fill list with all python files found in all subdirectories
    for root, dirs, files in os.walk("edurate", topdown=False):
        pyFiles = glob.glob(root + "/*.py")
        filenames.extend(pyFiles)

    style_guide = flake8.get_style_guide(ignore=["E265", "E501"])
    report = style_guide.check_files(filenames)
    assert report.get_statistics('E') == [], 'Flake8 found violations'
