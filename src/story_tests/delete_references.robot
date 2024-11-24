*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
After pressing delete-button the counter in the main page should decrease by one
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
    Input Text  year  1920
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 2
    Page Should Contain  Test Title1
    Page Should Contain  Test Book title2

    Click Button  Delete
    Page Should Contain  Saved references: 1

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