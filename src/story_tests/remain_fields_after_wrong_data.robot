*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Wrong data does not reset the form
    Go To Add Reference Page
    Input Text  author  xx
    Input Text  title  Test Title1
    Input Text  booktitle  Test Book title1
    Input Text  year  2020
    Submit Reference
    Submit Should Fail With Message  Reference author length must be greater than 3

    Text Field Value Should Be  author  xx
    Text Field Value Should Be  title  Test Title1
    Text Field Value Should Be  booktitle  Test Book title1
    Text Field Value Should Be  year  2020

*** Keywords ***
New Reference Page Should Be Open
    Title Should Be  Create a new reference

Go To Add Reference Page
    Go To  ${ADD_REFERENCE_URL}

Submit Reference
    Click Button  Create

Submit Should Fail With Message
    [Arguments]  ${message}
    New Reference Page Should Be Open
    Page Should Contain  ${message}