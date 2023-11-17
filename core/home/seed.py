#It will generate data and add to the database.

# sourcery skip: merge-dict-assign, use-named-expression
import requests
from bs4 import BeautifulSoup
from home.models import Contest



# html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python').text
# # print(html_text)
# soup = BeautifulSoup(html_text, 'lxml')
# # print(soup)
# jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

# for job in jobs:
#     company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip().capitalize()
#     # print(company_name)
#     skills = job.find('span', class_ = 'srp-skills').text.strip().replace(' ', '')
#     # print(skills)
#     published_date = job.find('span', class_ = 'sim-posted').text.strip()
#     # print(published_date)

#     print(f"""
#     Company name : {company_name}
#     Required skills : {skills}
#             """)




url = 'https://clist.by/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
title_search_tags = soup.find_all('a', class_='title_search')

contest_list = []

for title_search_tag in title_search_tags:
    if response.status_code == 200:
        if title_search_tag:
            link = title_search_tag.get('href')
            title = title_search_tag.get('title')
            contest_dict = {}
            contest_dict['title'] = title
            contest_dict['link'] = link
            # contest_list.append(contest_dict)
            Contest.objects.create(title=title, link=link)
        else:
            print("Anchor tag with class 'title_search' not found.")
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)




# Language converter
# pip install translitcodec
# from translitcodec import translit

# cyrillic_text = "Национальн"

# # Convert Cyrillic to English
# english_text = translit(cyrillic_text, 'ru', reversed=True)

# print(english_text)




