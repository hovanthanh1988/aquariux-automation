#!/bin/bash

set -e

echo "Running pytest..."
pytest testcases --alluredir=reports/allure-results

echo "Generating Allure report..."
allure generate reports/allure-results -o reports/allure-report --clean
