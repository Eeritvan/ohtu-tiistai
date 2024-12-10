*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
After pressing delete-button the counter in the main page should decrease by one
    Go To Add Reference Page
    Select Reference Type  inproceedings
    Input Text  author  Test Author1
    Input Text  title  Test Title1
    Input Text  booktitle  Test Book title1
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Go To Add Reference Page
    Select Reference Type  inproceedings
    Input Text  author  Test Author2
    Input Text  title  Test Title2
    Input Text  booktitle  Test Book title2
    Input Text  year  1920
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 2
    Page Should Contain  Test Title1
    Page Should Contain  Test Book title2

    Click Button  Delete
    Page Should Contain  Saved references: 1

    Go To Add Reference Page
    Select Reference Type  book
    Input Text  author  Test Author3
    Input Text  title  Test Title3
    Input Text  year  2000
    Input Text  publisher  Test Publisher3
    Input Text  address  Test Address3
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 2
    Page Should Contain  Test Title2
    Page Should Contain  Test Publisher3

    Click Button  Delete
    Click Button  Delete
    Page Should Contain  Saved references: 0

    Go To Add Reference Page
    Select Reference Type  article
    Input Text  author  Test Author4
    Input Text  title  Test Title4
    Input Text  year  2020
    Input Text  journal  Test Journal4
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1
    Page Should Contain  Test Journal4

    Click Button  Delete
    Page Should Contain  Saved references: 0

*** Keywords ***
Main Page Should Be Open
    Title Should Be  Reference app

New Reference Page Should Be Open
    Title Should Be  Create a new reference

Go To Home Page
    Go To  ${HOME_URL}

Go To Add Reference Page
    Go To  ${ADD_REFERENCE_URL}

Select Reference Type
    [Arguments]  ${reference_type}
    Select From List By Value  id=ref_types  ${reference_type}
    Click Button  name=select_type_submit

Submit Reference
    Click Button  Create

Submit Should Succeed
    Main Page Should Be Open

Submit Should Fail With Message
    [Arguments]  ${message}
    New Reference Page Should Be Open
    Page Should Contain  ${message}