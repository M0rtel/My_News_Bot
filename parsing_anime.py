import os
import requests
from bs4 import BeautifulSoup
import json


headers = {
    "Accept": "text/css,*/*;q=0.1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36"
}

all_url = [
    'https://amedia.online/1177-mozhet-ja-vstrechu-tebja-v-podzemele-4.html',
    'https://amedia.online/1167-sozdannyj-v-bezdne-2.html',
    'https://amedia.online/1112-aoj-asito.html'
]


def get_data_anime():
    info = []
    for url in all_url:
        req = requests.get(url=url, headers=headers)
        req.encoding = 'UTF8'
        src = req.text

        soup = BeautifulSoup(src, 'lxml')

        title = soup.find('article', class_='film-wr').find('h1').text[: -17]
        total_series = int(soup.find('div', class_='info').find_all('span')[0].text[: -6])

        if soup.find('div', class_='info').find_all('span')[1].text[: -6][-1] == '+':
            app_series = int(soup.find('div', class_='info').find_all('span')[1].text[: -7])
        else:
            app_series = int(soup.find('div', class_='info').find_all('span')[1].text[: -6])

        info.append(
            {
                'Название': title,
                'Добавленные серии': total_series,
                'Все серии': app_series,
                'Ссылка': url
            }
        )

    if not os.path.exists('JSON_FAILS'):
        os.mkdir('JSON_FAILS')

    with open(f"JSON_FAILS/info_anime.json", "w", encoding='utf-8') as file:
        json.dump(info, file, indent=4, ensure_ascii=False)
