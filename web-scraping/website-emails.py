# This script is for finding all email addresses of a website
# Used requests for handling HTTP/HTTPS requests and bs4 for handling html elements
# re for extracting emails from soup object

import re
import requests
from bs4 import BeautifulSoup

# defining two empty lists ,one for different urls found from web-pages another is for storing all emails
# we need to scrap all pages of a website so we need to find all the links of the site
# We are storing all visited links in the list which we already scraped.
# Because we don't want to scrap any single page more than one time

url_list = []
email_list = []
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}


# function for scrape web-page. used recursion for scraping multiple pages by only one function
# we will take all urls from a page and scrap only links which contains the keyword.
# Because we don't want to find information from other sites
# the keyword is the part of the domain. Like https://example.com then the keyword can be 'example'

def get_emails_and_urls(url, key_word, save):
    try:
        page = requests.get(url, headers=headers)
    except:
        return

    # creating a bs4 object for finding html elements from the webpage
    soup = BeautifulSoup(page.content, 'html.parser')

    # regex query for getting all emails from the website
    emails = [i for i in re.findall('[\w.]+@[a-z.]+', soup.decode())]
    for i in emails:
        if i not in email_list:
            if save:
                file = open('emails ('+key_word+').txt', 'a')
                file.write(i+'\n')
                file.close()

            email_list.append(i)
            print(i)
    urls = [i.attrs.get('href').strip() for i in soup.findAll('a') if i.attrs.get('href') is not None]
    for i in urls:
        if key_word in i and i not in url_list and ('http' in i or 'www.' in i):
            url_list.append(i)
            get_emails_and_urls(i, key_word, save)


# extract a keyword from the main url
def get_keyword(url):
    url = url.split('//')[-1]
    if 'www.' in url:
        url = url.split('www.')[-1]
        key_word = url.split('.')[0]
    else:
        key_word = url.split('.')[0]
    return key_word


# when we start the program the code will scrap the main page associated with user inputted link
# so first appending the main url to the url_list because it will be scraped at the beginning of the execution

url_list.append(input("Enter website's url : ").strip())

print("\nIf you want to save the emails in a file first check if any file named like 'emails (your-domain).txt' exists "
      "in your directory. If the file exists please move or delete or rename to avoid overwrite the file\n")
# check if user want's to save all emails in a text file
save = input('Do you want to save emails ? [y/any] : ').lower()

if save == 'y':
    get_emails_and_urls(url_list[0], get_keyword(url_list[0]), True)
else:
    get_emails_and_urls(url_list[0], get_keyword(url_list[0]), False)