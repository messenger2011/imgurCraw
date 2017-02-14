import re
import os
import sys
import requests
import threading

def download(link, filelocation):
    r = requests.get(link, stream=True)
    with open(filelocation, 'wb') as f:
        for chunk in r.iter_content(1024):
            if chunk:
                f.write(chunk)

def cDownload(link, filelocation):
    try:
        print("Downloading -> ", link)
        download_thread = threading.Thread(target=download, args=(link,filelocation))
        download_thread.start()
    except Exception(e):
        print ("Error -> ", e)

class Parser():

    def find_by_regex(self, regex, html):
        try:
            p = re.findall(r'{}'.format(regex), html);
            return p
        except:
            print ('Regex error!')
            return []

    def search(self, q):
        url = 'http://imgur.com/t/' + q
        r = requests.get(url, verify=True)
        if r.status_code == 200:
            return r.text

def craw(q):
    if (os.path.isdir == False or os.path.exists('images') == False):
        os.mkdir('images')
    parser = Parser()

    for text in q.split(','):
        print("Trying -> ", text)
        ids = parser.find_by_regex('/t/([a-zA-Z0-9]+)/([a-zA-Z0-9]+)', parser.search(text))
        if (ids):
            for id in ids:
                img = 'http://i.imgur.com/' + id[1] + '.jpg'
                cDownload(img, 'images/' + id[1])

craw('girl,sexy,sweet,lewd,cat,big+boobs,chubby')