import os
import requests
from bs4 import BeautifulSoup
import json


headers = {
    "Accept": "text/css,*/*;q=0.1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36"
}

all_url = [
    'https://readmanga.live/vseveduchii_chitatel__A5664',
    'https://readmanga.live/bashnia_boga__A5664',
    'https://mintmanga.live/saga_o_vinlande__A5327',
    'https://readmanga.live/nachalo_posle_konca__A5664',
    'https://readmanga.live/chetyre_vsadnika_apokalipsisa__A5664'
]


def get_data_manga():
    info_manga = []
    for url in all_url:
        req = requests.get(url=url, headers=headers)
        req.encoding = 'UTF8'
        src = req.text

        soup = BeautifulSoup(src, 'lxml')

        title = soup.find('span', class_='name').text
        chapter = soup.find('a', class_='chapter-link read-last-chapter').text[6:]
        if soup.find('div', class_='col-sm-7').find('div', class_='subject-meta').find_all('p')[1].find('b').text == 'Основной переводчик:':
            translation = soup.find('div', class_='col-sm-7').find('div', class_='subject-meta').find_all('p')[2].text[8:].strip()
        else:
            translation = soup.find('div', class_='col-sm-7').find('div', class_='subject-meta').find_all('p')[1].text[8:].strip()

        info_manga.append(
            {
                'Название': title,
                'Количество томов и глав': chapter,
                'Перевод': translation,
                'Ссылка': url
            }
        )

    if not os.path.exists('JSON_FAILS'):
        os.mkdir('JSON_FAILS')

    with open(f"JSON_FAILS/info_manga.json", "w", encoding='utf-8') as file:
        json.dump(info_manga, file, indent=4, ensure_ascii=False)
