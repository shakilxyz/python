""""
    In this script I have used selenium and chrome webdriver for getting weather data from https://openweathermap.org/
    Selenium is used for catching data which are loaded by javascript
    We know that javascript files load after loading the static web-page, so it takes some time.
        That's why I used selenium for fetching weather data when the full page is loaded

    For web scraping with selenium we need to use chrome webdriver (chromewebdriver.exe) for this script.
        Please check the same directory on my github page or download chromewebdriver.exe and place both
        python script and chromewebdriver.exe in same directory then this script will work
"""

from selenium import webdriver
from time import sleep
from termcolor import colored


# using headless browser because we don't want to open a new chrome window after running this script
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

while True:
    try:
        location = input(colored('Location : ', 'green'))
        driver.get('https://openweathermap.org/find?q=' + location)
        soup = driver.find_element_by_tag_name('tr')
        link = soup.find_element_by_tag_name('a').get_attribute('href').strip()
        print(soup.text)
        more = input(colored("\nMore details ? [y/any] : ", 'green')).strip().lower()
        if more == 'y':
            driver.get(link)

            # wait 1 second for loading javascript files
            # You can increase the waiting time if your internet is slow or the website loads slowly
            sleep(1)
            
            for li in driver.find_element_by_class_name('day-list').find_elements_by_tag_name('li'):
                span = li.find_elements_by_tag_name('span')
                print("{:<13}  |  {:<11}  |  {:<15}".format(span[0].text, span[1].text, span[2].text))
    except:
        print(colored("No data found", 'red'))
    print()
