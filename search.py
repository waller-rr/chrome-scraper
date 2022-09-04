import json
import requests


def get_search(term):
    cookies = {
        'NID': '511=nPp9gxiMjrFOb240qHnDaaap_FjYiUjiWXzH6ciWU-NWogstzrUJ4NJ4P4DidEYH31-rawYEuY6cn9Irp_Q4XXhrS_Be7PVT5p-0ydepDnubXKUFLKJmelePLxUxx7LOJg_L_62dZm9fR3Tzl7VZRhKuxuNdR9H9Q4wOldIZzXs',
        '__utma': '73091649.1251424543.1662302279.1662302279.1662302279.1',
        '__utmc': '73091649',
        '__utmz': '73091649.1662302279.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '__utmt': '1',
        '__utmb': '73091649.12.6.1662302285939',
    }

    headers = {
        'authority': 'chrome.google.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'NID=511=nPp9gxiMjrFOb240qHnDaaap_FjYiUjiWXzH6ciWU-NWogstzrUJ4NJ4P4DidEYH31-rawYEuY6cn9Irp_Q4XXhrS_Be7PVT5p-0ydepDnubXKUFLKJmelePLxUxx7LOJg_L_62dZm9fR3Tzl7VZRhKuxuNdR9H9Q4wOldIZzXs; __utma=73091649.1251424543.1662302279.1662302279.1662302279.1; __utmc=73091649; __utmz=73091649.1662302279.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=73091649.12.6.1662302285939',
        'origin': 'https://chrome.google.com',
        'referer': 'https://chrome.google.com/',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-same-domain': '1',
    }

    params = {
        'authuser': '0',
        'hl': 'zh-CN',
        'gl': 'HK',
        'pv': '20210820',
        'mce': 'atf,pii,rtr,rlb,gtc,hcn,svp,wtd,hap,nma,dpb,utb,hbh,ebo,hqb,ifm,ndd,ntd,oiu,c3d,ncr,hns,ctm,ac,hot,hfi,dtp,mac,bga,fcf,hsp,rma',
        'count': '112',
        'searchTerm': term,
        'sortBy': '0',
        'container': 'CHROME',
        '_reqid': '181487',
        'rt': 'j',
    }

    data = 'login=&'

    response = requests.post('https://chrome.google.com/webstore/ajax/item', params=params, cookies=cookies,
                             headers=headers, data=data)
    response_json = response.text[4:].strip()
    return json.loads(response_json)


def get_search_detail(data):
    search_data = data[0][1][1]
    result = []
    for item in search_data:
        result.append({
            "id": item[0],
            "name": item[1],
            "icon": item[3],
            "url": item[37],
            "summary": item[6],
            "category": item[9],
            "category_name": item[10],
            "score": item[12],
            "ratings": item[22],
            "users": item[23],
            "developer_name": item[2],
            "developer_website": item[81],
            # "featured": item[89],
        })
    return result


def search(term='SEO'):
    data = get_search(term)
    return get_search_detail(data)
