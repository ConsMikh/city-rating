## Импорт данных о городах

### Общие данные о городах

| Показатель  | Сайт   | Метод     | Скрипт     | Очищенные данные    |  Примечания                                                                                                                                        |
| :-------------------- | :---------------------------------------------------------- | :---------------------------- | :---------------------------------------- | :------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Численность населения | [Росстат](https://rosstat.gov.ru/compendium/document/13282) | Парсинг файла                 | [rosstat.ipynb](Population/rosstat.ipynb) | [rosstat_clean.csv](Population/rosstat_clean.csv) | Высокодостоверные данные, так как взяты с сайта официальной статистики                                                                                                         |
| Данные о климате      | [Сайт погодные сервисы](http://pogoda-service.ru/)          | Парсинг файла, скрапинг сайта | [climate.py](Climate/climate.py)          | [citiescoor.json](Climate/citiescoor.json)        | Данные вызывают сомнения. Например, для Москвы в начале января указана минимальная температура около 10 градусов мороза. Сомнительно. Не для всех городов легко достать данные |
| Координаты | [Geocoder API](https://docs.2gis.com/ru/api/search/geocoder/overview#nav-lvl2--Прямое_геокодирование) | REST API | [coordinates.ipynb](Coordinates/coordinates.ipynb) | [city_coordinates.csv](Coordinates/city_coordinates.csv) | Доступ к сервису осуществлен по ключу, полученному в исследовательских целях |
| Страна, регион | Wikipedia | Скрапинг сайта | [wikiaddress.ipynb](Common%20information/wikiaddress.ipynb)|[address.json](Common%20information/address.json)||

Тематические сайты
Численность населения:

http://www.statdata.ru/largest_cities_russia

https://города-россия.рф/

Климат:

http://pogoda-service.ru/climate.php

Образование

| Показатель  | Сайт   | Метод     | Скрипт     | Очищенные данные    |  Примечания  |
| :---------- | :----- | :-------- | :--------- | :------------------ | :----------- |
| Рейтинг вузов России | [raex-rr.com](https://raex-rr.com/pro/all_rankings/) | Скрапинг сайта | [top_university.ipynb](Education/top_university.ipynb) | [univercity_rating.json](Education/univercity_rating.json) | Помимо рейтингов содержит: ИНН, регион ВУЗа, ссылку на сайт |

