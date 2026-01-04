# test_login.py
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------------- Firefox driver fixture ----------------
@pytest.fixture
def driver():
    service = Service('./geckodriver.exe')  # Path to geckodriver
    options = Options()
    options.headless = False  # Browser window visible
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()  # Close browser after test

# ---------------- Test login navigation ----------------
def test_login_navigation(driver):
    # Open login page
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Wait for username field and enter credentials
    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username.send_keys("student")  # demo username

    password = driver.find_element(By.ID, "password")
    password.send_keys("Password123")  # demo password

    # Click login button
    login_button = driver.find_element(By.ID, "submit")
    login_button.click()

    # Wait for success message
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )

    # Assertion to confirm login successful
    assert "Logged In Successfully" in success_message.text
