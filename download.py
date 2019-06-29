import requests, os
from bs4 import BeautifulSoup
from time import sleep
from dotenv import load_dotenv, find_dotenv
from pytube import YouTube
load_dotenv(find_dotenv())
        

def download_file(url, base=None):
    yt = YouTube(url)
    title = yt.title
    video = yt.streams.filter(progressive=True, subtype='mp4').order_by('resolution').desc().last()
    print(title)
    path = os.path.join(base, video.default_filename)
    if (os.path.exists(path)):
        print('file already exist in folder')
    else:
        video.download(base)
        print('completed')



def main():
    base = os.getenv('BASEPATH')
    channel_url = os.getenv('CHANNEL')
    re = requests.get(channel_url)
    soup = BeautifulSoup(re.text, 'html.parser')
    links = soup.findAll('a')
    urls = []

    for link in links:
        url = link.get('href')
        if 'watch' in url and url not in urls:
            urls.append(url)

    for url in urls:
        download_file('https://www.youtube.com'+url, base)
        sleep(3)

main()
