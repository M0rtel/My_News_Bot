import os
import json
from selenium import webdriver
from selenium_stealth import stealth  # Очень помогает для обхода блокировок на сайтах
from selenium.webdriver.chrome.service import Service  # новый вид записи driver
from selenium.webdriver.common.by import By  # новый вид записи find_element
from selenium.webdriver.common.action_chains import ActionChains  # при ошибке с click помогает!!!

url = 'https://27jul.zetflix-online.net/films/new_netflix_films/'


def get_data_film():
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")
    # Путь для хром бета
    options.binary_location = "C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
    # Сделать в полный экран
    options.add_argument("--start-maximized")
    # Отключение Webdriver
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Фоновый режим
    # options.add_argument('--headless')

    options.add_experimental_option("excludeSwitches", ["enable-automation"])  # selenium-stealth
    options.add_experimental_option('useAutomationExtension', False)  # selenium-stealth

    try:
        service = Service(executable_path="104.exe")
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url=url)

        # selenium-stealth
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win64",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

        actions = ActionChains(driver)
        info_films = []
        films_page = len(driver.find_elements(By.CLASS_NAME, 'vi-in'))
        for num in range(1, films_page + 1):
            href_film = driver.find_element(By.XPATH, f'//*[@id="dle-content"]/div[{num}]/div/a')
            url_film = href_film.get_attribute('href')
            name_film = driver.find_element(By.XPATH, f'//*[@id="dle-content"]/div[{num}]/div/a/div[1]/div').text
            actions.move_to_element(href_film).click().perform()

            rating = driver.find_elements(By.XPATH, '//*[@id="dle-content"]/article/div[1]/div/div[1]/span')
            rating_list = []
            for rating_ in rating:
                rating_list.append(rating_.text)

            try:
                year_film = driver.find_element(By.XPATH, '//*[@id="finfo"]/li[1]/span[2]').text
            except:
                year_film = 'нет'

            try:
                director = driver.find_element(By.XPATH, '//*[@id="finfo"]/li[4]/span[2]').text
            except:
                driver = 'нет'

            try:
                country = driver.find_element(By.XPATH, '//*[@id="finfo"]/li[3]').text[8:]
            except:
                country = 'нет'

            info_films.append(
                {
                    'Название': name_film,
                    'Рейтинг': rating_list,
                    'Год выхода': year_film,
                    'Режиссёр': director,
                    'Страна': country,
                    'Ссылка': url_film
                }
            )

            driver.back()

    except Exception as ex:
        print(ex)

    finally:
        driver.close()  # Выключение окна
        driver.quit()  # Выключение chrome

    if not os.path.exists('JSON_FAILS'):
        os.mkdir('JSON_FAILS')

    with open(f"JSON_FAILS/info_films.json", "w", encoding='utf-8') as file:
        json.dump(info_films, file, indent=4, ensure_ascii=False)
