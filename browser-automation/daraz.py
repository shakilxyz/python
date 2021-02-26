"""
    It's a simple script for automate https://daraz.com.bd
    You can search product by name then select your product as given output
    Daraz takes a little bit time to load it's pages so my scraper is also works slowly

    Note : you must use chrome web driver (chromedriver.exe) to run this script. place this python script and chrome driver
        in same directory. Then run this script
"""
from selenium import webdriver
from termcolor import colored
import time
import os

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

print(colored("Simple daraz (https://daraz.com.bd) search automation. search products, go to next page and back to "
              "previous page, Or you can see product description with buyers comments. There is a little bit problem "
              "for the speed of the script. This script works slowly because you know that daraz.com.bd website takes "
              "a little bit longer time to load it's data\n", 'green'))


def get_product_info(lnk):
    print(colored("It will take some time for loading data. Wait a few seconds\n", 'red'))
    driver.get(lnk)
    t = time.time()
    while time.time() - t <= 10:
        try:
            description = driver.find_element_by_class_name('pdp-product-detail').find_elements_by_tag_name('li')
            des = ''
            for li in description:
                if li.text:
                    des += li.text.strip() + '\n'
            print(des)
            try:
                print("Rating :", driver.find_element_by_class_name('score').text)
            except:
                pass
            comments = driver.find_elements_by_class_name('item-content')
            for i in comments:
                print("[+]", i.text.strip())

            p = input("press enter to continue ")
            return
        except:
            pass
    print("page didn't load in 10 seconds. So it has been skipped\n")


def show_searches(p, s):
    driver.get('https://www.daraz.com.bd/catalog/?page={}&q={}'.format(p, s))
    results = driver.find_elements_by_class_name('c5TXIP')

    count = 1
    products = {}
    for j in results:
        link = j.find_element_by_class_name('cRjKsc').find_element_by_tag_name('a')
        link = link.get_attribute('href')
        pricing = j.find_element_by_class_name('c3KeDq')
        name = pricing.find_element_by_tag_name('a').text
        price = pricing.find_element_by_tag_name('span').text
        products[count] = [name, price, link]
        count += 1
    return products


def show_result(l, h, d):
    t = len(d)
    for i in range(l, h):
        if i > t:
            break
        print(colored("[" + str(i) + "]", 'yellow') + " Product : {} \n\tPrice : {}".format(d[i][0], d[i][1], d[i][2]),
              end="\n")


def main_operations(s):
    page = 1
    nxt = 11
    result = show_searches(page, s)
    total = len(result)

    while True:
        print(colored("\nshowing "+'10'+' results'+', page of '+str(page), 'red'))
        show_result(nxt - 10, nxt, result)

        select = input(colored("\n[{}-{}] / back / next / main : ".format(nxt - 10, nxt - 1), 'yellow')).strip().lower()
        print()
        if select == 'back':
            if nxt >= 21:
                nxt -= 10
                continue
            else:
                break
        elif select == 'next':
            if nxt < total:
                nxt += 10
                continue
            else:
                page += 1
                nxt = 11
                result = show_searches(page, search)
                total = len(result)
                continue
        elif select == 'main':
            break
        try:
            select = int(select)
            if nxt - 10 <= select <= nxt:
                get_product_info(result[select][2])
            else:
                print('invalid selection\n')
        except:
            print('invalid selection\n')


while True:
    search = input(colored("Search : ", 'green')).strip().lower()
    if search == 'exit':
        break
    if search == 'clear':
        os.system('clear')
        continue

    main_operations(search)
