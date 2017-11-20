import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime

file_name = "%s.csv" % datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
num_pages = 3
google_url = "https://www.google.ru/search?q=ico+company+list&oq=ico+company+list&start=%s"

links_final = []
for i in range(num_pages):
    offset = i*10
    google_url_w_offset = google_url % offset

    page = requests.get(google_url_w_offset)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print soup.prettify()


    for link in soup.find_all('a'):
        if link.parent.get('class') and link.parent.get('class')[0] == u"r":
            links_final.append([link.get('href').replace("/url?q=", "")])

with open(file_name, 'wb') as file:
    for link in links_final:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        wr.writerow(link)
#
#
# # [
# #     ["a", "b", "c"],
# #     ["d", "e", "f"]
# # ]
