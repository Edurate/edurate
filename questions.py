from oauth2client.service_account import ServiceAccountCredentials

def add_question(url):
    urlSplit = url.split("/")
    formID = urlSplit[5]
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'Edurate_Client.json', scope)
    client = gspread.authorize(creds)
    # Open a form by ID.
    form = FormApp.openById(formID);
    print("Would you like to create a open ended or a multiple choice question? ")
    response = input("Enter a 1 for open ended or a 2 for multiple choice: ")
    if response == 1:
        title = raw_input("Enter a title for the question: ")
        form.addParagraphTextItem()
        .setTitle(title)
    elif response == 2:
        title = raw_input("Enter a title for the question: ")
        #if time will allow them to choose number of multiple choice default = 4
        #numChoices = input("Enter the number of choices for the question: ")
        choice1 = raw_input("Enter first multiple choice answer: ")
        choice2 = raw_input("Enter second multiple choice answer: ")
        choice3 = raw_input("Enter third multiple choice answer: ")
        choice4 = raw_input("Enter fourth multiple choice answer: ")
        form.addMultipleChoiceItem()
        .setTitle(title)
        .setChoiceValues([choice1,choice2,choice3,choice4])
        .showOtherOption(true);

def remove_question(url):
    urlSplit = url.split("/")
    formID = urlSplit[5]
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'Edurate_Client.json', scope)
    client = gspread.authorize(creds)
    # Open a form by ID.
    form = FormApp.openById(formID);
    questionToRemove = raw_input("Enter the title of the question to be removed: ")
    form.deleteItem(questionToRemove)
