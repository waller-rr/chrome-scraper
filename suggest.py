import json
import requests


def get_suggests(term):
    cookies = {
        'NID': '511=DOGiRzWRpX_Gaf-lvvYq2yM6jqh0N2fBo5QYznDzyHS4dRKO9PUls7P_hsFkcHBzIMBxACSaJ_Psun3BPxJrAtIdlA_pqOAK0VCruCyS3pX9-W9WRMPLogEZa9877tpPKk3iNPqqQJrCw55PXOwlC2Q_K6yMYpUZHHV5C3QTuf0',
        '__utma': '73091649.118271506.1662101850.1662101850.1662101850.1',
        '__utmc': '73091649',
        '__utmz': '73091649.1662101850.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '__utmt': '1',
        '__utmb': '73091649.19.0.1662101858250',
    }

    headers = {
        'authority': 'chrome.google.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'NID=511=DOGiRzWRpX_Gaf-lvvYq2yM6jqh0N2fBo5QYznDzyHS4dRKO9PUls7P_hsFkcHBzIMBxACSaJ_Psun3BPxJrAtIdlA_pqOAK0VCruCyS3pX9-W9WRMPLogEZa9877tpPKk3iNPqqQJrCw55PXOwlC2Q_K6yMYpUZHHV5C3QTuf0; __utma=73091649.118271506.1662101850.1662101850.1662101850.1; __utmc=73091649; __utmz=73091649.1662101850.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=73091649.19.0.1662101858250',
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
        'hl': 'zh-CN',
        'gl': 'HK',
        'pv': '20210820',
        'mce': 'atf,pii,rtr,rlb,gtc,hcn,svp,wtd,hap,nma,dpb,utb,hbh,ebo,hqb,ifm,ndd,ntd,oiu,c3d,ncr,hns,ctm,ac,hot,hfi,dtp,mac,bga,fcf,rai,rma,igb,ibg,pot,evt,hib,ess',
        'q': term,
        '_reqid': '1253854',
        'rt': 'j',
    }

    data = 'login=&'

    response = requests.post('https://chrome.google.com/webstore/search/autocomplete', params=params, cookies=cookies,
                             headers=headers, data=data)
    response_json = response.text[4:].strip()
    return json.loads(response_json)


def get_suggest_detail(data):
    return data[0][1][2]


def suggest(term='ASO'):
    suggest_data = get_suggests(term)
    return get_suggest_detail(suggest_data)
