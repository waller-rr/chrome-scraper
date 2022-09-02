# Chrome-Scraper

Chrome-Scraper provides APIs to easily crawl the Chrome Extension or Theme for Python *without any external dependencies!*

## Related Projects
### [chrome-scraper](https://github.com/waller-rr/chrome-scraper)

I have referred a lot to the API design of this library.

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

### App Reviews
`reviews` function returns `result` with `continuation token`.

- `result` : Crawling result of reviews. (list)
- `continuation_token` : Data containing how many items were loaded, what arguments used in the current result. If you pass this value to the `continuation_token` parameter of the `reviews` function, the next items are crawled. For example, if 1000 reviews are retrieved and the returned token 'eXamplE' is passed to the reviews function, the list of reviews is retrieved from 1000 or later items.

> :bulb: Setting `count` too high can cause problems. Because the maximum number of reviews per page supported by Google Play is 200, it is designed to pagination and recrawl by 200 until the number of results reaches count.

```python
from google_play_scraper import Sort, reviews

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
        "userName": "Alyssa Williams",
        "userImage": "https://lh3.googleusercontent.com/-cVEHKr7mzv8/AAAAAAAAAAI/AAAAAAAAAAA/AKF05nB2r3GUkji31m0tC4ylFNiVMpmNWA/photo.jpg",
        "content": "This is literally the best idle game I have ever played. The penguins waddle around and live their best lives in the cutest little outfits. I just unlocked the little penguins and I have been sobbing uncontrollably for ten minutes because they are so adorable. There are only two suggestions I have for this game: more of the penguin info ads. I love them. I have learned so much about all the teeny fellas. Secondly, I would like to be able to name my 'guins so I can tell them apart.",
        "score": 5,
        "thumbsUpCount": 54,
        "reviewCreatedVersion": "1.16",
        "at": datetime.datetime(2020, 2, 24, 17, 19, 34),
        "replyContent": "Hello, We will gradually improve the various systems in the game to enhance the player's game experience. We have recorded your suggestions and feedback to the planner. If you have any other suggestions and ideas, please feel free to contact us at penguinisle@habby.com.Thank you for playing!",
        "repliedAt": datetime.datetime(2020, 2, 24, 18, 30, 42),
        "reviewId": "gp:AOqpTOE0Iy5S9Je1F8W1BgCl6l_TCFP_QN4qGtRATX3PeB5VV9aZu6UHfMWdYFF1at4qZ59xxLNHFqYLql5SL-k"
    },
    {
        "userName": "EasyJet 123",
        "userImage": "https://lh3.googleusercontent.com/a-/AOh14GhE3-Fsq5KDs_kmCRGcifbNUQTOtK5DpZkJ2AiqyQ",
        "content": "Easily my favorite game. Relaxing, with easy controls, no purchase necessary to advance... I love it. 100% recommend. I love how you can get gems continually by completing missions, and the low price of boosts are great. But how about adding new buildings like an airport, an army base, and a train station? Would be great to see these. And the building purchase price might be lowered so it's a bit easier to progress after the Igloo. Maybe...",
        "score": 5,
        "thumbsUpCount": 79,
        "reviewCreatedVersion": "1.14",
        "at": datetime.datetime(2020, 2, 12, 8, 42, 41),
        "replyContent": None,
        "repliedAt": None,
        "reviewId": "gp:AOqpTOHyQo9QEPtxefmvjNuqR9VmFyBaj2FNXLvHsuH19de9bC0dT_voHWSKNGFcc10jv077wOdzBrkgLKX6pUc"
    },
    {
        "userName": "Lillemann",
        "userImage": "https://lh3.googleusercontent.com/a-/AOh14GjiVSIrx033k9HZ9Tu4BQ1iYZST0IRW8UlDCX3gdw",
        "content": "Really good looking. And it runs super super smooth. I love the camera options when clicking the camera button. And the penguins looks absolutely awesome and I really love the limited eddition ones. That sometimes the ads are replaced with penguin facts is just awesome. I suggest that you set up some kind of leaderboard it could probobly show the players that are earning the most money per sec or something. But overall this game is a strong 10/10",
        "score": 5,
        "thumbsUpCount": 2,
        "reviewCreatedVersion": "1.14",
        "at": datetime.datetime(2020, 2, 11, 18, 8, 11),
        "replyContent": "Thank you very much for your review concerning our game. We will try our best to do better,If you have any other feedback or suggestions, feel free to contact us at penguinisle@habby.com. Have a nice day!",
        "repliedAt": datetime.datetime(2020, 2, 11, 18, 53, 38),
        "reviewId": "gp:AOqpTOEGUPB6HA0DIPNp3K2yAHRK-GN96dVJ-zkhPgKpclevgt8q9nR6Pv4N_F4TIPCpMeaoTutNGOZ2CSs65Ws"
    },
]
```

### App All Reviews
`reviews_all` function returns all of reviews from app. If you want to set the count to infinity while using the `reviews` function, you can use the `reviews_all` function.

> :bulb: Because of the Google Play Store limit (up to 200 reviews can be fetched at a time), http requests are generated as long as the number of app reviews is divided by 200. For example, targeting an app like Pokémon GO makes tens of thousands of http requests.

```python
from google_play_scraper import Sort, reviews_all

result = reviews_all(
    'com.fantome.penguinisle',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=5 # defaults to None(means all score)
)
```


### App Permissions
`permissions` function returns permissions of app.

```python
from google_play_scraper import permissions

result = permissions(
    'com.spotify.music',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
)
```

Result of `print(result)`:

```
{
    "Microphone": [
        "record audio"
    ],
    "Wi-Fi connection information": [
        "view Wi-Fi connections"
    ],
    "Camera": [
        "take pictures and videos"
    ],
    "Photos/Media/Files": [
        "modify or delete the contents of your USB storage",
        "read the contents of your USB storage"
    ],
    "Storage": [
        "modify or delete the contents of your USB storage",
        "read the contents of your USB storage"
    ],
    "Device ID & call information": [
        "read phone status and identity"
    ],
    "Contacts": [
        "find accounts on the device"
    ],
    "Phone": [
        "read phone status and identity"
    ],
    "Identity": [
        "add or remove accounts",
        "find accounts on the device"
    ],
    "Other": [
        "access Bluetooth settings",
        "allow Wi-Fi Multicast reception",
        "change network connectivity",
        "change your audio settings",
        "control Near Field Communication",
        "control vibration",
        "full network access",
        "install shortcuts",
        "pair with Bluetooth devices",
        "prevent device from sleeping",
        "run at startup",
        "send sticky broadcast",
        "use accounts on the device",
        "view network connections"
    ],
    "Uncategorized": [
        "receive data from Internet"
    ]
}
```
### App Search
```python
from google_play_scraper import search

result = search("best Pikachu game",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=3  # defaults to 30 (= Google's maximum)
)
result
```

Result of `print(result)`:

```
[{'appId': 'com.nianticlabs.pokemongo',
  'icon': 'https://play-lh.googleusercontent.com/SVQIX_fYcu5mc4Pq-D7dgxXZdRMpNTAbRKeBJygAsIXKITHEcKckyhzLsIXMQLSRZw',
  'screenshots': ['https://play-lh.googleusercontent.com/O-OR6Mh0AoNyiaYYaa3OJ_VHGfLqWW2qNzUUZxRRodD3fqs2Pm04FatavdNbz-jsMZM',
   'https://play-lh.googleusercontent.com/HiLNXxmIpOl1jLBssHWcGqsQ58oUC5RvmS5tiX7L86mPHCG6wVEN-aX5OxTKAbDzh10',
   'https://play-lh.googleusercontent.com/Il9B11lqrHX_Kd3QzLCA6hA6O7EsT56ItiLWMf1JkwcdmRyR3CE2KW_vR9w1izanO-JM',
   'https://play-lh.googleusercontent.com/_84Pq9dJ0_iTKwx9-CkYFYoakSMKK_yfdrp1WSX-inE2XvCTr8ri2tKoISLHN_9PEvP5',
   'https://play-lh.googleusercontent.com/JjgLXR7CMiQfSbtICOa86_35f7Pf8IzJn78zWQslwJn56Qm2O7BOV7xzXXE8mz3Vhg',
   'https://play-lh.googleusercontent.com/iAYd9LdbFI7aajPU760XoNZ8b3woDQ58B0harYiUed2y7WQLU19fcj9I8yS-_K9BDQ',
   'https://play-lh.googleusercontent.com/lpw5tz7Onf_6Sx4Q3kGX1zKXcec4EWpRyr9I4w5d3TrQMoorPWVke6veB5qmqhfQZn4',
   'https://play-lh.googleusercontent.com/KgDQ-Kjb2B7_jDP-8KmQDNhAmP2lqAV_w3zArOCBL7YZnQ02Qqp4VTlgdocO-4MFk4s'],
  'title': 'Pokémon GO',
  'score': 4.283571,
  'genre': 'Adventure',
  'price': 0,
  'free': True,
  'currency': 'USD',
  'video': 'https://www.youtube.com/embed/DFXbVBFPOOs?ps=play&vq=large&rel=0&autohide=1&showinfo=0',
  'videoImage': 'https://i.ytimg.com/vi/DFXbVBFPOOs/hqdefault.jpg',
  'description': 'New! Now you can battle other Pokémon GO Trainers online! Try the GO Battle League today!\r\n\r\nJoin Trainers across the globe who are discovering Pokémon as they explore the world around them. Pokémon GO is the global gaming sensation that has been downloaded over 1 billion times and named “Best Mobile Game” by the Game Developers Choice Awards and “Best App of the Year” by TechCrunch.\r\n_______________\r\n\r\nUncover the world of Pokémon: Explore and discover Pokémon wherever you are!\r\n \r\nCatch more Pokémon to complete your Pokédex!\r\n \r\nJourney alongside your Buddy Pokémon to help make your Pokémon stronger and earn rewards!\r\n\r\nCompete in epic Gym battles and...\r\n\r\nTeam up with other Trainers to catch powerful Pokémon during Raid Battles!\r\n \r\nIt’s time to get moving—your real-life adventures await! Let’s GO!\r\n_______________\r\n\r\nNotes: \r\n- This app is free-to-play and offers in-game purchases. It is optimized for smartphones, not tablets.\r\n- Compatible with Android devices that have 2GB RAM or more and have Android Version 6.0–10.0+ installed.\r\n- Compatibility is not guaranteed for devices without GPS capabilities or devices that are connected only to Wi-Fi networks.\r\n- Application may not run on certain devices even if they have compatible OS versions installed.\r\n- It is recommended to play while connected to a network in order to obtain accurate location information.\r\n- Compatibility information may be changed at any time.\r\n- Please visit PokemonGO.com for additional compatibility information. \r\n- Information current as of October 20, 2020.',
  'descriptionHTML': 'New! Now you can battle other Pokémon GO Trainers online! Try the GO Battle League today!<br><br>Join Trainers across the globe who are discovering Pokémon as they explore the world around them. Pokémon GO is the global gaming sensation that has been downloaded over 1 billion times and named “Best Mobile Game” by the Game Developers Choice Awards and “Best App of the Year” by TechCrunch.<br>_______________<br><br>Uncover the world of Pokémon: Explore and discover Pokémon wherever you are!<br> <br>Catch more Pokémon to complete your Pokédex!<br> <br>Journey alongside your Buddy Pokémon to help make your Pokémon stronger and earn rewards!<br><br>Compete in epic Gym battles and...<br><br>Team up with other Trainers to catch powerful Pokémon during Raid Battles!<br> <br>It’s time to get moving—your real-life adventures await! Let’s GO!<br>_______________<br><br>Notes: <br>- This app is free-to-play and offers in-game purchases. It is optimized for smartphones, not tablets.<br>- Compatible with Android devices that have 2GB RAM or more and have Android Version 6.0–10.0+ installed.<br>- Compatibility is not guaranteed for devices without GPS capabilities or devices that are connected only to Wi-Fi networks.<br>- Application may not run on certain devices even if they have compatible OS versions installed.<br>- It is recommended to play while connected to a network in order to obtain accurate location information.<br>- Compatibility information may be changed at any time.<br>- Please visit PokemonGO.com for additional compatibility information. <br>- Information current as of October 20, 2020.',
  'developer': 'Niantic, Inc.',
  'installs': '100,000,000+'},
 {'appId': 'jp.pokemon.pokemonunite',
  'icon': 'https://play-lh.googleusercontent.com/l6iBBhrah3mNhvcjZgZBwICAF5uu3KjorU4pq-eMOxYgT_L_TnpzT7a3TmmdxaMMgbUy',
  'screenshots': ['https://play-lh.googleusercontent.com/0BXdHWr_OWcqwc2egRCGa9el75tMO9VS7tj2K2oiHMulKpVZ7t7eKLYwdye7JnUhdxMj',
   'https://play-lh.googleusercontent.com/tReAAbW5OMk2tFwAWHuCCjdfUHTcx11tHPfmX8HF9ggTf4dJZ5A5AKfEoGYhg0ee9kU',
   'https://play-lh.googleusercontent.com/VVXVsn7QiICtyN7VI4IlFAhC4i5Vw-ezx3sLbywIG01HpKUlbVcDsnqM6Rc6TStHgQ',
   'https://play-lh.googleusercontent.com/qIdex-XxcS2Dl5Efq6DJF39VQuJShLoeLC0X40YiqeSV-ePG0N2CGKWbZI07sXPEDDo',
   'https://play-lh.googleusercontent.com/BQun4awXd5t-NapkXAI7-uyOl1PzWr80NWPKnSsDBrR8-FZLLBIz5KNg_pHK36EMoYYK',
   'https://play-lh.googleusercontent.com/57M-IQvvMsyRUULDZZ6cXGRaiVJMUY9ABf7R19sdmi8sS-hOzf7wp3v5JgOxrIMcag',
   'https://play-lh.googleusercontent.com/BOIBHIXkqZKDcUSvZUM88GiftsIxLoFU1qR2R0PiKRImWXOT4MG0GRdfRkIhESTlipoc',
   'https://play-lh.googleusercontent.com/F_kaX-tKz2KwQeozaB4emu8OaH422d3uSB9Ovhp3Rdycyh303Pukj-LLmsh4drid4Q2Y',
   'https://play-lh.googleusercontent.com/HuxwQsc_wqUeGgyeclWyiNYKIYbUhx4HL2evXauReksvdMwKazZ2Ze8oYysbPkTH7Do',
   'https://play-lh.googleusercontent.com/h_VR3XmUEbStoW4Kbkz48etOwc6I8AO7caEPmlG_s6QoFn_Hvy8cPGHZs8Ie8sIn4COD',
   'https://play-lh.googleusercontent.com/pXZIkNh6VGWAkL5kDDVUVxAjba1aRVootuQRfHmLRLnI3TC2AqMm5H19M8jIj2jzIQ',
   'https://play-lh.googleusercontent.com/zW64FFgL-bacNW851Z-veKZJEAFjt5G6iA_1DJjH5GGgoBrzOITYOSANSoZRvTrV91Dp',
   'https://play-lh.googleusercontent.com/LgY2r8NPH1SErkQ46Srhyzujxg3Po-ZBo7DYOUrqctIya-DeeTJRbOtC1lAtgdAE3w',
   'https://play-lh.googleusercontent.com/legf5ocJ02NksPSP__k5g7I-EXa9w34F1Xd5BBQ2p4ILvvGdkR2T-CXfqwhzLF4RJW8',
   'https://play-lh.googleusercontent.com/KRaCNowecDHdl1V7y1wkhlBf_qOiGddBNRORXOU5xfAQdjnJqK3RYD8dgCUFY29E_Uo',
   'https://play-lh.googleusercontent.com/Kx2V-5ybEv2m1K1f1v2bJHRO27WNIpb-2Gex6sMh63Fzr9T6Npwh3lDu2tG8oOnP7A',
   'https://play-lh.googleusercontent.com/_yL5mS4Iw65B0L9gfoz--xKbfijilqEA0kEVk5N3muLXBLsWly2BR-mpwJl5Ia2IoQ',
   'https://play-lh.googleusercontent.com/ULyQg55oKym85qsQMvKq0nVginG2gF0qw5g82knbjS15pMu-n_HxRYL86FyOEiRXboQ',
   'https://play-lh.googleusercontent.com/6LZs0vvZFta2dcFjKSglRx-ugeYzYYjM_ziEYv8_O14Hngr6rid2-qYuBsgri8GefQ',
   'https://play-lh.googleusercontent.com/Q5nklhiiZwY_tnUjUlvh9PkDS-H-OF7wBI_AblMUbpVVdVr1CEw1CuO791p_1bU0bkgE',
   'https://play-lh.googleusercontent.com/AVrvQmbm06_cta6VInNudHS0aqOQcZEkM-KRGU8IdN3HW3lHMEXwJsyWTivUK8juBQ',
   'https://play-lh.googleusercontent.com/MaFH8pnG9lT6m7XeaFC0r2ZsRprk9VkSTO22ornPlot9GGrimGl9iBoiy4emMtgOFg'],
  'title': 'Pokémon UNITE',
  'score': 4.5547147,
  'genre': 'Action',
  'price': 0,
  'free': True,
  'currency': 'USD',
  'video': 'https://www.youtube.com/embed/ZLBVuHDguvQ?ps=play&vq=large&rel=0&autohide=1&showinfo=0',
  'videoImage': 'https://i.ytimg.com/vi/ZLBVuHDguvQ/hqdefault.jpg',
  'description': 'Headline:\r\n\r\nPokémon UNITE:\r\nTeam up and take down the opposition in Pokémon’s first 5-on-5 strategic team battle game!  \r\n\r\nJoin Trainers from around the world as they head for Aeos Island to compete in Unite Battles! In Unite Battles, Trainers face off in 5-on-5 team battles to see who can score the most points within the allotted time. Teamwork is key as you and your teammates defeat wild Pokémon, level up, evolve your own Pokémon, and work to prevent the opposing team from scoring points. Put your teamwork to the test, and take home the win!  \r\n\r\nKey Features: \r\n•\tBATTLE IN STYLE: Take to the field while looking your best in Holowear! Thanks to a special technology developed using Aeos energy, Trainers can deck out their Pokémon in a variety of holographic outfits—with new styles arriving regularly! \r\n \r\n•\tUNITE MOVES: Unleash the true power of your Pokémon with Unite Moves! Leverage these all-new Pokémon moves, which are only possible while in Unite Battles, and turn the tide of even the direst situations. \r\n \r\n•\tRANK UP: Looking to prove how skilled you are? Participate in ranked matches, and earn points as you climb up the global leaderboard! \r\n \r\n•\tCOMMUNICATION IS KEY: Even the most skilled Trainers recognize how important communication is to their team’s success. Leverage signals, quick-chat messages, and—for the first time in a Pokémon title—voice chat to communicate and stay in sync with your team. \r\n \r\n•\tCROSS-PLATFORM PLAY: Challenge Trainers from around the world to Unite Battles on the Nintendo SwitchTM system or on a compatible mobile device thanks to cross-platform support. Trainers may use their Pokémon Trainer Club account or Nintendo Account on both Nintendo Switch and mobile to easily keep their progress synced between devices. \r\n\r\n\r\nCheck out the official website for more information, and follow Pokémon UNITE on Twitter for all the latest news. \r\n------------------------------------------------------------\r\nOfficial Website: http://PokemonUNITE.com/\r\nOfficial Twitter: https://twitter.com/PokemonUNITE/\r\n\r\nLegal:\r\n•\tThis is a free-to-start game; optional in-game purchases available. Data charges may apply.\r\n•\tAn internet connection is required to play the game.',
  'descriptionHTML': 'Headline:<br><br>Pokémon UNITE:<br>Team up and take down the opposition in Pokémon’s first 5-on-5 strategic team battle game!  <br><br>Join Trainers from around the world as they head for Aeos Island to compete in Unite Battles! In Unite Battles, Trainers face off in 5-on-5 team battles to see who can score the most points within the allotted time. Teamwork is key as you and your teammates defeat wild Pokémon, level up, evolve your own Pokémon, and work to prevent the opposing team from scoring points. Put your teamwork to the test, and take home the win!  <br><br>Key Features: <br>•\tBATTLE IN STYLE: Take to the field while looking your best in Holowear! Thanks to a special technology developed using Aeos energy, Trainers can deck out their Pokémon in a variety of holographic outfits—with new styles arriving regularly! <br> <br>•\tUNITE MOVES: Unleash the true power of your Pokémon with Unite Moves! Leverage these all-new Pokémon moves, which are only possible while in Unite Battles, and turn the tide of even the direst situations. <br> <br>•\tRANK UP: Looking to prove how skilled you are? Participate in ranked matches, and earn points as you climb up the global leaderboard! <br> <br>•\tCOMMUNICATION IS KEY: Even the most skilled Trainers recognize how important communication is to their team’s success. Leverage signals, quick-chat messages, and—for the first time in a Pokémon title—voice chat to communicate and stay in sync with your team. <br> <br>•\tCROSS-PLATFORM PLAY: Challenge Trainers from around the world to Unite Battles on the Nintendo SwitchTM system or on a compatible mobile device thanks to cross-platform support. Trainers may use their Pokémon Trainer Club account or Nintendo Account on both Nintendo Switch and mobile to easily keep their progress synced between devices. <br><br><br>Check out the official website for more information, and follow Pokémon UNITE on Twitter for all the latest news. <br>------------------------------------------------------------<br>Official Website: http://PokemonUNITE.com/<br>Official Twitter: https://twitter.com/PokemonUNITE/<br><br>Legal:<br>•\tThis is a free-to-start game; optional in-game purchases available. Data charges may apply.<br>•\tAn internet connection is required to play the game.',
  'developer': 'The Pokemon Company',
  'installs': '10,000,000+'},
 {'appId': 'com.dena.a12026418',
  'icon': 'https://play-lh.googleusercontent.com/h4dRm7zBF605F3rNY-KdMlTIGatw4csK1HSUEBit7-PtqPmYuXxzP-Wooy8hRI8YTA',
  'screenshots': ['https://play-lh.googleusercontent.com/82gD-bWWy0B9SHVaPqTnvCNo_SBk0ssGyI2ZrbgOvNQ6FK6guz20aKPKhLcCCUv_SP8',
   'https://play-lh.googleusercontent.com/ysrmlowWJCm5nF-i-nAezyDr_jHlfe0tCOLOSzsIVyGTMQnDxoO5h30uCk5DgYDY6A',
   'https://play-lh.googleusercontent.com/Xj85MdUloyyfLNjud73TBcJL3j9r97O3lEWjwnTyk4hF00gqQb58x64Bx2HoJlmBW5Oi',
   'https://play-lh.googleusercontent.com/J7tY8gJtd5pyiGe-To-Amfbc7aiWqzLqm3Msg0UnLSp0DCtX9mwxS4xAisliQw2OfA0',
   'https://play-lh.googleusercontent.com/u_od4LQquoRSoZF5hA9dAH0dB41illZ6ouYxIl49bH8yHoQulcUslwxy-b9nWxCiOJtM',
   'https://play-lh.googleusercontent.com/wIRwnAKtqBD6GL2Lxnz8K-1jZlZ9qbBUXD5tMToxF-sUyWNBxUD5m_rR8bwXR98oGls',
   'https://play-lh.googleusercontent.com/I-wGFjAD7ut2YGNze8xDVaiR89HCAxKPEOgfYcGpR3Ka5vKjQPH5M4BXti2xWJqEpA',
   'https://play-lh.googleusercontent.com/9cap7BX24s5T_RNPDIXN6rykD0J4LMOhaC1JCPjcRGhkcTO32JNX2GD88Hw5usFjbgo',
   'https://play-lh.googleusercontent.com/j3024cER2J5EIyNIWybWFDqfxuAkvJqrRxTKxAx55eWilRoY7aOF2JvK_yFNMm1CXAkU',
   'https://play-lh.googleusercontent.com/6zEEW5lScq4uIw-7B4w19dDVglcTBRHRG0pUdRHjLpULuUw9hKmLnu8mDonkmlYqTA'],
  'title': 'Pokémon Masters EX',
  'score': 4.3176017,
  'genre': 'Role Playing',
  'price': 0,
  'free': True,
  'currency': 'USD',
  'video': 'https://www.youtube.com/embed/tPN87sf7hyU?ps=play&vq=large&rel=0&autohide=1&showinfo=0',
  'videoImage': 'https://i.ytimg.com/vi/tPN87sf7hyU/hqdefault.jpg',
  'description': 'DYNAMAX! \r\nThe ability to Dynamax comes to Pokémon Masters EX! Now your Pokémon can drastically multiply in size once per battle to unleash a powerful max move on your opponents!\r\n\r\nTRAINERS DON SPECIAL OUTFITS!\r\nEnjoy special and seasonal Trainer outfits—exclusive to Pokémon Masters EX!\r\n\r\nHATCH EGGS & TEAM UP!\r\nHatch Eggs to get new Pokémon! Add hatched Pokémon to your team, and battle your way to the top!\r\n\r\nBUILD THE ULTIMATE TEAM FOR 3-ON-3 BATTLE!\r\nAssemble Trainers and Pokémon to take on battles! Create a team all your own, and aim for victory!\r\n\r\nTRAINERS FROM THE PAST COME TOGETHER!\r\nChampions, Elite Four members, and Gym Leaders from the past have come together! Team up with Trainers and their Pokémon, and go on adventures!\r\n\r\nNEW STORIES WITH YOUR FAVORITE CHARACTERS\r\nIn Pokémon Masters EX, experience an original story that crosses generations—along with familiar Trainers!\r\n\r\n\r\n・We recommend a device with at least 2GB of RAM.\r\n・Android OS 7.0 or higher is recommended.\r\n・Android OS 5.0 or above\r\nNote: \r\n・We do not guarantee functionality on all devices listed above.\r\n・There may be cases where the app does not function properly due to your device’s capabilities, specifications, or particular conditions for using apps.\r\n・It may take time to become compatible with the latest OS.',
  'descriptionHTML': 'DYNAMAX! <br>The ability to Dynamax comes to Pokémon Masters EX! Now your Pokémon can drastically multiply in size once per battle to unleash a powerful max move on your opponents!<br><br>TRAINERS DON SPECIAL OUTFITS!<br>Enjoy special and seasonal Trainer outfits—exclusive to Pokémon Masters EX!<br><br>HATCH EGGS &amp; TEAM UP!<br>Hatch Eggs to get new Pokémon! Add hatched Pokémon to your team, and battle your way to the top!<br><br>BUILD THE ULTIMATE TEAM FOR 3-ON-3 BATTLE!<br>Assemble Trainers and Pokémon to take on battles! Create a team all your own, and aim for victory!<br><br>TRAINERS FROM THE PAST COME TOGETHER!<br>Champions, Elite Four members, and Gym Leaders from the past have come together! Team up with Trainers and their Pokémon, and go on adventures!<br><br>NEW STORIES WITH YOUR FAVORITE CHARACTERS<br>In Pokémon Masters EX, experience an original story that crosses generations—along with familiar Trainers!<br><br><br>・We recommend a device with at least 2GB of RAM.<br>・Android OS 7.0 or higher is recommended.<br>・Android OS 5.0 or above<br>Note: <br>・We do not guarantee functionality on all devices listed above.<br>・There may be cases where the app does not function properly due to your device’s capabilities, specifications, or particular conditions for using apps.<br>・It may take time to become compatible with the latest OS.',
  'developer': 'DeNA Co., Ltd.',
  'installs': '10,000,000+'}]
```

## Changes
Change logs are here : [CHANGELOG.md](CHANGELOG.md)