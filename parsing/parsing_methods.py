import requests
from bs4 import BeautifulSoup
import pandas as pd
from parsing import config


def get_html(text) -> str:
    """Метод получения html страницы по запросу"""

    # параметры запроса
    params = {'text': text, 'lr': '213', 'clid': '9582', 'suggest_reqid': '753027389159888357950561896282144'}

    # получение запроса с параметрами
    response = requests.get('https://yandex.ru/search/', params=params, cookies=config.cookies, headers=config.headers)

    if response.status_code == 200:  # проверка на успешно выполненный запрос
        # возврат html страницы
        return response.text
    else:
        raise 'Error in get_html(): Problems with request, be careful captcha'


def get_data_items(html) -> dict:
    """Метод ищет нужные данные из страницы и формирует словарь с ними"""
    # BS для поиска нужной информации на странице
    soup = BeautifulSoup(html, 'lxml')
    # словарь в котором будет храниться информация по первым 10 ссылкам
    query_result = dict()
    try:
        # поиск все тегов li с указанным классом и делаем срез, чтобы ограничиться 10-ю
        li_arr = soup.findAll('li', {'class': 'serp-item serp-item_card'})[:10]
        # поиск информации по каждому тегу li
        for i in range(len(li_arr)):
            # Номер в поиске
            index = int(li_arr[i].get('data-cid'))
            # Заголовок
            header = li_arr[i].find('span', {'class': 'OrganicTitleContentSpan organic__title'}).text
            # Описание
            description = li_arr[i].find('span', {'class': 'OrganicTextContentSpan'}).text
            # Ссылка
            link = li_arr[i].find('a', {'class': 'Link Link_theme_normal OrganicTitle-Link organic__url link'}).get(
                'href')
            # добавление записи в словарь
            query_result[index] = {'header': header,
                                   'description': description,
                                   'link': link}
        return query_result
    except AttributeError as e:
        print("Error in get_data_items(): ", e)
    except IndexError as e:
        print("Error in get_data_items(): ", e)


def collect_into_table(query_result, text):
    """Формирование таблицы с данными и генерация xlsx файла"""
    # создание Dataframe колоннами
    df_data = pd.DataFrame(columns=['Номер в списке', 'Заголовок', 'Описание', 'Ссылка'])
    # добавление элементов в Dataframe
    for key in query_result.keys():
        new_row = {'Номер в списке': key, 'Заголовок': query_result[key]['header'],
                   'Описание': query_result[key]['description'], 'Ссылка': query_result[key]['link']}
        # добавление нового элемента в Dataframe
        df_data = df_data.append(new_row, ignore_index=True)
    try:
        # создание xlsx файла
        df_data.to_excel(f'result_{text}.xlsx')
        print('Successful generate xlsl-file')
    except Exception as e:
        print('Error in collect_into_table(): ', e)


def parse_search_yandex(text):
    html_sheet = get_html(text)
    info = get_data_items(html_sheet)
    collect_into_table(info, text)
