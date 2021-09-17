import pandas as pd
from WebScraper import LinkedIn_WebScraper

def data_to_csv(job_title, job_company_name, job_location, job_date, job_link, custom_encoding = 'UTF-8', custom_name='exported_data.csv'):
    all_data = pd.DataFrame({'Title': job_title,
    'Company': job_company_name,
    'Location': job_location,
    'Date': job_date,
    'Link': job_link
    })

    all_data.to_csv(custom_name, index=False ,header=True, sep=';', encoding=custom_encoding)
    
if __name__ == '__main__':    
    url = 'https://pt.linkedin.com/jobs/search?keywords=Data%20Analyst&location=Lisboa%2C%20Portugal'
    chromedriver_loc='C:/Users/Tiago/Desktop/PostgreSQL Python/LinkedInWebScrape/.driver/chromedriver.exe'

    WS = LinkedIn_WebScraper(url, chromedriver_loc)
    WS.run()
    WS.load_page()
    WS.get_jobs()

    job_title, job_company_name, job_location, job_date, job_link = WS.get_job_details()

    print('job_title: ' + str(len(job_title)))
    print('job_company_name: ' + str(len(job_company_name)))
    print('job_location: ' + str(len(job_location)))
    print('job_date: ' + str(len(job_date)))
    print('job_link: ' + str(len(job_link)))

    WS.wd_quit()

    data_to_csv(job_title, job_company_name, job_location, job_date, job_link)
#-----------------------------------------------------------------------------------#
