#!/bin/bash

# Exit on first error
set -e

echo "✅ Running pytest..."
pytest testcases -k test_login_success --alluredir=reports/allure-results

echo "✅ Generating Allure report..."
allure generate reports/allure-results -o reports/allure-report --clean
#
#echo "✅ Opening report in browser..."
#if [[ "$OSTYPE" == "linux-gnu"* ]]; then
#    xdg-open reports/allure-report/index.html
#elif [[ "$OSTYPE" == "darwin"* ]]; then
#    open reports/allure-report/index.html
#elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
#    start reports/allure-report/index.html
#else
#    echo "⚠️ Please open report/allure-report/index.html manually"
#fi
