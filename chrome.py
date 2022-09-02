import datetime
import json
import ramda as R
import requests
from typing import Callable, List, Any, Optional
from utils.common import formatter_screenshots, formatter_users, formatter_date, formatter_free, formatter_related, formatter_manifest


class MappingsSpec:
    def __init__(
            self,
            mapping: List[int],
            function: Callable = None,
            default_value: Any = None,
    ):
        self.map = mapping
        self.function = function
        self.default_value = default_value

    def extract_content(self, source_data):
        try:
            result = R.path(self.map, source_data)
            if self.function is not None:
                result = self.function(result)
        except:
            result = self.default_value
        return result


class Mappings:
    Detail = {
        "chrome_id": MappingsSpec([0, 1, 1, 0, 0]),
        "name": MappingsSpec([0, 1, 1, 0, 1]),
        "icon": MappingsSpec([0, 1, 1, 0, 3]),
        "summary": MappingsSpec([0, 1, 1, 0, 6]),
        "description": MappingsSpec([0, 1, 1, 1]),
        "category": MappingsSpec([0, 1, 1, 0, 9]),
        "category_name": MappingsSpec([0, 1, 1, 0, 10]),
        "score": MappingsSpec([0, 1, 1, 0, 12]),
        "ratings": MappingsSpec([0, 1, 1, 0, 22]),
        "size": MappingsSpec([0, 1, 1, 25]),
        "users": MappingsSpec([0, 1, 1, 4], formatter_users),
        "users_text": MappingsSpec([0, 1, 1, 4]),
        "version": MappingsSpec([0, 1, 1, 6]),
        "updated_date": MappingsSpec([0, 1, 1, 7], formatter_date),
        "languages": MappingsSpec([0, 1, 1, 8]),
        "free": MappingsSpec([0, 1, 1, 9, 3], formatter_free),
        "free_text": MappingsSpec([0, 1, 1, 9, 3]),
        "manifest": MappingsSpec([0, 1, 1, 9, 0], formatter_manifest),
        "chrome_type": MappingsSpec([0, 1, 1, 10]),
        "featured": MappingsSpec([0, 1, 1, 0, 89]),
        "url": MappingsSpec([0, 1, 1, 0, 37]),

        "small_promo_tile": MappingsSpec([0, 1, 1, 0, 4]),
        "large_promo_tile": MappingsSpec([0, 1, 1, 0, 5]),
        "marquee_promo_tile": MappingsSpec([0, 1, 1, 0, 17]),
        "screenshots": MappingsSpec([0, 1, 1, 11], formatter_screenshots),

        # "unknown01": MappingsSpec([0, 1, 1, 24]),

        "developer_name": MappingsSpec([0, 1, 1, 0, 2]),
        "developer_email": MappingsSpec([0, 1, 1, 35, 0]),
        "developer_website": MappingsSpec([0, 1, 1, 0, 35]),
        "developer_address": MappingsSpec([0, 1, 1, 35, 1]),
        "developer_privacy_policy": MappingsSpec([0, 1, 1, 35, 2]),
        "developer_trader": MappingsSpec([0, 1, 1, 35, 3]),
        "homepage_url": MappingsSpec([0, 1, 1, 3]),
        "support_url": MappingsSpec([0, 1, 1, 5]),

        "google_analytics_id": MappingsSpec([0, 1, 1, 0, 48]),

        "related": MappingsSpec([0, 1, 2], formatter_related),

    }


def chrome(chrome_id, lang="en", country="us"):
    chrome_data = get_chrome(chrome_id, lang, country)
    return get_chrome_detail(chrome_data)


def get_chrome_detail(chrome_data):
    result = {}
    detail_mappings = Mappings.Detail.items()
    for key, item in detail_mappings:
        result[key] = item.extract_content(chrome_data)
    return result


def get_chrome(chrome_id, lang, country):
    cookies = {
        '1P_JAR': '2022-08-11-08',
        'AEC': 'AakniGNLgwwXBPHv6TUXNq3OvDzF2aFg6gbGaLqM02RJecMhQCpEjQ2laA',
        'NID': '511=HZEv0eDIIg6o6TXxRrtJhf1On7LuliilEnKqWituNux396AKW02-H1h9hL_OC5l8xp18mnkla9ukbCOu6I6G7g3q69Nzs1dFvxUKEI8otVLjtkp7g5Kd6gDjH5n3kMI8zowGC1gw6A2JemFaR7CYeO7BhaW06NJoYIBjy9K52WA',
        'GOOGLE_ABUSE_EXEMPTION': 'ID=3dca7f0c04e34bf2:TM=1660206264:C=r:IP=84.17.56.76-:S=Zg9qFaA4CQFgUzzHQ4oILiY',
        '__utma': '73091649.1810321544.1660206270.1660206270.1660206270.1',
        '__utmb': '73091649.26.3.1660206286063',
        '__utmc': '73091649',
        '__utmz': '73091649.1660206270.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
        '__utmt': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://chrome.google.com/',
        'X-Same-Domain': '1',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        'Origin': 'https://chrome.google.com',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '1P_JAR=2022-08-11-08; AEC=AakniGNLgwwXBPHv6TUXNq3OvDzF2aFg6gbGaLqM02RJecMhQCpEjQ2laA; NID=511=HZEv0eDIIg6o6TXxRrtJhf1On7LuliilEnKqWituNux396AKW02-H1h9hL_OC5l8xp18mnkla9ukbCOu6I6G7g3q69Nzs1dFvxUKEI8otVLjtkp7g5Kd6gDjH5n3kMI8zowGC1gw6A2JemFaR7CYeO7BhaW06NJoYIBjy9K52WA; GOOGLE_ABUSE_EXEMPTION=ID=3dca7f0c04e34bf2:TM=1660206264:C=r:IP=84.17.56.76-:S=Zg9qFaA4CQFgUzzHQ4oILiY; __utma=73091649.1810321544.1660206270.1660206270.1660206270.1; __utmb=73091649.26.3.1660206286063; __utmc=73091649; __utmz=73091649.1660206270.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'hl': lang,
        'gl': country,
        'pv': '20210820',
        'mce': 'atf,pii,rtr,rlb,gtc,hcn,svp,wtd,hap,nma,dpb,utb,hbh,ebo,hqb,ifm,ndd,ntd,oiu,hns,ctm,ac,hot,hfi,dtp,mac,bga,bps,fcf,rai,rma',
        'id': chrome_id,
        'container': 'CHROME',
        '_reqid': '159087',
        'rt': 'j',
    }

    data = 'login=&'

    response = requests.post('https://chrome.google.com/webstore/ajax/detail', params=params, cookies=cookies,
                             headers=headers, data=data)
    response_json = response.text[4:].strip()
    return json.loads(response_json)

