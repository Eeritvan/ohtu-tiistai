*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***

User can search references by authors name
    Go To Add Reference Page
    Select Reference Type  inproceedings
    Input Text  author  Test Author
    Input Text  title  Test Title
    Input Text  booktitle  Test Book title
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Go To Add Reference Page
    Select Reference Type  inproceedings
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
    Select Reference Type  inproceedings
    Input Text  author  First Author
    Input Text  title  First Title
    Input Text  booktitle  First Book title
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Go To Add Reference Page
    Select Reference Type  article
    Input Text  author  Test Author2
    Input Text  title  Test Title2
    Input Text  year  1970
    Input Text  journal  Test Journal2
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 2

    Go To Search Page
    Input Text  title  Test Title2
    Submit Search
    Page Should Contain  Matching references: 1
    Page Should Contain  Test Author2
    Page Should Contain  Test Title2

User can search references by year
    Go To Add Reference Page
    Select Reference Type  inproceedings
    Input Text  author  First Author
    Input Text  title  First Title
    Input Text  booktitle  First Book title
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Go To Add Reference Page
    Select Reference Type  inproceedings
    Input Text  author  Second Author
    Input Text  title  Second Title
    Input Text  booktitle  Second Book title
    Input Text  year  1920
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 2

    Go To Add Reference Page
    Select Reference Type  book
    Input Text  author  Test Author3
    Input Text  title  Test Title3
    Input Text  year  2000
    Input Text  publisher  Test Publisher
    Input Text  address  Test Address
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 3

    Go To Search Page
    Input Text  year  2000
    Submit Search
    Page Should Contain  Matching references: 1
    Page Should Contain  Test Author3
    Page Should Contain  Test Title3

User can search references by type
    Go To Add Reference Page
    Select Reference Type  inproceedings
    Input Text  author  First Author
    Input Text  title  First Title
    Input Text  booktitle  First Book title
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Go To Add Reference Page
    Select Reference Type  inproceedings
    Input Text  author  Second Author
    Input Text  title  Second Title
    Input Text  booktitle  Second Book title
    Input Text  year  1920
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 2

    Go To Add Reference Page
    Select Reference Type  book
    Input Text  author  Test Author3
    Input Text  title  Test Title3
    Input Text  year  2000
    Input Text  publisher  Test Publisher
    Input Text  address  Test Address
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 3

    Go To Add Reference Page
    Select Reference Type  article
    Input Text  author  Test Author4
    Input Text  title  Test Title4
    Input Text  year  1970
    Input Text  journal  Test Journal
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 4

    Go To Search Page
    Input Text  ref_type  inproceedings
    Submit Search
    Page Should Contain  Matching references: 2
    Page Should Contain  First Author
    Page Should Contain  Second Title
    Page Should Contain  inproceedings

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

Select Reference Type
    [Arguments]  ${reference_type}
    Select From List By Value  id=ref_types  ${reference_type}
    Click Button  name=select_type_submit

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