# encoding: utf-8
import re

from comics.aggregator.crawler import CrawlerBase, CrawlerImage
from comics.core.comic_data import ComicDataBase


class ComicData(ComicDataBase):
    name = "Anleggsplassen"
    language = "no"
    url = "https://www.at.no/"
    rights = "Trond J. Stavås"


class Crawler(CrawlerBase):
    history_capable_days = 7
    schedule = "Fr"
    time_zone = "Europe/Oslo"

    def crawl(self, pub_date):
        page = self.parse_page(ComicData.url)
        article = page.root.xpath('//span[.="Ukens stripe"]/..')
        article = article[0]
        title = article.get("data-article-headline")
        date = article.get("data-publish-date")[0:10]
        if not pub_date.strftime("%Y-%m-%d") == date:
            return

        image = article.xpath(
            'figure[@data-headline-prefix="Anlegg"]' "/a/div/noscript/picture/source"
        )
        srcset = image[0].get("srcset")
        matches = re.search(
            r"//(img\.gfx\.no/[0-9]+/[0-9]+/.+?)\.[0-9x]+mc\.([a-z]+)",
            srcset,
        )
        url = "https://%s.%s" % (matches.group(1), matches.group(2))

        return CrawlerImage(url, title)
