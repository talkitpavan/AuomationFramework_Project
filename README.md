# PYTHON API AUTOMATION FRAMEWORK

# TechStack 
- Python 3.12
- Requests - HTTP requests 
- PyTest - Testing framework
- Reporting - Allure report or PyTest Html
- Test Data - CSV, EXCEL, JSON, Faker
- Advance API TestCase - JSON Schema 
- Parallel Execution - X Distribute (xdist) [in java we use testng]
## How to install packages ? 
- pip install pytest requests pytest-html allure-pytest faker jsonschema
## How to install X Distribute (xdist) to run test case in parallel
- pip install pytest-xdist

## First Step 
- Create a new python package file as "src"
- all the data which are not related to test
## Second Step
- Create a new python package file as "tests"
- - all the data which are related to test is kept here
## Third Step 
- Create a .gitignore file 

## Fourth Step 
- Create a new python package file as "utils" under the "src"
- all the common utility are kept here 
- read data from excel,csv,json
- set the header value to json/application
- 
## Fifth Step 
- Create a new python package file as "const" under the "src"
- all the constants are utility are kept here 
- create an api_constant.py file and keep all the URLS here used for restful booker
## Sixth Step 
- Create a new python package file as "crud" under the "tests"
- create new test_case under (test_filename.py) for API test 
- 


