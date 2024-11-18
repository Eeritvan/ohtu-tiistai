*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset References

*** Test Cases ***
At start there are no references
    Go To Main Page
    Main Page Should Be Open
    Page Should Contain  Saved references: 0

Click New Reference Link
    Go To Main Page
    Click Link  Create new reference
    New Reference Page Should Be Open

*** Keywords ***
Go To Main Page
    Go To  ${HOME_URL}

Main Page Should Be Open
    Title Should Be  Reference app

New Reference Page Should Be Open
    Title Should Be  Create a new reference
