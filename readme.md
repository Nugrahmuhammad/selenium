# Automation Framework and Test Suite

## Overview
This documentation provides an overview of an automation framework and test suite built using Python, Selenium, and Pytest for testing a Magento-based e-commerce website. The test suite includes end-to-end tests for signing in, adding products to the cart, and placing an order.

## Framework Components
The framework includes the following components:
- **Selenium**: A web automation framework for interacting with web pages.
- **Pytest**: A testing framework for writing and running test cases.
- **Allure**: A tool for generating test reports with rich visuals.

## Prerequisites
Before running the test suite, ensure that the following prerequisites are met:
1. Python is installed on your system.
2. Install the necessary Python packages using the following command:

pip install selenium pytest allure-pytest

3. Download the Chrome WebDriver [from here](https://sites.google.com/chromium.org/driver/) and add it to your system's PATH.

## Test Data
You can configure test data such as email addresses, passwords, and phone numbers in the `constants.py` file.

## Test Execution
Follow these steps to set up and run the test suite:
1. Clone the test automation project from the repository or save the script to your local machine.
2. Open the `constants.py` file and configure the necessary constants for your test data.
3. Navigate to the project directory in your terminal.
4. Run the test suite using the following command:
pytest test.py --alluredir=./allure-results

5. The tests will run in a Chrome browser window, and you will see the automation steps executed on the Magento website.
6. After test execution, Allure reports will be generated in the project directory.
7. To view the Allure report, run the following command:


## Test Suite Structure
The test suite is structured as follows:
- `test_open_magento(driver)`: Opens the Magento website.
- `test_sign(driver)`: Signs in with the provided credentials.
- `test_add_product(driver)`: Adds products to the cart and completes the checkout process.

Each test is documented using Allure steps to provide clear reporting.

## Reporting
Allure reports provide detailed insights into test execution. You can view test statuses, steps, and attachments for each test case.

Feel free to update this `README.md` with any additional information or specifics about your automation framework and test suite.

