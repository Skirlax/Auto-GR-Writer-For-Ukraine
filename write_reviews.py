import random
import time

import numpy as np
import requests
import selenium.common.exceptions
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import get_input

gi = get_input.HandleUserInput()


class WriteGoogleReviews:
    opt = webdriver.ChromeOptions()
    opt.add_argument('--disable-blink-features=AutomationControlled')
    browser = webdriver.Chrome(options=opt, executable_path="ChromeDriver/chromedriver")
    act = ActionChains(browser)
    stealth(browser,
            user_agent='DN',
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True
            )

    wait = WebDriverWait(browser, 180)

    def login_to_maps(self):
        self.browser.get(
            'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
        logged_in = gi.login_to_goole_prompt()  # Not needed variable here.
        # I am using the input method just to wait until the user is logged in.

    def find_place_in_russia(self):
        self.browser.get(
            'https://www.google.com/maps/search/restaurants+near+Russia/@55.7585392,37.5604265,13z/data=!4m2!2m1!6e5')
        search_box = self.browser.find_element(by=By.XPATH, value='//*[@id="searchboxinput"]')
        search_box.click()
        for x in "restaurants near Russia":
            search_box.send_keys(x)
            time.sleep(random.randint(1, 3))

    def search_for_places(self, search_term):
        url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
        api_key = 'User your own if you want to use this method...'
        r = requests.get(url, 'query=' + search_term + '&key=' + api_key)
        _ = r.json()
        data = _['results']
        for c in data:
            print(c.get('name'))

    def read_places(self, where_to_read): # Used to read the current place from the text file called restaurants.txt
        with open("restaurant_names.txt", "r+", encoding='UTF-8') as file:
            place = file.readlines()
            return str(np.char.strip(place[where_to_read]))

    def write_reviews(self, message_to_write, line_number):
        self.browser.get('https://www.google.com/maps/@-70.6502477,47.2431857,3z')
        if message_to_write == 'x':
            message_to_write = self.read_default_message()

        place = self.search_on_maps(line_number)
        time.sleep(5)
        time.sleep(4)
        _ = self.browser.find_element(By.XPATH,
                                      value='//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]/span/span[1]/span[2]/span[1]/button')
        _.click()

        time.sleep(4)
        _ = self.browser.find_element(By.XPATH, value='//*[@id="pane"]/div/div[1]/div/div/div[2]/div[4]/div/button')
        _.click()
        time.sleep(8)
        for x in range(1, 8):
            if x == 7:
                self.act.send_keys(Keys.SPACE)
                self.act.perform()
            self.act.send_keys(Keys.TAB)
            self.act.perform()
            time.sleep(0.5)
        time.sleep(3)
        for x in message_to_write:
            self.act.send_keys(x)
            self.act.perform()
        time.sleep(random.randint(1, 5))
        time.sleep(0.5)
        for x in range(1, 4):
            self.act.send_keys(Keys.TAB)
            self.act.perform()
            time.sleep(0.6)
            if x == 1:
                self.act.send_keys(Keys.SPACE)
                self.act.perform()
                time.sleep(5)
                for y in range(6):
                    self.act.send_keys(Keys.TAB).perform()
                    time.sleep(1)

            self.act.send_keys(Keys.ARROW_RIGHT).perform()
            self.act.send_keys(Keys.ENTER).perform()
            time.sleep(8)
            for b in range(0, 6):
                self.act.send_keys(Keys.TAB).perform()
                time.sleep(1)
            time.sleep(8)
            self.act.send_keys(Keys.SPACE).perform()
            for i in range(4):
                self.act.send_keys(Keys.ARROW_RIGHT).perform()
                self.act.send_keys(Keys.SPACE).perform()
                time.sleep(1)
            time.sleep(8)
            for p in range(1, 2):
                self.act.send_keys(Keys.TAB).perform()
                time.sleep(1)
            self.act.send_keys(Keys.ENTER).perform()

            time.sleep(4)
            break

        for p in range(1, 17):
            self.act.send_keys(Keys.TAB).perform()
            time.sleep(0.5)
        time.sleep(3)
        self.act.send_keys(Keys.ENTER).perform()
        time.sleep(10)
        self.act.send_keys(Keys.ESCAPE)
        self.act.perform()
        time.sleep(10)
        go_back = self.browser.find_element(By.XPATH,
                                            value='//*[@id="pane"]/div/div[1]/div/div/div[1]/div/div/div[1]/span/button')
        go_back.click()
        time.sleep(1)
        return place, self.browser.current_url

    def read_default_message(self):
        result_str = ''
        with open('message.txt', 'r+', encoding='UTF-8') as file:
            _ = file.readlines()
            for x in _:
                result_str += x
            for b in result_str:
                if '[' in b or ']' in b or "'" in b:
                    b = b.replace(b, "")

        return result_str

    def search_on_maps(self, line_number):
        place = self.read_places(line_number)
        self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="searchboxinput"]')))
        search_box = self.browser.find_element(By.XPATH, value='//*[@id="searchboxinput"]')
        search_box.click()
        if 'Restaurant' not in place and 'restaurant' not in place:
            for letter in place + ' Restaurant Russia':
                search_box.send_keys(letter)
                time.sleep(random.randint(0, 1))
        else:
            for letter in place + ' Russia':
                search_box.send_keys(letter)
                time.sleep(random.randint(0, 1))
        search_box.send_keys(Keys.ENTER)
        try:
            WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located(
                (By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/a')))
            _ = self.browser.find_element(By.XPATH,
                                          value='//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/a')
            _.click()
        except selenium.common.exceptions.NoSuchElementException and selenium.common.exceptions.TimeoutException:
            pass
        time.sleep(6)
        return place

    def remove_places_from_list(self):
        with open('restaurant_names.txt') as file:
            _ = file.readlines()
            _.pop(0)
            _.pop(1)
            _.pop(2)
            file.close()
        with open('restaurant_names.txt', 'w+') as f:
            f.writelines(_)

    def write_logs(self, current_place, url):
        with open(f'logs/{datetime.now().strftime("%b %d %Y %H:%M:%S")}', 'w+',encoding='UTF-8') as log:
            log.write(
                f"""Writing recension to '{current_place}' done at {datetime.now().strftime("%b %d %Y %H:%M:%S")}.
                 Place removed from list of usable places. The review may be found on the following URL: '{url}'""")
            log.close()
