*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
After each added reference the counter in the main page should increase by one
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

Filling Each Input Should Succeed
    Go To Add Reference Page
    Input Text  author  Test Author
    Input Text  title  Test Title
    Input Text  booktitle  Test Book title
    Input Text  year  2020
    Input Text  editor  Test Editor
    Input Text  volume  12
    Input Text  number  12
    Input Text  series  Test Series
    Input Text  pages  Test Pages
    Input Text  address  Test Address
    Input Text  month  12
    Input Text  organisation  Test Organisation
    Input Text  publisher  Test Publisher
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Test Editor
    Page Should Contain  12
    Page Should Contain  Test Organisation

*** Keywords ***
Go To Add Reference Page
    Go To  ${ADD_REFERENCE_URL}

Submit Reference
    Click Button  Create

Main Page Should Be Open
    Title Should Be  Reference app

Submit Should Succeed
    Main Page Should Be Open

Submit Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}