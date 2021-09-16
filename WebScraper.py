import pandas as pd
import time
import random
from selenium import webdriver

url = 'https://pt.linkedin.com/jobs/search?keywords=Data%20Analyst&location=Lisboa%2C%20Portugal'
chromedriver_loc = 'C:/Users/Tiago/Desktop/PostgreSQL Python/LinkedInWebScrape/.driver/chromedriver.exe'

wd = webdriver.Chrome(executable_path=chromedriver_loc)
wd.get(url)
wd.maximize_window()

number_of_vagas = int(wd.find_element_by_css_selector('span.results-context-header__job-count').text)

n_jobs = len(wd.find_elements_by_class_name('base-card__full-link'))

while n_jobs < number_of_vagas and wd.find_element_by_class_name('inline-notification__text').text != 'Você viu todas as vagas para esta pesquisa':
    n_jobs = len(wd.find_elements_by_class_name('base-card__full-link'))
    wd.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    print(n_jobs)
    try:
        load_more_jobs_buttom = wd.find_element_by_xpath('//*[@id="main-content"]/section[2]/button').click()
        time.sleep(random.uniform(0.2, 2))
    except:
        pass
        time.sleep(random.uniform(0.2, 2))





print(n_jobs)