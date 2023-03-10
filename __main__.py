from os import wait
from getpass import getpass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, WebDriverException, TimeoutException, NoSuchElementException, NoSuchFrameException


driver = webdriver.Firefox()
login_url = "https://www.overleaf.com/login"
all_projects_url = "https://www.overleaf.com/project"
# email = input("Email: ")
email = "haadbhutta@gmail.com"
# password = getpass("Password: ")
password = "R1a4786$"

def access():
    try:
        driver.get(login_url)
    except TimeoutException:
        print("Time out")
    login_title = "Log in to Overleaf - Overleaf, Online LaTeX Editor"
    assert login_title in driver.title
    print(f"Accessed {driver.current_url}")


def login(email, password):
    # Find email and password entry elements
    try:
        email_elem = driver.find_element(By.NAME, "email")
        password_elem = driver.find_element(By.NAME, "password")
        email_elem.clear()
        password_elem.clear()
    except NoSuchElementException:
        print("One of the email or password textfields was not found!")

    # Clear their text fields 

    # Type in the user's given email and press enter
    email_elem.send_keys(email)
    email_elem.send_keys(Keys.RETURN)

    # Type in the user's given (hidden) password and press enter
    password_elem.send_keys(password)
    password_elem.send_keys(Keys.RETURN)

    assert "No results found." not in driver.page_source
    # driver.close()

def url_has_changed(desired_url) -> bool:
    return driver.current_url == desired_url

def get_user_info() -> list:
    info = []
    email = input("Email: ")
    password = input("Password: ")
    info.append(email)
    info.append(password)
    return info

def get_files() -> list:
    files = []
    pass

def access_folders():
    folders = []
    for folder in folders:
        folder.get_files()
    

get_user_info()

email = get_user_info()[0]
password = get_user_info()[1]

access()
login(email=email,password=password)


if url_has_changed(all_projects_url):
    access_folders()
else:
    raise NoSuchFrameException


