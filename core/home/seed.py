import requests
from bs4 import BeautifulSoup
from home.models import *
import math
import nltk
from nltk.tokenize import word_tokenize


# Download the necessary NLTK resources.
nltk.download('punkt')
nltk.download('universal_tagset')


def contest_generator():
    # This function scrap contests from web and put it into our database for further uses.
    url = 'https://clist.by/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
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
    # This function scrap jobs from web and put it into our database for further uses.
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for job in jobs:
        if response.status_code == 200:
            if job:
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip().capitalize()
                skills = job.find('span', class_ = 'srp-skills').text.strip().replace(' ', '')
                apply_link = 'https://shorturl.at/cuvMU'
                posted_date = job.find('span', class_ = 'sim-posted').text.strip()
                Job.objects.create(company_name = company_name, skills = skills, posted_date = posted_date, apply_link = apply_link)
            else:
                print("Anchor tag with class 'title_search' not found.")
        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)


def news_generator():
    # This function scrap news with their title and data from web and put it into our database for further uses.
    url = 'https://timesofindia.indiatimes.com/briefs'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news = soup.find_all('div', class_='brief_box')

    ML_Model_cofficient = [1.34674492, -3.96302032, 2.06307081]  #Theta-0(const), Theta-1(adj/pron), Theta-2(adv/adj)

    for new in news:
        if response.status_code == 200:
            if new.find('h2'):
                headline = new.find('h2').find('a').text.strip()
            if new.find('p'):
                summary = new.find('p').find('a').text.strip()
                apply_link = 'https://timesofindia.indiatimes.com/india/bhai-dont-tell-ma-that-im-trapped-in-tunnel/articleshow/105299928.cms'
            
            # Tokenize the text into words
            words = word_tokenize(summary)
            # Tag the words using NLTK's pos_tag function with the universal tagset
            tagged_words = nltk.pos_tag(words, tagset='universal')
            # Count the number of adjectives (ADJ), adverbs (ADV), and pronouns (PRON)
            adj_count = sum(1 for word, tag in tagged_words if tag == 'ADJ')
            adv_count = sum(1 for word, tag in tagged_words if tag == 'ADV')
            pron_count = sum(1 for word, tag in tagged_words if tag == 'PRON')

            # Handling division by 0
            if (adj_count and pron_count) != 0:
            # Calculate z
                z = ML_Model_cofficient[0] + ML_Model_cofficient[1] * (adj_count/pron_count) + ML_Model_cofficient[2] * (adv_count / adj_count)
            else:
                z = ML_Model_cofficient[0]

            # Calculate sigmoid
            sigmoid = 1 / (1 + math.exp(-z))

            rounded_sigmoid = round(sigmoid ,4) * 100

            if rounded_sigmoid > 0:

                News.objects.create(headline = headline, summary = summary, link = apply_link, percent = rounded_sigmoid)

        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)


# Here I am calling the function for adding data into databses.
news_generator()
contest_generator()
job_generator()


