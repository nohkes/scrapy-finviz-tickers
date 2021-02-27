import scrapy

class TickerSpider(scrapy.Spider):
    name = "ticker"
    start_urls = [
        'https://www.finviz.com/screener.ashx?v=111&f=cap_small,geo_usa,sh_avgvol_o300,sh_opt_option,sh_short_low&ft=4&o=-change'
    ]

    def parse(self, response):
        
        for ticker in response.css('a.screener-link-primary'):
            yield {
                'ticker': ticker.css('.screener-link-primary::text').getall()
            }
            next_page = response.css( ".tab-link::attr(href)")[-7].get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)