*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***

User can search references by authors name
    Go To Add Reference Page
    Input Text  author  Test Author
    Input Text  title  Test Title
    Input Text  booktitle  Test Book title
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Go To Add Reference Page
    Input Text  author  Writer
    Input Text  title  Test Title2
    Input Text  booktitle  Test Book title2
    Input Text  year  1920
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 2
    Page Should Contain  Test Title
    Page Should Contain  Test Book title2

    Go To Search Page
    Input Text  author  Writer
    Submit Search
    Page Should Contain  Matching references: 1

User can search references by title
    Go To Add Reference Page
    Input Text  author  First Author
    Input Text  title  First Title
    Input Text  booktitle  Test Book title
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Go To Add Reference Page
    Input Text  author  Second Author
    Input Text  title  Second Title
    Input Text  booktitle  Test Book title2
    Input Text  year  1920
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 2

    Go To Search Page
    Input Text  title  Second Title
    Submit Search
    Page Should Contain  Matching references: 1
    Page Should Contain  Second Author
    Page Should Contain  Second Title

User can search references by year
    Go To Add Reference Page
    Input Text  author  First Author
    Input Text  title  First Title
    Input Text  booktitle  First Book title
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Go To Add Reference Page
    Input Text  author  Second Author
    Input Text  title  Second Title
    Input Text  booktitle  Second Book title
    Input Text  year  1920
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 2

    Go To Add Reference Page
    Input Text  author  Third Author
    Input Text  title  Third Title
    Input Text  booktitle  Third Book title
    Input Text  year  1928
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 3

    Go To Search Page
    Input Text  year  1920
    Submit Search
    Page Should Contain  Matching references: 1
    Page Should Contain  Second Author
    Page Should Contain  Second Title

User can search references by booktitle
    Go To Add Reference Page
    Input Text  author  First Author
    Input Text  title  First Title
    Input Text  booktitle  First Book title
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Go To Add Reference Page
    Input Text  author  Second Author
    Input Text  title  Second Title
    Input Text  booktitle  Second Book title
    Input Text  year  1920
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 2

    Go To Add Reference Page
    Input Text  author  Third Author
    Input Text  title  Third Title
    Input Text  booktitle  Third Book title
    Input Text  year  1928
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 3

    Go To Search Page
    Input Text  booktitle  Second Book title
    Submit Search
    Page Should Contain  Matching references: 1
    Page Should Contain  Second Author
    Page Should Contain  Second Title
    Page Should Contain  Second Book title

*** Keywords ***
Main Page Should Be Open
    Title Should Be  Reference app

New Reference Page Should Be Open
    Title Should Be  Create a new reference

Go To Home Page
    Go To  ${HOME_URL}

Go To Add Reference Page
    Go To  ${ADD_REFERENCE_URL}

Go To Search Page
    Go To  ${SEARCH_REF}

Submit Reference
    Click Button  Create

Submit Search
    Click Button  Search

Submit Should Succeed
    Main Page Should Be Open

Submit Should Fail With Message
    [Arguments]  ${message}
    New Reference Page Should Be Open
    Page Should Contain  ${message}