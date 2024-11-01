import requests
from bs4 import BeautifulSoup
import csv

csvFile = open('dataset_scrapping.csv', 'w', newline='')
csvWriter = csv.writer(csvFile)

url = 'https://id.wikipedia.org/wiki/Rumah_Gadang'
res = requests.get(url) #kirimkan header
html = BeautifulSoup(res.text, 'html.parser') #parsing html
proyek = []

for item in html.find_all("img") :
    href = item.get('src')
    proyek.append (href)

csvWriter.writerow(['All IMG'])
for item in proyek:
    csvWriter.writerow([item]) #buat baris pada csv