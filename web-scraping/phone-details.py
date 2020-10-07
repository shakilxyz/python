"""
    I have written the script using list comprehension for reducing the line of the code
    and for running fast. So I am not explaining this.
"""

from bs4 import BeautifulSoup
import requests


def show_info():
    print("""
        In this script I have used https://mobilemaya.com for getting modile details.
        Note that this is a Bangladeshi website. You will find the phones which are available in Bangladesh
        
        Enter single phone name with model or you can search for multiple phones.
        Just separate phone names with semicolon (;) and press enter
        example -> phone1; phone2; phone3 ...\n
    """)


def get_urls(user_input):
    urls =["https://www.mobilemaya.com/?q="+phone+"&about=search" for phone in ["+".join(x.strip().split(" ")) for x in user_input.split(";")]]
    searches = [BeautifulSoup(requests.get(j).content, 'html.parser') for j in urls]
    lst = [i.find_all('div', attrs={'id':'picture'}) for i in searches if i.find_all('div', attrs={'id':'picture'}) != []]
    search_links = []
    for x in lst:
        for y in x:
            search_links.append(y)
    phone_links = ["https://"+j.find('a').attrs.get('href').split('www.')[-1] for j in search_links]
    return phone_links


def get_phone_information(link):
    soup = BeautifulSoup(requests.get(link).content, 'html.parser')
    my_dict = {}
    caption = "\n\tPrice : ".join(soup.find('div', attrs={'id':'caption'}).text.split("Price:"))
    for i in soup.find_all("div", attrs={'class':'pure-g'}):
        if i.find_all('div', attrs={'class': 'pure-u-2-5'}):
            my_dict[i.find('div', attrs={'class': 'pure-u-2-5'}).text] = i.find('div', attrs={'class':'pure-u-3-5'}).text
    return caption, my_dict


def show_result(u):
    for i in get_urls(u):
        print()
        caption, m_dict = get_phone_information(i)
        print("+ "*40)
        print("\t\t",caption)
        print("+ " * 40)
        for k in m_dict.keys():
            print("{:<20}{}".format(k, m_dict[k]))


show_info()
show_result(input("Phone name : "))