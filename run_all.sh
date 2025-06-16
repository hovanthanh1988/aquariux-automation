#!/bin/bash

# Exit on first error
set -e

echo "Running pytest..."
pytest testcases -k test_login_success --alluredir=reports/allure-results

echo "Generating Allure report..."
allure generate reports/allure-results -o reports/allure-report --clean
