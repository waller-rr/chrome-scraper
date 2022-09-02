import json
import requests
import ramda
from typing import Callable, List, Any, Optional


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
            result = ramda.path(self.map, source_data)
            if self.function is not None:
                result = self.function(result)
        except:
            result = self.default_value
        return result


class Mappings:
    Detail = {
        "uid": MappingsSpec([2, 0]),
        "name": MappingsSpec([2, 1]),
        "icon": MappingsSpec([2, 2]),
        "score": MappingsSpec([3]),
        "comment": MappingsSpec([4]),
        "created_at": MappingsSpec([6]),
        "reply": MappingsSpec([9, 4]),
    }


def reviews(chrome_id, lang='en', country='us'):
    reviews_data = get_reviews(chrome_id, lang, country)
    return get_review_detail(reviews_data)


def get_review_detail(data):
    reviews_data = ramda.path([0, 1, 4], data)
    # reviews_count = ramda.path([0, 1, 6], data)
    reviews_result = []
    detail_mappings = Mappings.Detail.items()
    for review in reviews_data:
        result = {}
        for key, item in detail_mappings:
            result[key] = item.extract_content(review)
        reviews_result.append(result)
    return reviews_result


def get_reviews(chrome_id, lang, country):
    cookies = {
        'NID': '511=QttGNRUkIjtGW8dyXHEmesBfK_v_sShRYoxgfSWyC_ZcDAVPq4PeO_VnYwyf9KYXhkKoNrHxJQvCsOXM7cEOTFOw3fU-0d2jThZ-BcJVMGvaazo-xNuLCpI5rURTCG95K2pP6AGJypwaVvhLFPQdOlhnVtxt7IKQ15EC2LoYIhU',
        '__utma': '73091649.1224404978.1661525128.1661525128.1661525128.1',
        '__utmc': '73091649',
        '__utmz': '73091649.1661525128.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '__utmt': '1',
        '__utmb': '73091649.37.4.1661526041359',
    }

    headers = {
        'authority': 'chrome.google.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'NID=511=QttGNRUkIjtGW8dyXHEmesBfK_v_sShRYoxgfSWyC_ZcDAVPq4PeO_VnYwyf9KYXhkKoNrHxJQvCsOXM7cEOTFOw3fU-0d2jThZ-BcJVMGvaazo-xNuLCpI5rURTCG95K2pP6AGJypwaVvhLFPQdOlhnVtxt7IKQ15EC2LoYIhU; __utma=73091649.1224404978.1661525128.1661525128.1661525128.1; __utmc=73091649; __utmz=73091649.1661525128.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=73091649.37.4.1661526041359',
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
        'hl': lang,
        'gl': country,
        'pv': '20210820',
        'mce': 'atf,pii,rtr,rlb,gtc,hcn,svp,wtd,hap,nma,dpb,utb,hbh,ebo,hqb,ifm,ndd,ntd,oiu,c3d,ncr,hns,ctm,ac,hot,hfi,dtp,mac,bga,fcf,rai,rma,lrc,spt,irt,scm,ibg,der,bgi,rer,bem,dda,rae,shr,esl,dha,hib,dsq',
        '_reqid': '1182840',
        'rt': 'j',
    }

    data = 'login=&f.req=%5B%22http%3A%2F%2Fchrome.google.com%2Fextensions%2Fpermalink%3Fid%3D{}%22%2C%22en%22%2C%5B25%5D%2C2%2C%5B2%5D%2Ctrue%5D&'.format(
        chrome_id)

    response = requests.post('https://chrome.google.com/webstore/reviews/get', params=params, cookies=cookies,
                             headers=headers, data=data)

    response_json = response.text[4:].strip()
    return json.loads(response_json)


def get_review_mappings(data):
    reviews_mappings = {
        "user_id": MappingsSpec([2, 0]),
        "name": MappingsSpec([2, 1]),
        "icon": MappingsSpec([2, 2]),
        "score": MappingsSpec([3]),
        "comment": MappingsSpec([4]),
        "created_at": MappingsSpec([6]),
        "reply": MappingsSpec([9, 4]),
    }
    result = {}
    mappings = reviews_mappings.items()
    for key, item in mappings:
        result[key] = item.extract_content(data)
    return result
