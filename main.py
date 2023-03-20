import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

amazon_url = 'https://www.amazon.com/'
search_box_selector = '#twotabsearchtextbox'
text = 'kinder'
item_selector = '#search > div.s-desktop-width-max.s-desktop-content.s-wide-grid-style-t1.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(2) > div > div > div > div > div.s-product-image-container.aok-relative.s-text-center.s-image-overlay-grey.s-padding-left-small.s-padding-right-small.puis-spacing-small.s-height-equalized > span > a'

def open_site(url):
    driver = webdriver.Chrome()
    driver.get(amazon_url)
    driver.maximize_window()
    return driver
def search(driver,selector,text):
    textbox = driver.find_element(By.CSS_SELECTOR, selector)
    textbox.send_keys(text)
    textbox.send_keys(Keys.ENTER)
def select_item(driver,selector):
    k_s = driver.find_element(By.CSS_SELECTOR,selector)
    k_s.click()




