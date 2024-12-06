*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
After pressing bibtex-button opens bibtex-page
    Go To Add Reference Page
    Input Text  author  Test Author1
    Input Text  title  Test Title1
    Input Text  booktitle  Test Book title1
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Click Button  Export BibTeX
    Page Should Contain  BibTeX Representation

Pressing bibtex-button generates citekey
    Go To Add Reference Page
    Input Text  author  Test Author
    Input Text  title  Test Title
    Input Text  booktitle  Test Book title
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Click Button  Export BibTeX
    Page Should Contain  Author2020TestTitle

BibTeX can be copied to clipboard
    Go To Add Reference Page
    Input Text  author  Test Author
    Input Text  title  Test Title
    Input Text  booktitle  Test Book title
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Click Button  Export BibTeX
    Page Should Contain  BibTeX Representation
    Copy to clipboard
    Handle Alert
    Go To Add Reference Page
    Click Element  author
    Paste Text
    Textfield Should Contain  author  Author2020TestTitle

After pressing Export all-button opens bibtex-page
    Go To Add Reference Page
    Input Text  author  Test Author1
    Input Text  title  Test Title1
    Input Text  booktitle  Test Book title1
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1
    Go To Add Reference Page
    Input Text  author  Test Author2
    Input Text  title  Test Title2
    Input Text  booktitle  Test Book title2
    Input Text  year  2022
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 2

    Click Button  Export all
    Page Should Contain  BibTeX Representation
    Page Should Contain  Test Author1
    Page Should Contain  Test Author2

BibTeXs can be copied to clipboard
    Go To Add Reference Page
    Input Text  author  Test Author1
    Input Text  title  Test Title1
    Input Text  booktitle  Test Book title1
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1
    Go To Add Reference Page
    Input Text  author  Test Author2
    Input Text  title  Test Title2
    Input Text  booktitle  Test Book title2
    Input Text  year  2022
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 2

    Click Button  Export all
    Page Should Contain  BibTeX Representation
    Copy to clipboard
    Handle Alert
    Go To Add Reference Page
    Click Element  author
    Paste Text
    Textfield Should Contain  author  Author2020TestTitle
    Textfield Should Contain  author  Author2022TestTitle


*** Keywords ***
Main Page Should Be Open
    Title Should Be  Reference app

New Reference Page Should Be Open
    Title Should Be  Create a new reference

Go To Home Page
    Go To  ${HOME_URL}

Go To Add Reference Page
    Go To  ${ADD_REFERENCE_URL}

Submit Reference
    Click Button  Create

Submit Should Succeed
    Main Page Should Be Open

Submit Should Fail With Message
    [Arguments]  ${message}
    New Reference Page Should Be Open
    Page Should Contain  ${message}

Copy to clipboard
    Click Button  Copy to Clipboard

Paste Text
    Press Keys  None  CTRL+v