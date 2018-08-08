from bs4 import BeautifulSoup
import requests
import urllib.request
import time

base_url = 'https://7gogo.jp/oguri-yui/images'
path = '755_download/oguri-yui/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# 进入子网页


def get_main_url():
    source_url = []
    wb_data = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    urls = soup.select('a._1RHwM1Y-')
    for i in urls:
        main_urls = i.get('href')
        source_url.append('https://7gogo.jp' + str(main_urls))
    # print(source_url)
    return source_url
# 获取图片链接


def get_img_url(furl):
    img_urls = []
    wb_data = requests.get(furl, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    imgs = soup.select('div.AlTY-23- img')
    for i in imgs:
        img_urls.append(i.get('data-src'))
    # print(img_urls)
    return img_urls

# 下载图片


def download_imgs(url):
    urllib.request.urlretrieve(
        url, path + url.split('/')[4] + url.split('/')[5] + '.jpg')
    print('Done')
    time.sleep(1)

if __name__ == '__main__':
    for furl in get_main_url():
        data = []
        for url in get_img_url(furl):
            download_imgs(url)
