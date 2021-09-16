import pandas as pd
import time
import random
from selenium import webdriver

def load_page(wd):
    number_of_vagas = int(wd.find_element_by_css_selector('span.results-context-header__job-count').text)

    n_jobs = len(wd.find_elements_by_class_name('base-card__full-link'))

    while n_jobs < number_of_vagas and wd.find_element_by_class_name('inline-notification__text').text != 'Você viu todas as vagas para esta pesquisa':
        n_jobs = len(wd.find_elements_by_class_name('base-card__full-link'))
        wd.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        #print(n_jobs)
        try:
            load_more_jobs_buttom = wd.find_element_by_xpath('//*[@id="main-content"]/section[2]/button').click()
            time.sleep(random.uniform(0.2, 2))
        except:
            pass
            time.sleep(random.uniform(0.2, 2))

def get_jobs(wd):
    job_list = wd.find_element_by_class_name('jobs-search__results-list')
    jobs = job_list.find_elements_by_class_name('base-card base-card--link base-search-card base-search-card--link job-search-card job-search-card--active')

    return jobs

def get_job_details(jobs):
    job_title = []
    job_company_name = []
    job_location = []
    job_date = []
    job_link = []

    for job in jobs:
        try:
            job_title.append(job.find_element_by_class_name('base-search-card__title').text)
        except:
            pass
            job_date.append('None')
        
        try:
            job_company_name.append(job.find_element_by_class_name('base-search-card__subtitle').text)
        except:
            pass
            job_date.append('None')
        
        try:
            job_location.append(job.find_element_by_class_name('job-search-card__location').text)
        except:
            pass
            job_date.append('None')
        
        try:
            job_date.append(job.find_element_by_class_name('job-search-card__listdate').text)
        except:
            pass
            job_date.append('None')
        
        try:
            job_link.append(job.find_element_by_class_name('base-card__full-link').get_attribute('href'))
        except:
            pass
            job_date.append('None')
    
    return job_title, job_company_name, job_location, job_date, job_link

if __name__ == '__main__':
    chromedriver_loc = 'C:/Users/Tiago/Desktop/PostgreSQL Python/LinkedInWebScrape/.driver/chromedriver.exe'
    url = 'https://pt.linkedin.com/jobs/search?keywords=Data%20Analyst&location=Lisboa%2C%20Portugal'
    
    wd = webdriver.Chrome(executable_path=chromedriver_loc)
    wd.get(url)
    wd.maximize_window()

    load_page(wd)
    jobs = get_jobs(wd)

    job_title, job_company_name, job_location, job_date, job_link = get_job_details(jobs)

    print('job_title: ' + str(len(job_title)))
    print('job_company_name: ' + str(len(job_company_name)))
    print('jjob_location: ' + str(len(job_location)))
    print('job_date: ' + str(len(job_date)))
    print('job_link: ' + str(len(job_link)))