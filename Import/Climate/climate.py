import re

import pandas as pd

from time import sleep

from IPython.display import clear_output

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json

# Загрузка данных об идентификаторах погодных станций. 
# Идентификаторы были получены вручную. Был открыт выпадающий список с перечнем
# доступных станций на странице http://pogoda-service.ru/climate.php. 
# Этот список быд исследован в браузере, тег, содержащий
# все идетификаторы был вручную скопирован в файл. Файл далее парсится скриптом.
# Результат записывает в словарь stationsdict

with open('Import/Climate/StationsRaw.txt', encoding='utf-8') as f:
    text = f.read()

options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(chrome_options=options)

res = re.findall(r'<option value="\d{6}">[а-яА-Я- ()]*</option>',text)
stations = []
for i in res:
    station = []
    station.append(re.findall(r'>[а-яА-Я- ()]*<',i)[0][1:-1])
    station.append(re.findall(r'\d{5,}',i)[0])
    stations.append(station)
stationsdict = dict(stations)

# Загрузка данных о климате в городе.
# Используя идентификаторы станций, формируется ссылка для запроса таблицы с данными климата.
# Полученная страница парсится. Для каждого города получаются:
# - широта
# - долгота
# - для каждого дня года:
#   * Максимальная (Tmax), минимальная (Tmin), средняя температура (Tavg) (градусы Цельсия)
#   * Атмосферное давление (Pres) (гектопаскали)
#   * Скорость ветра (Wspeed) (метры в секунду)
#   * Осадки (Rain) (миллиметры)
#   * Эффективная температура (Tef) (градусы Цельсия)
# Результат записывается в файл JSON

citydf = pd.read_csv('Import/Population/rosstat_clean.csv',encoding='cp1251')
cityAn = citydf['City'].to_list()

citynone = []
citiescoor =[]

for city in cityAn:
    if (stationsdict.get(city, 'none') != 'none'):
        print(city)
        url = r'http://pogoda-service.ru/climate_table.php?country=RS&station=' + stationsdict[city] + r'&day_begin=01&month_begin=01&day_end=31&month_end=12'
        browser.get(url)
        html = browser.page_source
        coor = re.findall(r'Географические координаты: [0-9.,]*',html)[0].split(' ')
        lat = coor[2].split(',')[0]
        lon = coor[2].split(',')[1]
        
        climateday = {}
        trlist = browser.find_elements(By.TAG_NAME, 'tr')
        for i in range(10,len(trlist)):
            climateline = trlist[i].text.split(' ')
            try:
                climateday[climateline[0]+' '+climateline[1]] = {'Tmax': climateline[2], 'Tmin': climateline[3], 'Tavg': climateline[4], 'Pres': climateline[5], 'Wspeed': climateline[6], 'Rain': climateline[7], 'Tef': climateline[8]}
            except: 1
        
        citycoor = {'city': city, 'lat': lat, 'lon': lon, 'climate': climateday}
        citiescoor.append(citycoor)
        sleep(10)
    else:
        citynone.append(city)

with open('Import/Climate/citiescoor.json', 'w') as file:
    json.dump(citiescoor, file, indent=2, ensure_ascii=False)
