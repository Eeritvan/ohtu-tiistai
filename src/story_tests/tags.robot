*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***

User Can Create A Tag
    Go To Tags Page
    Input Text  name  Test Tag
    Create Tag
    Page Should Contain  Test Tag

User Can Delete A Tag
    Go To Tags Page
    Input Text  name  Test Tag
    Create Tag
    Page Should Contain  Test Tag
    Click Button  Delete
    Page Should Contain  Tag 'Test Tag' deleted successfully

#User Can Attach a Tag To The Reference

#User Can Search By Tag

#Tags Use Different Colors

*** Keywords ***
Main Page Should Be Open
    Title Should Be  Reference app

New Reference Page Should Be Open
    Title Should Be  Create a new reference

Go To Home Page
    Go To  ${HOME_URL}

Go To Tags Page
    Go To  ${TAGS_URL}

Go To Add Reference Page
    Go To  ${ADD_REFERENCE_URL}

Create Tag
     Click Button  Create

Select Tag
    [Arguments]  ${selected_tag}
    Select From List By Value  id=tags  ${selected_tag}
    Click  Element ${selected_tag}

Select Reference Type
    [Arguments]  ${reference_type}
    Select From List By Value  id=ref_types  ${reference_type}
    Click Button  name=select_type_submit
