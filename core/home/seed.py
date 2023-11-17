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


contest_list_a = contest_list[:25]

contest_list_all = [{'title': 'BlackHat MEA CTF Final 2023', 'link': 'https://ctftime.org/event/2113/'}, {'title': '2019 - 2021 Selected ICPC Finals problems', 'link': 'https://clist.by/standings/2019-2021-selected-icpc-finals-problems-47089378/'}, {'title': 'Google - Fast or Slow? Predict AI Model Runtime [artificial intelligence, retrieval/ranking, tpu, graph, graph neural network]', 'link': 'https://clist.by/standings/google-fast-or-slow-predict-ai-model-runtime-artificial-intelligence-retrievalranking-tpu-graph-graph-neural-network-45822306/'}, {'title': 'Lux AI Season 2 - NeurIPS Stage 2 [video games, simulations]', 'link': 'https://clist.by/standings/lux-ai-season-2-neurips-stage-2-video-games-simulations-46336924/'}, {'title': 'NeurIPS 2023 - Machine Unlearning [research, deep learning]', 'link': 'https://clist.by/standings/neurips-2023-machine-unlearning-research-deep-learning-46110230/'}, {'title': 'Open Problems – Single-Cell Perturbations [genetics, biotechnology, tabular]', 'link': 'https://clist.by/standings/open-problems-single-cell-perturbations-genetics-biotechnology-tabular-46135523/'}, {'title': 'Regression with a Mohs Hardness Dataset [beginner, tabular, regression, earth science]', 'link': 'https://clist.by/standings/regression-with-a-mohs-hardness-dataset-beginner-tabular-regression-earth-science-47846737/'}, {'title': 'Child Mind Institute - Detect Sleep States [health, time series analysis, multiclass classification]', 'link': 'https://clist.by/standings/child-mind-institute-detect-sleep-states-health-time-series-analysis-multiclass-classification-45970468/'}, {'title': 'Stanford Ribonanza RNA Folding [biology, biotechnology, chemistry, video games, regression]', 'link': 'https://clist.by/standings/stanford-ribonanza-rna-folding-biology-biotechnology-chemistry-video-games-regression-46019475/'}, {'title': 'Optiver - Trading at the Close [tabular, finance]', 'link': 'https://clist.by/standings/optiver-trading-at-the-close-tabular-finance-46336195/'}, {'title': 'CAFA 5 Protein Function Prediction [biology]', 'link': 'https://clist.by/standings/cafa-5-protein-function-prediction-biology-42623949/'}, {'title': 'UBC Ovarian Cancer Subtype Classification and Outlier Detection (UBC-OCEAN) [image, classification]', 'link': 'https://clist.by/standings/ubc-ovarian-cancer-subtype-classification-and-outlier-detection-ubc-ocean-image-classification-46753572/'}, {'title': 'NFL Big Data Bowl 2024 [sports, exploratory data analysis, football]', 'link': 'https://www.kaggle.com/competitions/nfl-big-data-bowl-2024'}, {'title': 'Linking Writing Processes to Writing Quality [education, nlp, primary and secondary schools]', 'link': 'https://clist.by/standings/linking-writing-processes-to-writing-quality-education-nlp-primary-and-secondary-schools-46651669/'}, {'title': 'LLM - Detect AI Generated Text [education, primary and secondary schools, binary classification, text generation]', 'link': 'https://clist.by/standings/llm-detect-ai-generated-text-education-primary-and-secondary-schools-binary-classification-text-generation-47485824/'}, {'title': 'Enefit - Predict Energy Behavior of Prosumers [tabular, energy, time series analysis]', 'link': 'https://clist.by/standings/enefit-predict-energy-behavior-of-prosumers-tabular-energy-time-series-analysis-47550689/'}, {'title': 'SenNet + HOA - Hacking the Human Vasculature in 3D [health, image segmentation, computer vision]', 'link': 'https://clist.by/standings/sennet-hoa-hacking-the-human-vasculature-in-3d-health-image-segmentation-computer-vision-47667973/'}, {'title': 'RIC 2 [public, icpc, individual]', 'link': 'https://lightoj.com/contest/ric2'}, {'title': 'Cricket Code Champions Hack. Hackathon', 'link': 'https://www.hackerearth.com/de/challenges/hackathon/cricket-code-champions-hack/'}, {'title': 'Canara DACOE-Thon (Data Analytics Centre of Excellence)', 'link': 'https://canara-dacoethon.hackerearth.com/de/'}, {'title': "COCI '23 Contest 1 Unofficial Mirror", 'link': 'https://clist.by/standings/coci-23-contest-1-unofficial-mirror-47752625/'}, {'title': "Scholarship Test 11th to 20th Nov'23", 'link': 'https://www.codingninjas.com/codestudio/contests/scholarship-test-11th-to-20th-nov-23'}, {'title': 'Командный.03афон по программированию "HELLO, WORLD!", Тренировка', 'link': 'https://clist.by/standings/komandnyi03afon-po-programmirovaniiu-hello-world-trenirovka-47336721/'}, {'title': 'Алгоритмы и структуры данных / Осень 2023. Очереди. Деки и стеки', 'link': 'https://cups.online/rounds/964'}, {'title': 'Выходи решать тест серт. математика серт тест', 'link': 'https://clist.by/standings/vykhodi-reshat-test-sert-matematika-sert-test-47459550/'}]



# Language converter
# pip install translitcodec
# from translitcodec import translit

# cyrillic_text = "Национальн"

# # Convert Cyrillic to English
# english_text = translit(cyrillic_text, 'ru', reversed=True)

# print(english_text)



