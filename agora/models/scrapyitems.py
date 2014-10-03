import scrapy


class AgoraItem(scrapy.Item):
	url = scrapy.Field()
	name = scrapy.Field()
	description = scrapy.Field()
	country = scrapy.Field()
	quantity = scrapy.Field()
	seller = scrapy.Field()