import re
from enum import Enum, unique


class Types(Enum):
    extensions = 1
    themes = 2


# 分类
# https://chrome.google.com/webstore/category/{Category}?gl=us&hl=en
class Category(Enum):
    accessibility = 'ext/22-accessibility'
    blogging = 'ext/10-blogging'
    web_development = 'ext/11-web-development'
    fun = 'ext/14-fun'
    news = 'ext/6-news'
    photos = 'ext/28-photos'
    productivity = 'ext/7-productivity'
    search_tools = 'ext/38-search-tools'
    shopping = 'ext/12-shopping'
    communication = 'ext/1-communication'
    sports = 'ext/13-sports'


# 榜单
# https://chrome.google.com/webstore/category/collection/{Collection}?gl=us&hl=en
class Collection(Enum):
    top_accessibility = "3p_accessibility_extensions"
    top_blogging = "top_picks_blogging"
    top_web_development = "top_picks_web-development"
    top_fun = "top_picks_fun"
    top_news = "top_picks_news"
    top_photos = "top_picks_photos"
    top_productivity = "top_picks_productivity"
    top_search_tools = "top_picks_search-tools"
    top_shopping = "top_picks_shopping"
    top_communication = "top_picks_communication"
    top_sports = "top_picks_sports"


class Country(Enum):
    us = 'us'
    cn = 'cn'


class Language(Enum):
    us = 'en'
    cn = 'zh-CN'
