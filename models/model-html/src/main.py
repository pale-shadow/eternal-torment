import asyncio
import json
import logging

import aiohttp
from pandas.io.json import json_normalize

import spider
import util

if __name__ == "__main__":
    """[summary]"""
    my_util = util.Util()
    # content = my_util.scrape_url(url)

    url = "https://www.bitsmasher.net"

    my_spider = spider.Spider()
    my_spider.processUrl(url)
