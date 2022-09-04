# Chrome-Scraper

Chrome-Scraper provides APIs to easily crawl the Chrome Extension or Theme for Python *without any external dependencies!*

## Installation
```
pip install chrome-scraper
```

## Usage
The country and language codes that can be included in the `lang` and `country` parameters described below depend on the [ISO 3166](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) and [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) standards, respectively. Therefore, we recommend using an ISO database library such as [pycountry](https://github.com/flyingcircusio/pycountry).

### Chrome Detail
```python
from chrome_scraper import chrome

result = chrome(
    'doffdbedgdhbmffejikhlojkopaleian',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)
```

Result of `print(result)`:

```
{
    "chrome_id": "doffdbedgdhbmffejikhlojkopaleian", 
    "name": "Best ASO Tools for Google Play Store", 
    "icon": "https://lh3.googleusercontent.com/pb9X1O23oTEqJWv5r-d0YFxk8Bme6UnGWpHjXitTk8UBgU9bqDT7EwWOyVAvaWW4znMNjxcwvlfK-d9V0yFnHD8UmaI=w50-h50-e365-rj-sc0x00ffffff", 
    "summary": "Analyzing the hidden metrics of the Android app market for a complete App Store Optimization & ASO competitive research report.", 
    "description": "This FREE and BEST ASO tool (App Store Optimization) provides the missing metrics of app marketing and keyword analysis for the Android Google Play.
It has 3 major features:
- Exposure of ASO performance
- App keyword checker
- Country switcher for different reports

🌟1. Exposure of ASO performance🌟
We calculate the core metrics for evaluating app marketing performances (which are hidden by Google Play), including the exact number of app downloads and review changes over a month, the current version, and the publish date.
Valuable metrics such as the revenue, MAU, and all the trends alongside are also available on ASOTools.io (the website)!

🌟2. App keyword checker [Coming Soon]🌟
Not all keywords in use for an app are written within the \"description\" on the product page. We sort out the top 10 keywords for each app to show what's contributing most to an app's in-store search rank.
For each keyword, we attach the popularity, in-store search volume, difficulty, counts of related apps, and app's search rank as well.

🌟3. Country switcher for different reports [Coming Soon]🌟
ASO performance and keyword mapping of an App differentiate in different countries/regions.
You can easily switch from one country/region to another in the Play Store to gain customized reports.

For any question or suggestion, we are always here for listening! Try this extension out and make the App competition analysis easier than ever!

What are ASOTools alternatives:

● Toolbox for Google Play Store™ and SpidyHive - ASO G-Play Helper Tool. Both are collections of multiple data resources.
● ASO - Google Play Feature Graphic Viewer. It shows the Feature Graphic for the current Google Play mobile app or game, but is not applicable in the latest Google Play store.
● ASO - Toolbox by StoreMaven. This tool lets you preview any App Store or Google Play app online.
● AppstoreSpy for Play Store. It provides all data from AppstoreSpy and needs registration first.
● ASO & Search Ads Free Tool by AppTweak. Nice tool for keyword density analysis, not applicable in the latest Google Play store.
● Search Ads Keyword Popularity Checker. A good ASO keyword checker tool that needs a subscription before use.
● Play Store Downloader. A free APK Downloader for the Google Play application.

प्ले स्टोर अनुकूलन
एएसओ टूल
ऐप कीवर्ड रिसर्च
खोजशब्द अनुसंधान", 
    "category": "ext/7-productivity", 
    "category_name": "Productivity", 
    "score": 5, 
    "ratings": 63, 
    "size": "110KiB", 
    "users": 631, 
    "users_text": "631", 
    "version": "1.2.0", 
    "updated_date": "2022-08-31", 
    "languages": [
        "Bahasa Indonesia", 
        "Bahasa Melayu", 
        "Deutsch", 
        "English", 
        "Filipino", 
        "Français", 
        "Nederlands", 
        "Norsk", 
        "Tiếng Việt", 
        "Türkçe", 
        "català", 
        "dansk", 
        "eesti", 
        "español", 
        "hrvatski", 
        "italiano", 
        "latviešu", 
        "lietuvių", 
        "magyar", 
        "polski", 
        "română", 
        "slovenský", 
        "slovenščina", 
        "suomi", 
        "svenska", 
        "čeština", 
        "Ελληνικά", 
        "Српски", 
        "български", 
        "русский", 
        "українська", 
        "עברית", 
        "فارسی‎", 
        "मराठी", 
        "हिन्दी", 
        "বাংলা", 
        "ગુજરાતી", 
        "தமிழ்", 
        "తెలుగు", 
        "മലയാളം", 
        "ไทย", 
        "‫العربية", 
        "中文 (简体)", 
        "中文 (繁體)", 
        "日本語", 
        "한국어"
    ], 
    "free": 1, 
    "free_text": "FREE", 
    "manifest": {
        "update_url": "https://clients2.google.com/service/update2/crx", 
        "name": "__MSG_appName__", 
        "description": "__MSG_appDesc__", 
        "default_locale": "en", 
        "short_name": "ASOTools", 
        "version": "1.2.0", 
        "manifest_version": 3, 
        "icons": {
            "16": "assets/images/icon.png", 
            "48": "assets/images/icon.png", 
            "128": "assets/images/icon.png"
        }, 
        "background": {
            "service_worker": "background.js", 
            "type": "module"
        }, 
        "action": {
            "default_title": "__MSG_appDesc__", 
            "default_icon": {
                "16": "assets/images/icon.png"
            }, 
            "default_popup": "popup.html"
        }, 
        "web_accessible_resources": [
            {
                "resources": [
                    "/assets/images/asotools.png", 
                    "/manifest.json"
                ], 
                "matches": [
                    "<all_urls>"
                ]
            }
        ], 
        "host_permissions": [
            "*://*.asotools.io/*"
        ], 
        "optional_host_permissions": [
            "*://*/*"
        ], 
        "content_scripts": [
            {
                "js": [
                    "/assets/js/jquery.min.js", 
                    "/assets/js/ramda.min.js", 
                    "content-script.js"
                ], 
                "matches": [
                    "https://play.google.com/store/apps/details*"
                ], 
                "run_at": "document_end"
            }
        ]
    }, 
    "chrome_type": "Extension", 
    "featured": 0, 
    "url": "https://chrome.google.com/webstore/detail/best-aso-tools-for-google/doffdbedgdhbmffejikhlojkopaleian?hl=en&gl=US", 
    "small_promo_tile": "https://lh3.googleusercontent.com/wQRPkvu46Xc7tXXgWQfJmIXxJJTTEIU-H9DUqJ6aCMdFbbtJmybIPvPubFPVDGuS-E2Qd0sIs78Eg5tRvfiJo0Lx-A=w220-h140-e365-rj-sc0x00ffffff", 
    "large_promo_tile": "https://lh3.googleusercontent.com/k2zxlglJDymgeFZLtSpuMrJ9gbpB53f-YcCdip4DxlTS93F39QLBeN0PYP3xyqmfsMiT6QAZRHBXP84j8n1g2vnR=w460-h340-e365-rj-sc0x00ffffff", 
    "marquee_promo_tile": "https://lh3.googleusercontent.com/BLEO21y20KgXFw-Z5nTVeW_1UwonEOqASlC6T6Z2M7uBj7VxdeP60jiGcdvCS7mu7CDnIbww8PANxHXlss_ADFpH=w700-h280-e365-rj-sc0x00ffffff", 
    "screenshots": [
        "https://lh3.googleusercontent.com/FI7ViaIcz8XTQwfsVa10VL_59K97iODifUD7hYAzpPs3qNU6wTpaEiXhNbnkxDKECNXNL5NGQ9gLoOxFJ-8NuMaS974=w640-h400-e365-rj-sc0x00ffffff", 
        "https://lh3.googleusercontent.com/MvdiZiAsJ9dmIx3-WnUVmnUOV_gun_l4tJi4rOm6bAbX3wNxKKOjeYPEQ3fuiI13MwF7DiXiruaHFcIbcUi0Od1PXw=w640-h400-e365-rj-sc0x00ffffff", 
        "https://lh3.googleusercontent.com/2MdwmG2i5D4yQlnfGCOgsHr9aEEfR22ak7AUYC4Ac4t4-pxm0WK3hvydzaRRzDQV9sgOgNPyAaB0BvpaIgoCAcXQtw=w640-h400-e365-rj-sc0x00ffffff", 
        "https://lh3.googleusercontent.com/uRfeqY-U5-vYKMbszkzERVbS9Hs3xIBKPUyo_xtbMdaRdSi3jmxzwj7r3Hyl1x_dvhm0KKB6kRKH49LbdHi0ib_7qQ=w640-h400-e365-rj-sc0x00ffffff"
    ], 
    "developer_name": "icaohongyuan", 
    "developer_email": "icaohongyuan@gmail.com", 
    "developer_website": "asotools.io", 
    "developer_address": null, 
    "developer_privacy_policy": "https://asotools.io/en/privacy", 
    "developer_trader": 0, 
    "homepage_url": "https://asotools.io/", 
    "support_url": "https://asotools.io/apps", 
    "google_analytics_id": "YT-140648082-54"
}
```

Example with `related` option:

```python
from chrome_scraper import chrome

result = chrome(
    'doffdbedgdhbmffejikhlojkopaleian',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us',
    related=True
)
```
Result of `print(result)`:

```
{
    "chrome_id": "doffdbedgdhbmffejikhlojkopaleian", 
    "name": "Best ASO Tools for Google Play Store", 
    
    ...
    
    "related": [
        {
          "id": "ofjlibelpafmdhigfgggickpejfomamk",
          "name": "Discordmate - Discord Chat Exporter",
          "icon": "https://lh3.googleusercontent.com/ORJL8gNWcFAK6EoTXZuIzIj0FX5_Vwe9WEYNg6o3Hz20ho5JpgWeHBfpEcP0kjD9ItJnYlGmvyo_YseeoE951Hj-gA=w50-h50-e365-rj-sc0x00ffffff",
          "url": "https://chrome.google.com/webstore/detail/discordmate-discord-chat/ofjlibelpafmdhigfgggickpejfomamk?hl=en&gl=US",
          "summary": "The extension that can provide Discord chat log export, batch export of video, images and such attachments in Discord chat history.",
          "category": "ext/7-productivity",
          "category_name": "Productivity",
          "score": 4.884615384615385,
          "ratings": 78,
          "users": "1,000+",
          "developer_name": "abel.sonmerfield",
          "developer_website": null,
          "featured": 0
        },
        {
          "id": "pcbmgmpmajnemcackfikoibnebfmlbab",
          "name": "LinkedRadar Notifier For LinkedIn™",
          "icon": "https://lh3.googleusercontent.com/NEVISWNNakKSdHGOMFgGVh29eSAT_lL4ILDK1rdxfHgyP6Ck_RwYtg7qdZkefe2bzuGDpRG1W71ZX-RxYbSs3FjfQA=w50-h50-e365-rj-sc0x00ffffff",
          "url": "https://chrome.google.com/webstore/detail/linkedradar-notifier-for/pcbmgmpmajnemcackfikoibnebfmlbab?hl=en&gl=US",
          "summary": "Convenient to get the real-time activity from linkedin.com, including Network, Messages and Notifications.",
          "category": "ext/1-communication",
          "category_name": "Social & Communication",
          "score": 4.983333333333333,
          "ratings": 60,
          "users": "169",
          "developer_name": "LinkedRadar",
          "developer_website": "https://linkedradar.com",
          "featured": 0
        },
        ...
    ]
}
```

### Chrome Reviews
`reviews` function returns `result` with `continuation token`.

- `result` : Crawling result of reviews. (list)
- `continuation_token` : Data containing how many items were loaded, what arguments used in the current result. If you pass this value to the `continuation_token` parameter of the `reviews` function, the next items are crawled. For example, if 1000 reviews are retrieved and the returned token 'eXamplE' is passed to the reviews function, the list of reviews is retrieved from 1000 or later items.

> :bulb: Setting `count` too high can cause problems. Because the maximum number of reviews per page supported by Google Play is 200, it is designed to pagination and recrawl by 200 until the number of results reaches count.

```python
from chrome_scraper import Sort, reviews

result, continuation_token = reviews(
    'com.fantome.penguinisle',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.NEWEST
    count=3, # defaults to 100
    filter_score_with=5 # defaults to None(means all score)
)

# If you pass `continuation_token` as an argument to the reviews function at this point,
# it will crawl the items after 3 review items.

result, _ = reviews(
    'com.fantome.penguinisle',
    continuation_token=continuation_token # defaults to None(load from the beginning)
)
```

Result of `print(result)`:

```
[
  {
    "uid": "0000002bce726e45",
    "name": "Lina Lee",
    "icon": "//lh3.googleusercontent.com/a-/AFdZucpygN2Z6WHx3j7bU7mwmb7ddXHXitKFDGCfGM4z=s40-c-k",
    "score": 5,
    "comment": "Great tool! would save your time in ASO.",
    "created_at": 1660629780540,
    "reply": []
  },
  {
    "uid": "0000004f4cd876fb",
    "name": "Vincent Lee",
    "icon": "//lh3.googleusercontent.com/a-/AFdZucrQC6sQQ8xixNcMXZXyYr5GOqpPAqHZliNjxRdX=s40-c-k",
    "score": 5,
    "comment": "very useful， nice tool， i like it",
    "created_at": 1660629373721,
    "reply": []
  },
  {
    "uid": "000000dada9abfaa",
    "name": "gogo sun",
    "icon": "//lh3.googleusercontent.com/a/default-user=s40-c-k",
    "score": 5,
    "comment": "It's very useful",
    "created_at": 1660629219523,
    "reply": []
  },
  ...
]
```

### Chrome Suggest
```python
from chrome_scraper import suggest

result = suggest('ASO')
```
Result of `print(result)`:
```
[
  "aso",
  "aso tools",
  "asos",
  "asos helper",
  "asos helper tools",
  "asodigger",
  "asociados",
  "asocial",
  "& asociados",
  "asos price"
]
```

### Chrome Search
```python
from google_play_scraper import search

result = search("SEO")
```

Result of `print(result)`:

```
[
  {
    "id": "bjogjfinolnhfhkbipphpdlldadpnmhc",
    "name": "SEO META in 1 CLICK",
    "icon": "https://lh3.googleusercontent.com/SB10T57nhIIwhu6og6aElpCgrk34Nq9zXh5zoGxpOFL9GNlICuJO8ngNXiTL0Y-crDmIoflJnsrqse13db8NMFwB6Tw=w50-h50-e365-rj-sc0x00ffffff",
    "url": "https://chrome.google.com/webstore/detail/seo-meta-in-1-click/bjogjfinolnhfhkbipphpdlldadpnmhc?hl=zh-CN&gl=HK&authuser=0",
    "summary": "Displays all meta data and main SEO information for the best SEO",
    "category": "ext/11-web-development",
    "category_name": "开发者工具",
    "score": 4.8567931456548346,
    "ratings": 817,
    "users": "300,000+",
    "developer_name": "Bilal Hadri",
    "developer_website": "http://www.seo-extension.com"
  },
  {
    "id": "giihipjfimkajhlcilipnjeohabimjhi",
    "name": "SEO Minion",
    "icon": "https://lh3.googleusercontent.com/VbaaufylDUi4QOiUNZC3x1SDcWgSjPo123d5EzXTnCtPVE0B1kFLjSnD69HpgdtGy5MvnzRpQHSBFdvqq_3oHievmQ=w50-h50-e365-rj-sc0x00ffffff",
    "url": "https://chrome.google.com/webstore/detail/seo-minion/giihipjfimkajhlcilipnjeohabimjhi?hl=zh-CN&gl=HK&authuser=0",
    "summary": "SEO Minion helps you in your daily SEO tasks such as On-Page SEO analysis, Broken Link Checking, SERP Preview and more",
    "category": "ext/38-search-tools",
    "category_name": "搜索工具",
    "score": 4.8696461824953445,
    "ratings": 537,
    "users": "200,000+",
    "developer_name": "Akash",
    "developer_website": "https://seominion.com"
  },
  ...
]
```

## Changes
Change logs are here : [CHANGELOG.md](CHANGELOG.md)