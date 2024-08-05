from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_first(driver):
    driver.get('https://www.demoblaze.com/index.html')
    wait = WebDriverWait(driver, 10)
    my_element = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="Sony vaio i5"]')))
    ActionChains(driver).key_down(Keys.CONTROL).click(my_element).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[1])
    cart = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="Add to cart"]')))
    cart.click()
    alert = wait.until(EC.alert_is_present())
    alert.accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    cart_1 = wait.until(EC.presence_of_element_located((By.ID, 'cartur')))
    cart_1.click()
    driver.implicitly_wait(6)
    assert driver.find_element(By.XPATH, '(//td[text()="Sony vaio i5"])[1]').text == "Sony vaio i5"


def test_second(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    wait = WebDriverWait(driver, 10)
    messenger_bag = driver.find_element(By.CSS_SELECTOR, '[alt="Push It Messenger Bag"]')
    actions = ActionChains(driver)
    actions.move_to_element(messenger_bag).perform()
    driver.find_element(By.CSS_SELECTOR, '.action.tocompare').click()
    compare_bag_text = wait.until(EC.presence_of_element_located((By.XPATH, '//*[text()="Push It Messenger Bag"]')))
    assert compare_bag_text.text == "Push It Messenger Bag"
