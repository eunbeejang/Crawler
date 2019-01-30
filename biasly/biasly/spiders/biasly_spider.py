import scrapy

from biasly.items import BiaslyItem

class RTSpider(scrapy.Spider):
	name = "Cosmopolitan"
	allowed_domains = ["cosmopolitan.com"]
	start_urls = ["https://www.cosmopolitan.com/entertainment/movies/"]

	def parse(self, response):
		# info about what to scrape
		"""
		1. get xPath: (terminal) scrapy shell "https://www.cosmopolitan.com/entertainment/movies/"
		2. find the selector
		3. add /@href to the xpath then extract
		(ie. response.xpath('/html/body/div[2]/div[3]/div[1]/div[2]/a/@href')[0].extract())
		4. url = <step3>
		response.urljoin(url) will return the full addess to the link
		5. find all links

		In [68]: all_url = []   
    ...: for main_cont in response.xpath('/html/body/div[2]/div[3]/div'):
    ...:     href = (main_cont.xpath('./div[2]/a/@href')).extract()
    ...:     if href:
    ...:         url = response.urljoin(href[0]) 
    ...:         all_url.append(url)
    ...: print(all_url)

		6. if <step 5 works, then add the code below>
		"""
		for main_cont in response.xpath('/html/body/div[2]/div[3]/div'):
			href = (main_cont.xpath('./div[2]/a/@href')).extract()
			if href:
				url = response.urljoin(href[0]) 
				yield scrapy.Request(url, callback=self.parse_page_contents)


	def parse_page_contents(self, response):
		item = BiaslyItem()
		item["title"] = response.xpath('/html/body/div[2]/header/div/h1/text()')[0].extract().strip()
		item["body"] = response.xpath('/html/body/div[2]/div[4]/div[1]//p/text()').extract() 
		item["url"] = response.xpath('/html/head/link[15]//@href')[0].extract()
		yield item

		# to run crawler (terminal) scrapy crawl Cosmopolitan -o cosmopolitan.csv








