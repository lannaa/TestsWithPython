import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("http://sps-cms-test.sparkle.testing1.startpagina.nl/themas#Pages")

# ??? how to check an element is displayed on a menu
def menu():
    header = driver.find_elements_by_xpath("//div[@id='menu']//li")
    for link in header:
        if link.get_attribute("class"):
            link.click()
        assert link.is_displayed()
menu()

def open_niew():
    pagina.click()
    title_element_new = driver.find_element_by_xpath('//*[@id="name"]')
    element_text_new = title_element_new.text
    # print(element_text_new)
    assert 'Pagina-aanvragen - Nieuw' == element_text_new
    #check columns
    thema_column = driver.find_element_by_xpath('//*[@id="items"]/div[2]/div/table/thead/tr/th[1]/button')

    assert thema_column.is_displayed()
open_niew()

def open_existing():
    tab_existing = driver.find_element_by_xpath('//a[contains(text(),"Bestaand")]')
    tab_existing.click()
    title_element_existing = driver.find_element_by_xpath('//*[@id="name"]')
    element_text_bestaand = title_element_existing.text
    # print(element_text_bestaand)
    assert 'Pagina-aanvragen - Bestaand' == element_text_bestaand
open_existing()

def open_pause():
    tab_pause = driver.find_element_by_xpath('//a[contains(text(),"Pauze")]')
    tab_pause.click()
    title_element_pause = driver.find_element_by_xpath('//*[@id="name"]')
    element_text_pause = title_element_pause.text
    # print(element_text_pause)
    assert 'Pagina-aanvragen - Pauze' == element_text_pause
open_pause()

def open_contract():
    tab_contract = driver.find_element_by_xpath('//*[@id="items"]/div[2]/div/ul/li[4]/a')  #('//a[contains(text(),"Contract\nsturen")]')
    tab_contract.click()
    title_element_contract = driver.find_element_by_xpath('//*[@id="name"]')
    element_text_contract = title_element_contract.text
    # print(element_text_contract)
    assert 'Contract Sturen' == element_text_contract
open_contract()

def open_signature():
    tab_signature = driver.find_element_by_xpath('//a[contains(text(),"Handtekening")]')
    tab_signature.click()
    title_element_signature = driver.find_element_by_xpath('//*[@id="name"]')
    element_text_signature = title_element_signature.text
    # print(element_text_signature)
    assert 'Wachten op handtekening' == element_text_signature
open_signature()


def driver_close():
    driver.close()
driver_close()


