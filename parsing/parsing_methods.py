import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_html(text):
    cookies = {
        'yandexuid': '7530273891598883579',
        'yuidss': '7530273891598883579',
        'gdpr': '0',
        '_ym_uid': '1598883580843224296',
        'mda': '0',
        'font_loaded': 'YSv1',
        'my': 'YwA=',
        'is_gdpr': '0',
        'is_gdpr_b': 'CLuMORDVECgC',
        'tuid': 'a:2f42fc4fd46278de9fc0848e1918d200cf28e0869387461ca684efbaba57598a',
        'amcuid': '1618030131628604256',
        'ys_fp': 'form6026-logId%3D67d19df05dd961cce889d6cb6a7ff02f80308db0ba5exWEBx5946x1637162339x0',
        'ymex': '1945925953.yrts.1630565953#1970992407.yrtsi.1655632407',
        'L': 'BzlWYFJ7X19+QQVkXHt6UwlfD0pTe3UGFRMYKxMXBz85dHwhCScLKyBcFAgV.1656084197.15018.382373.86f5d884d9ea4443908f21a14a2ba349',
        'yandex_login': 'yarivanov77@gmail.com',
        'i': 'tdL1wUK4f98ZBftrhhJoEfaLARKty3pzuqJWU1BCkIcldDbCEyxSgPr+U9CTB6qVww4mh0f8998QggyOIN5RLnOFMeQ=',
        'yandex_gid': '213',
        'Session_id': '3:1656527727.5.0.1656084197316:Skywsg:44.1.2:1|1651632255.-1.0.1:319617191|3:254551.224571.aw3LMuaChQbSiquQCG89ox74yKQ',
        'sessionid2': '3:1656527727.5.0.1656084197316:Skywsg:44.1.2:1.499:1|1651632255.-1.0.1:319617191|3:254551.422435.3P05jhfPKj0vcQahga6kH2QZ6m0',
        '_ym_isad': '2',
        '_ym_d': '1656533343',
        'spravka': 'dD0xNjU2NTMzODgxO2k9MTc4LjE3Ni43Ni4xNzI7RD00RDhBMzUyQkI0OERENDgyNDY1NjlENzlCRTkwNUU4OERFODBERUI3OUVDNkJDMEIxN0RDMzIxMkQ0MUUxREMyQjJCOTQzN0U7dT0xNjU2NTMzODgxODM1MDMyMzAzO2g9N2U4ODQxODM4ZTQ5MWMxMDY3YmEwNmI4NGE1YWY3MzI=',
        'cycada': 'Aa9cpZjTCpzx4GorPE3Jg5zaqC2VQBluOombfnkPuQA=',
        'yabs-frequency': '/5/2m0101FEl6867PrX/UGYZJh-eO4jCHoEp9WFbw9hQJan78_ik1i96S1XLI4SZI4harDzWfM18HoFkZ9N-eSoLP4X7Ouy3GiZx8Lf2I4SZgvmCBnRG5Kf8HqErb5iyMt5ZN4X78oBjJmGCfCPkI4SZvlnCtaT9lr9CHo1VqRATgLHmMan780TU-7bLgZvSJ4SW_Ui5otWDI4DCHs22y9ldsnYvJan782nLk8sjvd1VJ4SW1ON2asM_JrTCHs26P1axLu_qPqr7007iOFQfs3uJUan7O1HMi72L0000J4T097gmS9K0001CHq2nTh1mbG0004r7O07kTx1mbG0004n787fAi72L0000J4V0lbcmS9K0001CHo00/',
        'yp': '1672301345.szm.1:1920x1080:620x939#1971444197.udn.cDp5YXJpdmFub3Y3N0BnbWFpbC5jb20%3D#1659119723.ygu.1#1688075091.p_sw.1656539090#1657132534.mcv.0#1657132534.mcl.t07rtz#1659211758.csc.1',
        '_yasc': 'z98hFhbbO0Wt4qeOFYqSO4luXooIFPxjsGd0O8lLE89xEQYG5Dh0A+zmf/HHnL+D',
        'ys': 'udn.cDp5YXJpdmFub3Y3N0BnbWFpbC5jb20%3D#c_chck.2637336584#wprid.1656535054259356-8468174080337452912-sas3-0979-e6b-sas-l7-balancer-8080-BAL-8066',
    }

    headers = {
        'authority': 'yandex.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'yandexuid=7530273891598883579; yuidss=7530273891598883579; gdpr=0; _ym_uid=1598883580843224296; mda=0; font_loaded=YSv1; my=YwA=; is_gdpr=0; is_gdpr_b=CLuMORDVECgC; tuid=a:2f42fc4fd46278de9fc0848e1918d200cf28e0869387461ca684efbaba57598a; amcuid=1618030131628604256; ys_fp=form6026-logId%3D67d19df05dd961cce889d6cb6a7ff02f80308db0ba5exWEBx5946x1637162339x0; ymex=1945925953.yrts.1630565953#1970992407.yrtsi.1655632407; L=BzlWYFJ7X19+QQVkXHt6UwlfD0pTe3UGFRMYKxMXBz85dHwhCScLKyBcFAgV.1656084197.15018.382373.86f5d884d9ea4443908f21a14a2ba349; yandex_login=yarivanov77@gmail.com; i=tdL1wUK4f98ZBftrhhJoEfaLARKty3pzuqJWU1BCkIcldDbCEyxSgPr+U9CTB6qVww4mh0f8998QggyOIN5RLnOFMeQ=; yandex_gid=213; Session_id=3:1656527727.5.0.1656084197316:Skywsg:44.1.2:1|1651632255.-1.0.1:319617191|3:254551.224571.aw3LMuaChQbSiquQCG89ox74yKQ; sessionid2=3:1656527727.5.0.1656084197316:Skywsg:44.1.2:1.499:1|1651632255.-1.0.1:319617191|3:254551.422435.3P05jhfPKj0vcQahga6kH2QZ6m0; _ym_isad=2; _ym_d=1656533343; spravka=dD0xNjU2NTMzODgxO2k9MTc4LjE3Ni43Ni4xNzI7RD00RDhBMzUyQkI0OERENDgyNDY1NjlENzlCRTkwNUU4OERFODBERUI3OUVDNkJDMEIxN0RDMzIxMkQ0MUUxREMyQjJCOTQzN0U7dT0xNjU2NTMzODgxODM1MDMyMzAzO2g9N2U4ODQxODM4ZTQ5MWMxMDY3YmEwNmI4NGE1YWY3MzI=; cycada=Aa9cpZjTCpzx4GorPE3Jg5zaqC2VQBluOombfnkPuQA=; yabs-frequency=/5/2m0101FEl6867PrX/UGYZJh-eO4jCHoEp9WFbw9hQJan78_ik1i96S1XLI4SZI4harDzWfM18HoFkZ9N-eSoLP4X7Ouy3GiZx8Lf2I4SZgvmCBnRG5Kf8HqErb5iyMt5ZN4X78oBjJmGCfCPkI4SZvlnCtaT9lr9CHo1VqRATgLHmMan780TU-7bLgZvSJ4SW_Ui5otWDI4DCHs22y9ldsnYvJan782nLk8sjvd1VJ4SW1ON2asM_JrTCHs26P1axLu_qPqr7007iOFQfs3uJUan7O1HMi72L0000J4T097gmS9K0001CHq2nTh1mbG0004r7O07kTx1mbG0004n787fAi72L0000J4V0lbcmS9K0001CHo00/; yp=1672301345.szm.1:1920x1080:620x939#1971444197.udn.cDp5YXJpdmFub3Y3N0BnbWFpbC5jb20%3D#1659119723.ygu.1#1688075091.p_sw.1656539090#1657132534.mcv.0#1657132534.mcl.t07rtz#1659211758.csc.1; _yasc=z98hFhbbO0Wt4qeOFYqSO4luXooIFPxjsGd0O8lLE89xEQYG5Dh0A+zmf/HHnL+D; ys=udn.cDp5YXJpdmFub3Y3N0BnbWFpbC5jb20%3D#c_chck.2637336584#wprid.1656535054259356-8468174080337452912-sas3-0979-e6b-sas-l7-balancer-8080-BAL-8066',
        'device-memory': '8',
        'downlink': '3.2',
        'dpr': '1',
        'ect': '4g',
        'referer': 'https://yandex.ru/',
        'rtt': '150',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Opera GX";v="87"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.58',
        'viewport-width': '1920',
    }

    params = {'text': text, 'lr': '213', 'clid': '9582', 'suggest_reqid': '753027389159888357950561896282144'}

    try:
        response = requests.get('https://yandex.ru/search/', params=params, cookies=cookies, headers=headers)
        return response.text
    except:
        print('Problems with request, be careful captcha')


def get_data_items(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        lis = soup.findAll('li', {'class': 'serp-item serp-item_card'})[:10]
        links = []
        headers = []
        descriptions = []
        index = [x for x in range(1, len(lis) + 1)]
        for li in lis:
            links.append(
                li.find('a', {'class': 'Link Link_theme_normal OrganicTitle-Link organic__url link'}).get('href'))
            headers.append(li.find('span', {'class': 'OrganicTitleContentSpan organic__title'}).text)
            descriptions.append(li.find('span', {'class': 'OrganicTextContentSpan'}).text)

        return [index, headers, links, descriptions]
    except:
        print("No standard elements in request")


def collect_into_table(list_data, text):
    try:
        data = {'?????????? ?? ????????????': list_data[0],
                '??????????????????': list_data[1],
                '????????????????': list_data[3],
                '????????????': list_data[2]}


        df_data = pd.DataFrame(data)
        df_data.to_excel(f'result_{text}.xlsx')
    except:
        print('Problems with generate xlsl-file')


def parse_search_yandex(text):
    try:
        html_sheet = get_html(text)
        info_from_html = get_data_items(html_sheet)
        collect_into_table(info_from_html, text)
    except:
        print('Nothing was found for your query')
