# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from crawlDouBan.items import CrawldoubanItem


class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/26581837/collections?start=0']

    rules = (
        Rule(LinkExtractor(allow=""), callback="parse", follow=True),
    )
    def start_requests(self):
        str_cookies = 'll="118114"; bid=MzayUA8LzG8; push_doumail_num=0; __utmv=30149280.14490; __yadk_uid=IlBGqNgouTQxt3JrLFn2SMrHxT1Vdsyf; douban-fav-remind=1; _vwo_uuid_v2=DB971F286DEF776A0EB7B229FD772F248|ae86a6a894e390be88d5e0b21a9a391f; trc_cookie_storage=taboola%2520global%253Auser-id%3Dcc01233f-d45a-4989-97f1-3a33179ef29c-tuct4208d5d; __gads=ID=4cd505b47576d520:T=1563665602:S=ALNI_MafDYUTgCd2b_2rB73AjjCoFwuZQQ; __utmz=223695111.1566373023.8.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ct=y; viewed="1209975"; gr_user_id=9e58812b-f2e8-4fca-b414-81700d9af419; __utmz=30149280.1567386479.24.19.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ap_v=0,6.0; acw_tc=276082a615681670247592159e5a2d706f847a471f5eb61f83b2a1217fed56; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1568167026%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.931219988.1562929992.1567386479.1568167067.25; __utmc=30149280; __utma=223695111.432825576.1562930009.1566373023.1568167069.9; __utmb=223695111.0.10.1568167069; __utmc=223695111; __utmb=30149280.4.10.1568167067; push_noty_num=0; dbcl2="144902619:cfq8HiiEw6I"; ck=dTSR; _pk_id.100001.4cf6=f3bfff4d7162e768.1562930009.9.1568171289.1566373909.'
        dict_cookies = {
            i.split('=')[0]: i.split('=')[1] for i in str_cookies.split("; ")
        }
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=dict_cookies, callback=self.parse_item)

    def parse_item(self, response):
        item = CrawldoubanItem()
        item['stars'] = response.xpath('//*[@id="collections_tab"]/div[2]/table//span/@title').extract()
        yield item
