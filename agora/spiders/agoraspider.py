from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class AgoraSpider(CrawlSpider):

    name = 'agora'
    allowed_domains = ['agorahooawayyfoe.onion']
    start_urls = ['http://agorahooawayyfoe.onion']
    rules = [Rule(LinkExtractor(allow=['/p/\w+']), 'parse_product')]

    def parse_product(self, response):
        torrent = TorrentItem()
        torrent['url'] = response.url
        torrent['name'] = response.xpath("//h1/text()").extract()
        torrent['description'] = response.xpath("//div[@id='description']").extract()
        torrent['size'] = response.xpath("//div[@id='info-left']/p[2]/text()[2]").extract()
        return torrent