# Selenium_Task
# Selenium Task 1 - Test Automation

**Company:** CODTECH IT SOLUTIONS  
**Intern Name:** Kandimalla Karthik  
**Intern ID:** CTIS2128  
**Domain:** Software Testing  
**Duration:** 4 Weeks  
**Mentor:** Neela Santosh  

---

## Task Description

As part of my internship at CODTECH IT SOLUTIONS, I was assigned a task in the domain of **Software Testing**, specifically to automate the testing of a sample web application using **Selenium WebDriver**. The goal of this task was to create a script that could verify the login functionality and navigation of a web application, and generate a detailed test report showing the results of the execution.

---

## How I Prepared

Before starting the automation, I first ensured that my environment was correctly set up for Selenium testing. I installed **Python 3.12**, created a **virtual environment**, and installed all necessary packages such as `selenium`, `pytest`, and `pytest-html` for generating HTML test reports. I also downloaded and set up **GeckoDriver** to work with Firefox, ensuring that the browser and driver versions were compatible.  

Once the setup was ready, I analyzed the requirements of the task. I identified the key elements of the login page, such as the **username field**, **password field**, and **login button**. I also considered what a successful navigation workflow would look like after logging in.

---

## What I Have Done

1. **Created the test script (`test_login.py`):**  
   - Automated opening of the web application.  
   - Entered valid credentials into the login form.  
   - Clicked the login button and verified navigation to the dashboard or homepage.  
   - Added explicit waits using Selenium’s `WebDriverWait` to ensure elements were fully loaded before interaction.  

2. **Handled exceptions and browser sessions:**  
   - Ensured that the browser opens and closes correctly after test execution.  
   - Used proper error handling to catch potential Selenium exceptions such as `NoSuchElementException` or `InvalidSessionIdException`.  

3. **Generated Test Report:**  
   - Used `pytest-html` to generate a detailed **HTML report**.  
   - The report includes the execution time, status of the test (pass/fail), and environment details such as Python version and platform.  

4. **Captured Output Screenshot:**  
   - Took a screenshot of the successful login page after the test execution.  
   - Saved the screenshot in the project folder for reference and submission.  

---

##output

<img width="1903" height="992" alt="Image" src="https://github.com/user-attachments/assets/9a5462c6-8a17-44a9-819d-fa4a834b0b05" />

