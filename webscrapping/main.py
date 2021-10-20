import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract(page_no):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'}
    url = f"https://in.indeed.com/jobs?q=python+developer&start={page_no}0"
    r = requests.get(url,header)
    soup = BeautifulSoup(r.content,"html.parser")
    data = []
    for item in soup.select('#mosaic-provider-jobcards > a'):
        if item.find(title='Python Developer'):
            data.append({
                'title': item.h2.get_text(),
                'Company_Name': item.pre.get_text(),
            })
    data1=pd.DataFrame(data)
    print(data1)

def load(upto):
    for i in range(0, upto):
        extract(i)
        i = +1



upto = int(input("Enter the page no u want to scarp"))
load(upto)

