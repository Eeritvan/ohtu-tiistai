*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
After each added reference the counter in the main page should increase by one
    Add New Valid Reference  Test Author1  Test Title1  Test Book title1  2020
    Submit Should Succeed
    Page Should Contain  Saved references: 1
    Add New Valid Reference  Test Author2  Test Title2  Test Book title2  1920
    Submit Should Succeed
    Page Should Contain  Saved references: 2
    Page Should Contain  Test Title1
    Page Should Contain  Test Book title2

Adding Duplicate Title Should Fail
    Add New Valid Reference  Test  Test  Test  2020
    Submit Should Succeed
    Page Should Contain  Saved references: 1
    Add New Valid Reference  Test  Test  Test  2020
    Submit Should Fail With Message  Title 'Test' already exists
    Go To Home Page
    Page Should Contain  Saved references: 1

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

Adding Too Short Author Should Fail
    Go To Add Reference Page
    Input Text  author  ab
    Input Text  title  Too Short
    Input Text  booktitle  Too Short
    Input Text  year  1920
    Submit Reference
    Submit Should Fail With Message  Reference author length must be greater than 3

Adding Too Short Title Should Fail
    Go To Add Reference Page
    Input Text  author  Too Short
    Input Text  title  ab
    Input Text  booktitle  Too Short
    Input Text  year  1920
    Submit Reference
    Submit Should Fail With Message  Reference title length must be greater than 3

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

Add New Valid Reference
    [Arguments]  ${author}  ${title}  ${booktitle}  ${year}
    Go To Add Reference Page
    Input Text  name=author  ${author}
    Input Text  name=title  ${title}
    Input Text  name=booktitle  ${booktitle}
    Input Text  name=year  ${year}
    Submit Reference