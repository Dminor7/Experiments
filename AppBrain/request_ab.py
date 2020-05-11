import os
import requests 
from bs4 import BeautifulSoup
import time
import logging

FORMAT = "[%(asctime)s, %(levelname)s ] %(message)s"
logging.basicConfig(filename='Test.log', level=logging.DEBUG, format=FORMAT)

class AppBrain(object):
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        # self.output_dir = self.home_dir + "/" + "outgoing"

    def change_log(self, url_list):
        if not url_list:
            return 
        # os.makedirs(self.output_dir, exist_ok=True)

        for url in url_list:
            try:
                page = requests.get(url)
                if(page.status_code == 200):
                    soup = BeautifulSoup(page.text, 'html.parser')
                    filename = url.split("/")[-1].split(".")[-1] + ".txt"
                    with open(filename,"a") as f:
                        for ultag in soup.find_all('ul',class_='app-changelog'):
                            for litag in ultag.find_all('li'):
                                date        = litag.find('span',class_='app-changelog-date').text
                                status        = litag.find('span',class_='app-changelog-type').text
                                description = litag.find('span',class_='app-changelog-description').text
                                f.write(date.strip() + " " + status.strip() + " " + description.strip() + "\n")
                    file_stats = os.stat(filename)
                    size = file_stats.st_size/(1024*1024)
                    if(size > 0):
                        logging.info("Successfully recieved data from {}".format("url"))
                    else:
                        logging.warning("Didn't received data from {}".format(url))
                else:
                    logging.error("Request failed with status code {}".format(page.status_code))
            except Exception as e:
                logging.exception("Error occured while requesting url {}, error {}".format(url,e))


    def scrape(self, url_list, num_requests=1):
        for _ in range(num_requests):
            self.change_log(url_list)
            time.sleep(10)


