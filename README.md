
# Edurate

Edurate is a professor evaluation program written to help professors gather
information throughout the semester in order to help them better their courses
and see where their students are struggling. Users need only send out
questionnaires and, once submitted, Edurate will read in the text files and
output information on where students are struggling. Edurate will save and
time stamp questionnaires so that each time it is run during a given semester
improvement can be seen.

## Installation

Edurate is a python 3 program and, therefore, uses
[pip](https://pip.pypa.io/en/stable/installing/) for installation. Type the
three following commands before running the program.

```
pip3 install --upgrade pip
```

```
pip3 install -r requirements.txt
```

```
python3 -m pip install --user gspreed oauth2client
```

Then, create a Google Sheet and a Google Form in Google Drive. In the form
create questions that allows your students to provide information about how
they feel about the teaching and the class. After you have received one
submission from the Form, go to the response tab and click the green icon with
the white cross through it. This will allow you to link the Sheet to the Form.
You can create a new Sheet or link said Sheet to a pre-existing form.

---

## Usage

Edurate analyzes professor and course questionnaires in using natural language
processing to detect the most common problems.  Consequently, it outputs them
into an LDavis visualization. To run the program and output LDavis
visualization, use the following command:

```
python3 edurate.py
```

## Analysis

Please see further information on how the LDavis visualization works and how
you can interpret its results at EdurateLDavis_Analysis.md

### Spam Filter

Edurate's spam filter removes profanities and sets aside unhelpful comments.

### Evolution

Edurate is open to evolution. Its initial questionnaire can be edited by
professors who wish to add or remove questions.

### Archive Information

Information is dumped to a rsv file in case of any crash so that professors may
download all the information to their computer or external hard drive.

### Confidentiality

Edurate has a confidentiality option. Before sending out the questionnaires the
professor will decide if the form should be confidential or not. If it is not
confidential, email addresses will be recorded. If it is confidential, they
will not.

---

## Testing

### Functions Tested

The test suite verifies Edurate's functions. The first function that is tested
is to make sure that the questionnaires are properly downloaded and transferred
into a usable spreadsheet. Then all argparsers are verified.

### Running the Test Suite

To run the test suite, run the following commands in the root directory of
Edurate.

```
pytest tests
```

### Automatic Linting

The linting automatically checks to ensure code is up to pep8 standards.
If linting errors occur, run the following command to perform automatic linting.
If there are errors that the tool cannot fix, the test suite will tell you
where and what the errors are so that you may go to the location and fix them.

```
autopep8 --in-place  --aggressive --aggressive  *.py
```

### Test Coverage

Test coverage is being addressed by Coveralls so that when Travis-CI runs, it
can evaluate the coverage of the test suite.

### Activating Travis-CI

Travis can only be implemented by admin accounts. Admin users can activate
Travis by creating a .travis.yml file in the project's root directory.

---

## Questions or Comments

Any problems regarding Edurate can be written in the issues link at the top of
the site.
