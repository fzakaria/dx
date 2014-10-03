import scrapy


class TorrentItem(scrapy.Item):
	url = scrapy.Field()
	name = scrapy.Field()
	description = scrapy.Field()
	country = scrapy.Field()
	quantity = scrapy.Field()
	seller = scrapy.Field()