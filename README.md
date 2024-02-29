# BiteBase

BiteBase is a Django-based web application that provides real-time information from various trusted sources. It offers features like contests and hackathons, job listings, and breaking news updates.

Website Link: https://bitebase.onrender.com/


## Installation

Clone the repository:

git clone https://github.com/nag2mani/NewsFeed.git


## Install dependencies:

pip install -r requirements.txt


## Run migrations:

python manage.py makemigrations
python manage.py migrate


## Start the development server:

python manage.py runserver

Visit http://127.0.0.1:8000/ in your web browser to access the application.


## Urls Pattern

path('', home, name='home'),

path('contest/', contest, name='contest'),

path('job/', job, name='job'),

path('news/', news, name='news'),

path("login/", login_page, name='login'),

path("logout/", logout_page, name='logout'),

path("signup/", signup, name='signup'),

path("contact/", contact, name='contact'),

path("add_your_news/", add_your_news, name='add_your_news'),



**Website Summary:**

Our website is a comprehensive platform that aggregates real-time data from various sources to provide users with valuable information on hackathons, coding contests, job opportunities, and news articles. Here's a summary of its key features:


1. **Hackathons and Coding Contests:**
   - Our website scrapes data from multiple websites worldwide to gather information about hackathons and coding contests.
   - This data is then stored in our database for easy access and management.
   - Users can explore upcoming hackathons and coding contests directly from our platform, making it convenient to find and participate in events of interest.


2. **Job Listings:**
   - Similar to hackathons, our website collects job listings from various sources on the internet.
   - Users can browse through a wide range of job opportunities conveniently aggregated on our platform.
   - By providing access to diverse job listings, we aim to help users find suitable employment opportunities more efficiently.


3. **News Articles:**
   - Our website also curates news articles from different sources, presenting users with the latest headlines and summaries.
   - Users can stay informed about current events, industry updates, and trending topics without the need to visit multiple websites.
   - The summarized news articles make it easy for users to grasp the key information quickly and efficiently.


Through these features, our website aims to empower users with valuable insights and opportunities, making it a one-stop destination for staying updated and discovering relevant content in the realms of technology, innovation, and professional development.



TechStack used;

1. HTML5
2. CSS
3. Bootstrap
4. Javascript
5. Python
6. Django
7. SQL
8. Machine Learning Model



Team:
Nagmani Kumar Team Lead [Backend and ML], 
Ram Bhanwar Bhadiyar [FrontEnd Developer], 
Amit Diwakar [UI/UX Designer]

