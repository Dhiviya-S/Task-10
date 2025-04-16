#To import pytest modules and filename should be test_filename.py or \filename_test.py
import pytest
#To import time library for use of time.sleep()
import time
#Importing WebDriver and By classes from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#Creating WebDriver instance to open Chrome browser
driver = webdriver.Chrome()
#get() navigates to the Saucedemo page
driver.get("https://www.saucedemo.com/")
#Maximizes the Chrome Browser Window
driver.maximize_window()

#driver.title displays the Saucedemo page title
print("Title of the webpage:",driver.title)
actual_title=driver.title

#driver.current_url prints the URL of Saucedemo page
print("Current URL of the webpage:", driver.current_url)
actual_url=driver.current_url

#open("filename.txt","mode") creates a file in writing mode and file.write is used to write page source to Webpage_task_11.txt
with open("Webpage_task_11.txt","w") as file:
    file.write(driver.page_source)

#find_element is used to find ID element and value of it using Inspect and send_keys() is used to enter the username in Saucedemo page
#<input class="input_error form_input" id="user-name" name="user-name" autocorrect="off" autocapitalize="none" value="">
#Syntax:driver.find_element(By.ID,"value")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
# Wait for the page to load
time.sleep(2)

#find_element is used to find ID  and value of it using Inspect and send_keys() is used to enter the password
#<input class="input_error form_input" id="password" name="password" autocorrect="off" autocapitalize="none" value="">
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)

#Identify the login button using By.ID and click() is used to click the login button after entering login credentials and navigate to the inventory page
driver.find_element(By.ID, "login-button").click()
print("URL after login credentials:",driver.current_url)
loginn_url=driver.current_url


#Fixtures are functions in pytest used to prepare environment for test execution.
@pytest.fixture
#title() function returns Saucedemo page title in the variable name "actual_title"
def title():
    return actual_title

#Pytest testcases are written as test_method(). Assert is used to check value of actual and expected one.
#Positive test case on asserting title of Saucedemo by providing correct title as "Swag Labs"
def test_title_positive(title):
    assert actual_title == "Swag Labs"

#Negative test case on asserting title of Saucedemo by providing incorrect title as "Sauce Lab"
def test_title_negative(title):
    assert actual_title =="Sauce Lab"


#url() function returns Saucedemo page url in the variable name "actual_url"
@pytest.fixture
def url():
    return actual_url

#Positive test case on asserting URL of Saucedemo by providing correct url
def test_positive_url(url):
    assert actual_url == "https://www.saucedemo.com/"

#Negative test case on asserting URL of Saucedemo by providing incorrect url
def test_negative_url(url):
    assert actual_url =="https://www.swagdemo.com/"


#login_url() function returns inventory page URL after entering login credentials of Saucedemo
@pytest.fixture
def login_url():
    return loginn_url

#Positive test case on asserting URL of Inventory page by providing correct url
def test_positive_loginurl(login_url):
    assert loginn_url == "https://www.saucedemo.com/inventory.html"

#Negative test case on asserting URL of Inventory page by providing incorrect url
def test_negative_loginurl(login_url):
    assert loginn_url =="https://www.saucedemo.com/payment.html"

time.sleep(5)
#Closes the Chrome Window and ends the WebDriver session
driver.quit()

#To generate HTML Report of Pytest cases:pytest -v -s test_url.py --html=report.html
#report.html(to be opened in Browser) and Webpage_task_11.txt is attached