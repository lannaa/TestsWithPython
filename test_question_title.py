import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

VALUE = 'How do you do?'
VALUE_2 = "1. Wat is je vraag?"
CATEGORIES = 'id_category'
QUESTION_BLOCK = '//*[@class="column question-helpers_block"]'

driver = webdriver.Firefox(executable_path=r'C:\Users\a.liakh\Desktop\geckodriver.exe')
driver.get("https://www.staging1.startpagina.nl/v/")
driver.implicitly_wait(10)


def test_start():
    search = driver.find_element_by_id('id_title')
    search.send_keys('How do you do')
    search.send_keys(Keys.RETURN)
    assert driver.find_element_by_id('id_title').get_attribute('value') == VALUE
    assert driver.find_element_by_xpath('//*[@class="column question-question_block"]//h2').text == VALUE_2
    assert driver.find_element_by_xpath(QUESTION_BLOCK).is_displayed()
    assert driver.find_element_by_xpath('//*[@class="column question-helpers_block"]//h3').is_displayed()
    assert len(driver.find_elements_by_xpath('//*[@class="list list-numeric list-numeric-items"]/li')) == 5
  #  assert driver.find_element_by_id(CATEGORIES) in driver.find_element_by_xpath('//*[@class="column question-category_block"]')

def test_dropdown():
    field = driver.find_element_by_id(CATEGORIES) # in driver.find_element_by_xpath('//*[@class="column question-category_block"]')
    field.click()


def test_quit():
    driver.close()
