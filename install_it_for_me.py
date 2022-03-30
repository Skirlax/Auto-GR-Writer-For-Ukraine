#!/usr/bin/env python3

import os
import wget
import shutil

os_name = input("Are you using Linux, Mac or Windows? (type: L for linux, M for mac etc: ")
if os_name == 'M':
    m1 = input("Does it have M1 chip? (y/n): ")
    if m1 == 'y':
        chromedriver = wget.download(
            'https://chromedriver.storage.googleapis.com/99.0.4844.51/chromedriver_mac64_m1.zip')
    if m1 == 'n':
        chromedriver = wget.download('https://chromedriver.storage.googleapis.com/99.0.4844.51/chromedriver_mac64.zip')
        
if os_name == 'W':
    chromedriver = wget.download('https://chromedriver.storage.googleapis.com/index.html?path=99.0.4844.51/')

if os_name == 'L':
    print('Good choice ;) You have the driver already installed :0')


os.replace(chromedriver, 'ChromeDriver/chromedriver')
print('New driver installed :)')

chrome_installed = input('Do you have chrome of version 99 (only) installed? (y/n): ')

if chrome_installed == 'n':
    chrome = wget.download('https://dw.uptodown.com/dwn/5jlsIJrp-1DbZeDY2YYzpOREzFQX_T2hqPSg_cEaywvH6z0UPjdkmhu-A8rNjkFwJ3SGKkpn9gIU8bYSO-K74nu7nqkxMv8CnhAPFKKu7_x47eayA3kCXaz9LhEBsguH/GPZjGBhOdUnANVHTj2ZhWOwCDnrbV7CbOG0XwH85mmOsuUeOVZO95mnl8_sngh9ThONz9jelaYHaz_HVdNXkiKEIOvm2rGtsZqPKYfUTcmVkuW0zV2uFuWPsv8abjXaA/R4VHw61ewr7EyRtDG4X25eyb1CbC8KHl1PqzAWab9KuRMj4CXT2bkiypxaagBRqYKneh8O0FUHUqYDJo2MW_tOYvZB7nrViX99-MEfnE9wA=/')

