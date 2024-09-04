## **Project for automating API and UI testing in Python for the online bookstore 'Chitai-Gorod'**

### The project aims to create an efficient testing system to verify the functionality of the web platform. 'Chitai-Gorod' is one of the leading bookstores in Russia. The goal of the automation is to improve the quality and reliability of the website, as well as to reduce the costs associated with manual testing.

### The project focuses on functionality available in both the web interface and through the REST API. A total of 5 UI and 5 API automated tests have been developed, and the Allure tool is used to generate reports on the conducted automated tests.

## **Steps:**
1. Get and use token:
- Open https://www.chitai-gorod.ru/ and open DevTools
- In DevTools in Application folder type "access-token" in the search field
- Copy and use the token without "Bearer%20"

2. Install dependencies:
- Ensure you have pip installed. 
- Install the required dependencies listed in the requirements.txt file by running:
pip install -r requirements.txt

3. Run the tests:
- Execute the tests using pytest by running:
pytest -m <marker_name>
- Replace <marker_name> with ui_test or api_test as needed.

4. Generate the report:
The command below launches Allure and converts the test results into a report:
allure serve allure-results

To ensure the terminal recognizes the allure command, install Allure Report.



## **Stack:**
- pytest
- selenium
- requests
- allure
- config

## **Structure:**
### - API
- /api_test.py - API-tests
- /api_page.py - description of API-methods
### - UI
- /ui_test.py - UI-tests'
- /ui_page.py - description of UI-methods
- README.md - file containing the project documentation, which describes installation, usage, project structure, and other important aspects
- requirements.txt - file with the used dependencies