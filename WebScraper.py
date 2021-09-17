import time
import random
from selenium import webdriver
""" NOT USED
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""

class LinkedIn_WebScraper:
    def __init__(self, url, chromedriver_loc):
        self.url = url
        self.chromedriver_loc = chromedriver_loc

    def run(self):
        self.wd = webdriver.Chrome(executable_path=self.chromedriver_loc)
        self.wd.get(self.url)
        self.wd.maximize_window()

        self.load_page()
        self.get_jobs()
        job_title, job_company_name, job_location, job_date, job_link = self.get_job_details()

        return job_title, job_company_name, job_location, job_date, job_link

    
    def load_page(self):
        number_of_vagas = int(self.wd.find_element_by_css_selector('span.results-context-header__job-count').text)

        n_jobs = len(self.wd.find_elements_by_class_name('base-card__full-link'))

        while n_jobs < number_of_vagas and self.wd.find_element_by_class_name('inline-notification__text').text != 'Você viu todas as vagas para esta pesquisa':
            n_jobs = len(self.wd.find_elements_by_class_name('base-card__full-link'))
            self.wd.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            try:
                load_more_jobs_buttom = self.wd.find_element_by_xpath('//*[@id="main-content"]/section[2]/button').click()
                time.sleep(random.uniform(0.2, 2))
            except:
                pass
                time.sleep(random.uniform(0.2, 2))

    def get_jobs(self):
        job_list = self.wd.find_element_by_class_name('jobs-search__results-list')
        self.jobs = job_list.find_elements_by_tag_name('li')
        return self.jobs
    
    def get_job_details(self):
        job_title = []
        job_company_name = []
        job_location = []
        job_date = []
        job_link = []

        for job in self.jobs:
            try:
                job_title.append(job.find_element_by_class_name('base-search-card__title').text)
            except:
                pass
                job_title.append('None')
            
            try:
                job_company_name.append(job.find_element_by_class_name('base-search-card__subtitle').text)
            except:
                pass
                job_company_name.append('None')
            
            try:
                job_location.append(job.find_element_by_class_name('job-search-card__location').text)
            except:
                pass
                job_location.append('None')
            
            try:
                job_date.append(job.find_element_by_class_name('job-search-card__listdate').text)
            except:
                try:
                    job_date.append(job.find_element_by_class_name('job-search-card__listdate--new').text)
                except:
                    job_date.append('None')
            
            try:
                job_link.append(job.find_element_by_class_name('base-card__full-link').get_attribute('href'))
            except:
                try:
                    job_link.append(job.find_element_by_tag_name('a').get_attribute('href'))
                except:
                    job_link.append('None')
        
        return job_title, job_company_name, job_location, job_date, job_link

    def wd_quit(self):
        self.wd.quit()
#-----------------------------------------------------------------------------------#