#It will generate data and add to the database.

# sourcery skip: merge-dict-assign, use-named-expression
import requests
from bs4 import BeautifulSoup
from home.models import *


def contest_generator():
    url = 'https://clist.by/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    title_search_tags = soup.find_all('a', class_='title_search')

    # contest_list = []

    for title_search_tag in title_search_tags:
        if response.status_code == 200:
            if title_search_tag:
                link = title_search_tag.get('href')
                title = title_search_tag.get('title')
                # contest_dict = {}
                # contest_dict['title'] = title
                # contest_dict['link'] = link
                # contest_list.append(contest_dict)
                Contest.objects.create(title=title, link=link)
            else:
                print("Anchor tag with class 'title_search' not found.")
        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)


def job_generator():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for job in jobs:
        if response.status_code == 200:
            if job:
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip().capitalize()
                skills = job.find('span', class_ = 'srp-skills').text.strip().replace(' ', '')
                apply_link = job.find('span', class_ = 'sim-posted').text.strip()
                Job.objects.create(company_name = company_name, skills = skills, apply_link = apply_link)
            else:
                print("Anchor tag with class 'title_search' not found.")
        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)





def news_generator():
    pass



# Language converter
# pip install translitcodec
# from translitcodec import translit

# cyrillic_text = "Национальн"

# # Convert Cyrillic to English
# english_text = translit(cyrillic_text, 'ru', reversed=True)

# print(english_text)




