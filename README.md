# Aquariux Automation

## Project Description
Aquariux Automation is a Python-based test automation framework designed to validate the functionality of the Aquariux trading platform. It uses Selenium WebDriver for browser automation and Pytest for test execution.

## Features
- Automated testing for login, market orders, pending orders, and order history.
- JavaScript-based DOM manipulation for handling complex web elements.
- Integration with Allure for generating detailed test reports.

## Prerequisites
- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver (managed automatically via `webdriver_manager`)
- Allure Commandline (for generating reports)

## Setup Instructions
1. Clone the repository:
   git clone https://github.com/hovanthanh1988/aquariux-automation.git
2. Install dependencies:  
_pip install -r requirements.txt_

3. Install Allure Commandline: Follow the instructions here.  
https://allurereport.org/docs/install-for-windows/

4. Running Tests
To execute a specific test, use the following command:
   _pytest /testcases/ -k <test_case_name>_

5. To run all tests, use:

   _run_all.sh_

6. Generating Reports
After running tests, generate the Allure report:

   _allure serve reports/allure-results_

7. Folder Structure

   - testcases/: Contains all test scripts.

   - pages/: Page Object Model classes for web elements.

   - config.py: Configuration file for test data.

   - reports/: Directory for storing test results and reports.
