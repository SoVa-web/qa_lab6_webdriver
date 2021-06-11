# -*- coding: utf-8 -*-

from re import S
import time 
from selenium import webdriver


def startDriver(urlWebsite):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #запускаємо вебдрайвер 
    browser = webdriver.Chrome(options=options)

    #робимо get-запит
    browser.get(urlWebsite)
    browser.implicitly_wait(30)
    return browser

def openPageByLink(link, driver):
    assert link in driver.current_url, "Сторінка не вікрилась"

def serhByCity(nameCity, driver):
    driver.find_element_by_id('brandTooltipBrandAutocompleteInput-region').send_keys(nameCity)
    driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/form/div[3]/button/span').click()
    time.sleep(2)

    actual_result = driver.find_element_by_xpath('/html/body/div[5]/section/div[2]/div/div/section[1]/div[4]/div[2]/div[3]/ul/li[2]').text
    assert actual_result==nameCity, "Результат не знайдено"
    time.sleep(2)
    return driver

def searchByMarka(marka, driver):
    driver.find_element_by_id('brandTooltipBrandAutocompleteInput-0').send_keys(marka)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="brandTooltipBrandAutocomplete-0"]/ul/li[1]').click()
    time.sleep(2)
    actual_result = driver.find_element_by_xpath('//*[@id="searchResults"]/section[1]/div[3]/div[2]/div[1]/div/a').text
    assert marka in actual_result, "Невдалий пошук"

def viewAdsInfo(marka, driver):
    driver.find_element_by_xpath('//*[@id="searchResults"]/section[1]/div[3]/div[2]/div[1]/div/a').click()
    actual_result = driver.find_element_by_xpath('/html/body/div[2]/div[6]/main/div[2]/h3').text
    assert marka in actual_result, "Результат не знайдений" 

def checkButtonAddNew(link, driver):
    driver.find_element_by_xpath('//*[@id="addAutoButton"]').click()
    assert link in driver.current_url, "Сторінку не знайдено"

def startTest():
    urlWebsite = "https://auto.ria.com/uk/"
    driver = startDriver(urlWebsite)
    openPageByLink(urlWebsite, driver)
    time.sleep(2)
    driver = serhByCity("Київ", driver)
    time.sleep(2)
    searchByMarka("Ford", driver)
    time.sleep(2)
    viewAdsInfo("Ford", driver)
    time.sleep(2)
    checkButtonAddNew("https://auto.ria.com/uk/add_auto.html", driver)
    time.sleep(15)


startTest()
