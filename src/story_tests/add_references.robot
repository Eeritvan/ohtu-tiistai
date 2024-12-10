*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset References

*** Test Cases ***
After each added reference the counter in the main page should increase by one
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
    Page Should Contain  Test Title1
    Page Should Contain  Test Book title2
    Page Should Contain  Test Publisher
    Page Should Contain  Test Journal

Adding Duplicate Title Should Fail
    Go To Add Reference Page
    Select Reference Type  inproceedings
    Input Text  author  Test
    Input Text  title  Test
    Input Text  booktitle  Test
    Input Text  year  2020
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Saved references: 1
    
    Go To Add Reference Page
    Select Reference Type  inproceedings
    Input Text  author  Test
    Input Text  title  Test
    Input Text  booktitle  Test
    Input Text  year  2020
    Submit Reference
    Submit Should Fail With Message  Title 'Test' already exists
    Go To Home Page
    Page Should Contain  Saved references: 1

    Go To Add Reference Page
    Select Reference Type  book
    Input Text  author  Test
    Input Text  title  Test
    Input Text  year  2000
    Input Text  publisher  Test
    Input Text  address  Test
    Submit Reference
    Submit Should Fail With Message  Title 'Test' already exists
    Go To Home Page
    Page Should Contain  Saved references: 1

    Go To Add Reference Page
    Select Reference Type  article
    Input Text  author  Test
    Input Text  title  Test
    Input Text  year  1970
    Input Text  journal  Test
    Submit Reference
    Submit Should Fail With Message  Title 'Test' already exists
    Go To Home Page
    Page Should Contain  Saved references: 1


Filling Each Input Should Succeed
    Go To Add Reference Page
    Select Reference Type  inproceedings
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

    Go To Add Reference Page
    Select Reference Type  article
    Input Text  author  Test Author2
    Input Text  title  Test Title Article
    Input Text  year  2020
    Input Text  journal  Test Journal
    Input Text  volume  10
    Input Text  number  10
    Input Text  pages  Test Pages2
    Input Text  month  10
    Input Text  note  Test Note
    Submit Reference
    Submit Should Succeed
    Page Should Contain  Test Pages2
    Page Should Contain  10
    Page Should Contain  Test Note

# no need to test book type here, as it only has mandatory fields

Adding Too Short Author Should Fail
    Go To Add Reference Page
    Select Reference Type  inproceedings
    Input Text  author  ab
    Input Text  title  Too Short
    Input Text  booktitle  Too Short
    Input Text  year  1920
    Submit Reference
    Submit Should Fail With Message  Reference author length must be greater than 3

    Go To Add Reference Page
    Select Reference Type  book
    Input Text  author  ab
    Input Text  title  Too Short Again
    Input Text  year  1920
    Input Text  publisher  Too Short Again
    Input Text  address  Too Short Again
    Submit Reference
    Submit Should Fail With Message  Reference author length must be greater than 3

    Go To Add Reference Page
    Select Reference Type  article
    Input Text  author  ab
    Input Text  title  Too Short Thrice
    Input Text  year  1920
    Input Text  journal  Too Short Thrice
    Submit Reference
    Submit Should Fail With Message  Reference author length must be greater than 3

Adding Too Short Title Should Fail
    Go To Add Reference Page
    Select Reference Type  inproceedings
    Input Text  author  Too Short
    Input Text  title  ab
    Input Text  booktitle  Too Short
    Input Text  year  1920
    Submit Reference
    Submit Should Fail With Message  Reference title length must be greater than 3

    Go To Add Reference Page
    Select Reference Type  book
    Input Text  author  Too Short Again
    Input Text  title  ab
    Input Text  year  1920
    Input Text  publisher  Too Short Again
    Input Text  address  Too Short Again
    Submit Reference
    Submit Should Fail With Message  Reference title length must be greater than 3

    Go To Add Reference Page
    Select Reference Type  article
    Input Text  author  Too Short Thrice
    Input Text  title  ab
    Input Text  year  1920
    Input Text  journal  Too Short Thrice
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