from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_submit_text(driver):
    link = 'https://www.qa-practice.com/elements/input/simple'
    input_text = 'blablabla'
    driver.get(link)
    input_field = driver.find_element(By.ID, 'id_text_string')
    input_field.send_keys(input_text)
    input_field.submit()
    result_text = driver.find_element(By.ID, 'result-text')
    print(result_text.text)


def test_fill_student_registration_form(driver):
    driver.get('https://demoqa.com/automation-practice-form ')
    name_element = driver.find_element(By.ID, 'firstName')
    name_element.send_keys("Egor")

    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys("Kovalenko")

    email_element = driver.find_element(By.ID, 'userEmail')
    email_element.send_keys("123434@mail.ru")

    checkbox_male = driver.find_element(By.XPATH, '//*[@for="gender-radio-1"]')
    checkbox_male.click()

    user_number_element = driver.find_element(By.ID, 'userNumber')
    user_number_element.send_keys('1237780912')

    calendar_input = driver.find_element(By.ID, 'dateOfBirthInput')
    calendar_input.click()
    month_input = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select')
    month_input.click()
    se = Select(month_input)
    se.select_by_visible_text('March')

    year_input = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select')
    year_input.click()
    se_1 = Select(year_input)
    se_1.select_by_visible_text('1988')

    day_input = driver.find_element(By.XPATH, '//*[@aria-label="Choose Tuesday, March 22nd, 1988"]')
    day_input.click()

    subjects_element = driver.find_element(By.ID, 'subjectsInput')
    subjects_element.send_keys('Scifi', '2024')

    hobby_element = driver.find_element(By.XPATH, '//*[@for="hobbies-checkbox-2"]')
    hobby_element.click()

    address_element = driver.find_element(By.ID, 'currentAddress')
    address_element.send_keys('Togliatty')

    input_data = ['NCR', 'Delhi']
    dropdown = driver.find_element(By.ID, 'react-select-3-input')
    dropdown.send_keys(input_data[0])
    dropdown.send_keys(Keys.ENTER)

    dropdown_1 = driver.find_element(By.ID, 'react-select-4-input')
    dropdown_1.send_keys(input_data[1])
    dropdown_1.send_keys(Keys.ENTER)

    submit_element = driver.find_element(By.ID, 'submit')
    submit_element.click()

    response_text = driver.find_element(By.CSS_SELECTOR, '.table-responsive')
    print(response_text.text)


def test_language_is_equal_to_presented(driver):
    link = 'https://www.qa-practice.com/elements/select/single_select'
    driver.get(link)
    visible_text = 'Python'
    input_select = driver.find_element(By.ID, 'id_choose_language')
    input_select.click()
    se = Select(input_select)
    se.select_by_visible_text('Python')
    input_select.submit()
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == visible_text


def test_text_is_presented(driver):
    link = 'https://the-internet.herokuapp.com/dynamic_loading/2'
    presented_text = "Hello World!"
    driver.get(link)
    # presented_text = "Hello World!"
    start_button = driver.find_element(By.XPATH, '//button[text()="Start"]')
    start_button.click()
    waiting = WebDriverWait(driver, 6)
    button_text = waiting.until(EC.presence_of_element_located((By.XPATH, '//h4[text()="Hello World!"]')))
    assert button_text.text == presented_text
