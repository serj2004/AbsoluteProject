# -*- coding: utf-8 -*-
import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(60)
    yield browser
    browser.quit()


def test_insurance_premium_checking(browser):
    browser.get('https://www.absolutins.ru/kupit-strahovoj-polis/strahovanie-zhizni-i-zdorovya/ukus-kleshcha/')
    browser.find_element_by_xpath('//li[2]/label').click()
    browser.find_element_by_xpath('//div[6]/div/div/div').click()
    browser.find_element_by_xpath('//span[@id=\'region-button\']/span').click()
    browser.find_element_by_id('ui-id-2').click()
    browser.find_element_by_name('PROMOCODE').clear()
    browser.find_element_by_xpath('//button/span').click()
    browser.find_element_by_id('result-number').click()
    browser.find_element_by_id('result-sum').click()
    result_number = browser.find_element_by_id('result-number').text
    result_sum = browser.find_element_by_id('result-sum').text
    assert 'руб./год' in result_sum
    assert len(result_number) == 8
    

