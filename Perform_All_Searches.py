import json
import pandas as pd
from datetime import datetime
import locale
from WebScraper import LinkedIn_WebScraper

def get_all_search_criteria():
    with open("all_search_criterias.json", "r") as f:
        json_content = json.load(f)
        all_search_criteria = json_content["all_searches"]
    return all_search_criteria

def get_search_criteria():
    with open("search_criteria.json", "r") as f:
        search_criteria = json.load(f)
    return search_criteria

def parse_job_name(name):
    name = name.replace(' ', '%20')
    return name

def parse_job_location(location):
    location = location.replace(', ', '%2C%20')
    return location

def data_to_csv(job_title, job_company_name, job_location, job_date, job_link, custom_encoding = 'UTF-8', custom_name='exported_data.csv'):
    all_data = pd.DataFrame({'Title': job_title,
    'Company': job_company_name,
    'Location': job_location,
    'Date': job_date,
    'Link': job_link
    })

    all_data.to_csv(custom_name, index=False ,header=True, sep=';', encoding=custom_encoding)
    
if __name__ == '__main__':

    all_search_criteria = get_all_search_criteria()

    for search_criteria in all_search_criteria:
        name = search_criteria["job"]
        location = search_criteria["location"]


        job_search_name = parse_job_name(name)
        job_search_location = parse_job_location(location)

        url = 'https://pt.linkedin.com/jobs/search?keywords={}&location={}'.format(job_search_name, job_search_location)
        chromedriver_loc='C:/Users/Tiago/Desktop/PostgreSQL Python/LinkedInWebScrape/.driver/chromedriver.exe'

        WS = LinkedIn_WebScraper(url, chromedriver_loc)
        job_title, job_company_name, job_location, job_date, job_link = WS.run()

        print('job_title: ' + str(len(job_title)))
        print('job_company_name: ' + str(len(job_company_name)))
        print('job_location: ' + str(len(job_location)))
        print('job_date: ' + str(len(job_date)))
        print('job_link: ' + str(len(job_link)))

        WS.wd_quit()

        locale.setlocale(locale.LC_TIME, "pt_PT.UTF-8")
        today_date = datetime.today().strftime('%Y-%m-%d')
        output_file_name = today_date +'_' + name + '_' + location + '.csv'
        output_file_name = output_file_name.replace('"', '')
        output_file_name = output_file_name.replace(', ', '-')
        output_file_name = 'Scraped_Data/'+ output_file_name
        
        data_to_csv(job_title, job_company_name, job_location, job_date, job_link, custom_name=output_file_name)