## FreeVPNPlanet Playwright Automation
This project demonstrates basic tests implemented using Python PyTest with PlayWright

## Original Task - Key Features and Additional Conditions:
Stack - python, PyTest, PageObject Model
Tests:
1. user registration
2. user authorization
3. password change
4. account verification (you will see the button in the User Cabinet)
5. checking that the data in the User Cabinet is displayed correctly according to the backend - subscription type, number of days / tariff

Additional conditions:
1. registration must be on gmail - therefore, from there it will be necessary to retrieve the password, verify the account, confirm the password change.
2. perhaps you will find a more concise and simple method of authorization than regularly entering the login and password
3. take into account that you do not know in advance on which OS I will run the script.
4. Based on point 3 above, create an accessible and easy-to-read README.md file


## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.12 or higher
- PyTest 8.3.4 or higher
- Playwright 1.49.0 or higher


## pip install
pip install pytest
pip install pytest-html
pip install playwright


## your "pip list" command output should have items like this
pip list                               
Package           Version
----------------- -------
greenlet          3.1.1 
iniconfig         2.0.0 
Jinja2            3.1.4 
MarkupSafe        3.0.2 
packaging         24.2 
pip               24.3.1 
playwright        1.49.0 
pluggy            1.5.0 
pyee              12.0.0 
pytest            8.3.4 
pytest-html       4.1.1 
pytest-metadata   3.1.1 
typing_extensions 4.12.2 


## Run tests
cd into project folder, then run:
pytest tests --html=results/report.html

