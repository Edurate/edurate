
# Edurate

Edurate is a professor evaluation program written to help professors gather
information throughout the semester in order to help them better their courses
as see where their students are struggling. Users need only send out
questionnaires and, once submitted, Edurate will read in the text files and
output information on where students are struggling. Edurate will save and time
stamp questionnaires so that each time it is run during a given semester
improvement can be seen.

## Installation

Edurate is a python 3 program and, therefore, uses [pip](https://pip.pypa.io/en/stable/installing/)
for instillation. Type the following commands before running.

```shell
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

---

## Usage

Edurate analysis professor/course questionnaires and uses natural language
processing detect the most common problems and output them into the terminal.

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

```shell
pytest tests
```

### Automatic Linting

The linting automatically checks to ensure code is up to pep8 standards.
If linting errors occur, run the following command to perform automatic linting.
If there are errors that the tool cannot fix, the test suite will tell you
where and what the errors are so that you may go to the location and fix them.

```shell
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
