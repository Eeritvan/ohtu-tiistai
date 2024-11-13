*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
At start there are no references
    Go To  ${HOME_URL}
    Title Should Be  Reference app
    Page Should Contain  Saved references: 0

After adding a reference, there is one
    Go To  ${HOME_URL}
    Click Link  Create new reference
    Input Text  author  Author milk
    Input Text  title  Buy milk
    Input Text  booktitle  Booktitle milk
    Input Text  year  2022
    Click Button  Create
    Page Should Contain  Saved references: 1
    Page Should Contain  Buy milk

After adding two references and marking one done, there is 2
    Go To  ${HOME_URL}
    Click Link  Create new reference
    Input Text  author  Author milk
    Input Text  title  Buy milk
    Input Text  booktitle  Booktitle milk
    Input Text  year  2020
    Click Button  Create
    Click Link  Create new reference
    Input Text  author  Author house
    Input Text  title  Clean house
    Input Text  year  1920
    Input Text  booktitle  Booktitle house
    Click Button  Create
#    Click Button  //li[div[contains(text(), 'Buy milk')]]/form/button
    Page Should Contain  Saved references: 2
    Page Should Contain  Buy milk