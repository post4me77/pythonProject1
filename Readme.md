# How run TCs

* To run tests with allure report:
  > pytest --alluredir=report_allure
* To run pytest with HTML report:
  > pytest --html=reports/report.html --self-contained-html

_________________________________________________________

# Souse labs configuration:

* Add SAUCE_USERNAME to your env variables
* Add SAUCE_ACCESS_KEY to your env variables
* Provide system info in run_settings.ini

_________________________________________________________

# How to generate documentation

* install doxygen and add it to your path
* you can change doxygen_config file
* run in terminal doxygen:
  > doxygen doxygen_config

__________________________________________________________

# Jmeter how to

* Copy reportgenerator.properties and overwrite this file in your jmeter bin folder to have configured html report
* Run command to generate HTML report:
  > jmeter -n -t "example_project.jmx" -l "result_file.csv" -e -o "report_folder"

>

# Docker image

* build docker image:
  > docker build -t test_automation_framework .
* run docker container
  > docker run -t -d test_automation_framework
* to open created docker container
  > docker exec -it {container_id} bash
  > 

# Allure
  > allure serve .\report_allure\
>
> 
# REST API test please use folder test_cases- > api_test
  > Run with test with mock data
> > If you use IDE start this test by UI
> 
