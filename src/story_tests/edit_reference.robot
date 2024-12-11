*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
Adding Reference And Editing Title Should Succeed
    Go To Add Reference Page
    Select Reference Type  inproceedings
    Input Text  author  Test Author1
    Input Text  title  Test Title1
    Input Text  booktitle  Test Book title1
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Enter edit
    Editing Page Should Be Open
    Input Text  title  Updated Title1
    Submit Edit
    Page Should Contain  Saved references: 1
    Page Should Contain  Updated Title1
    Click Button  Delete

    Go To Add Reference Page
    Select Reference Type  book
    Input Text  author  Test Author2
    Input Text  title  Test Title2
    Input Text  year  2000
    Input Text  publisher  Test Publisher2
    Input Text  address  Test Address2
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Enter edit
    Editing Page Should Be Open
    Input Text  title  Updated Title2
    Submit Edit
    Page Should Contain  Saved references: 1
    Page Should Contain  Updated Title2
    Click Button  Delete

    Go To Add Reference Page
    Select Reference Type  article
    Input Text  author  Test Author3
    Input Text  title  Test Title3
    Input Text  year  2020
    Input Text  journal  Test Journal3
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Enter edit
    Editing Page Should Be Open
    Input Text  title  Updated Title3
    Submit Edit
    Page Should Contain  Saved references: 1
    Page Should Contain  Updated Title3

Adding Reference And Adding Series Through Editing Should Succeed
    Go To Add Reference Page
    Select Reference Type  inproceedings
    Input Text  author  Test Author1
    Input Text  title  Test Title1
    Input Text  booktitle  Test Book title1
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Enter edit
    Editing Page Should Be Open
    Input Text  series  Test Series
    Submit Edit
    Page Should Contain  Saved references: 1
    Page Should Contain  Test Series

Adding Reference And Adding Note Through Editing Should Succeed
    Go To Add Reference Page
    Select Reference Type  article
    Input Text  author  Test Author1
    Input Text  title  Test Title1
    Input Text  year  2020
    Input Text  journal  Test Journal1
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Enter edit
    Editing Page Should Be Open
    Input Text  note  Test Note
    Submit Edit
    Page Should Contain  Saved references: 1
    Page Should Contain  Test Note

Adding Reference And Editing Wrong Data Should Fail
    Go To Add Reference Page
    Select Reference Type  inproceedings
    Input Text  author  Test Author1
    Input Text  title  Test Title1
    Input Text  booktitle  Test Book title1
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Enter edit
    Editing Page Should Be Open
    Clear Element Text  title
    Submit Edit
    Submit Should Fail With Message  Reference title length must be greater than 1

    Go To Add Reference Page
    Select Reference Type  book
    Input Text  author  Test Authorjdlkwajdljwa
    Input Text  title  Test Titledljwadlkjwa
    Input Text  year  2000
    Input Text  publisher  Test Publisherwajdwadja
    Input Text  address  Test Addresswajdwaldjwa
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 2

    Enter edit
    Editing Page Should Be Open
    Clear Element Text  title
    Submit Edit
    Submit Should Fail With Message  Reference title length must be greater than 1

    Go To Add Reference Page
    Select Reference Type  article
    Input Text  author  Test Authorrrr
    Input Text  title  Test Titleeeee
    Input Text  year  2020
    Input Text  journal  Test Journalllll
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 3

    Enter edit
    Editing Page Should Be Open
    Clear Element Text  title
    Submit Edit
    Submit Should Fail With Message  Reference title length must be greater than 1

Adding Inproceedings And Editing Wrong Data Should Retain Data
    Go To Add Reference Page
    Select Reference Type  inproceedings
    Input Text  author  Test Author1rr
    Input Text  title  Test Title1ee
    Input Text  booktitle  Test Book title1book
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Enter edit
    Editing Page Should Be Open
    Clear Element Text  title
    Submit Edit
    Submit Should Fail With Message  Reference title length must be greater than 1
    Text Field Value Should Be  author  Test Author1rr
    Text Field Value Should Be  booktitle  Test Book title1book
    Text Field Value Should Be  year  2020


Adding Book And Editing Wrong Data Should Retain Data
    Go To Add Reference Page
    Select Reference Type  book
    Input Text  author  Test Author2qweiu
    Input Text  title  Test Title2qweoiu
    Input Text  year  2000
    Input Text  publisher  Test Publisher2asdlkj
    Input Text  address  Test Address2adslkj
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Enter edit
    Editing Page Should Be Open
    Clear Element Text  title
    Submit Edit
    Submit Should Fail With Message  Reference title length must be greater than 1
    Text Field Value Should Be  author  Test Author2qweiu
    Text Field Value Should Be  year  2000
    Text Field Value Should Be  publisher  Test Publisher2asdlkj


Adding Article And Editing Wrong Data Should Retain Data
    Go To Add Reference Page
    Select Reference Type  article
    Input Text  author  Test Author3testi
    Input Text  title  Test Title3testi
    Input Text  year  2020
    Input Text  journal  Test Journal3testi
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1

    Enter edit
    Editing Page Should Be Open
    Clear Element Text  title
    Submit Edit
    Submit Should Fail With Message  Reference title length must be greater than 1
    Text Field Value Should Be  author  Test Author3testi
    Text Field Value Should Be  year  2020
    Text Field Value Should Be  journal  Test Journal3testi

*** Keywords ***
Main Page Should Be Open
    Title Should Be  Reference app


Editing Page Should Be Open
    Title Should Be  Edit reference

Go To Add Reference Page
    Go To  ${ADD_REFERENCE_URL}

Select Reference Type
    [Arguments]  ${reference_type}
    Select From List By Value  id=ref_types  ${reference_type}
    Click Button  name=select_type_submit

Submit Reference
    Click Button  Create

Submit Edit
    Click Button  Confirm edits

Enter edit
    Click Button  Edit

Submit Should Succeed
    Main Page Should Be Open

Submit Should Fail With Message
    [Arguments]  ${message}
    Editing Page Should Be Open
    Page Should Contain  ${message}