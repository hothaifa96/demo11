from main import *
import requests


class TestUI:
    def test_1(self):
        driver = open_site(amazon_url)
        time.sleep(1)
        search(driver, search_box_selector, text)
        time.sleep(1)
        select_item(driver, item_selector)
        time.sleep(1)
        actual = driver.current_url
        expected = 'https://www.amazon.com/Kinder-Joy-Chocolates-Surprise-Inside/dp/B077NT42QP/ref=sr_1_1?crid=22JGBB9PVIB0Q&keywords=kinder&qid=1679333459&sprefix=kinder%2Caps%2C235&sr=8-1'

        assert actual == expected


class TestAPI:
    def test_1(self):
        res = requests.get('https://api.dictionaryapi.dev/api/v2/entries/ar/fchgjkl;,mknjbkh')
        assert 400 > res.status_code >= 200
