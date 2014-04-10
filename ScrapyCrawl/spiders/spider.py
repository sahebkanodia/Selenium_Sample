from scrapy.spider import BaseSpider
from scrapy.http import TextResponse
from ScrapyCrawl.items import ScrapycrawlItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import XMLFeedSpider
from scrapy.contrib.pipeline.images import ImagesPipeline
import random, time, json
import unicodedata

links = {}

json_data=open('data.jl', 'r')
data = json.load(json_data)
json_data.close()

class FlipkartSpider (BaseSpider):
	name = 'Flipkart'
	allowed_domains =['www.flipkart.com']
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'flipkart.com':
				for j in range(len(data[i]['flipkart.com'])):
					li.append(data[i]['flipkart.com'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem()
			hxs = HtmlXPathSelector (response)
			item['site'] = 'flipkart.com'
			item['partner_url'] = response.url
			title = hxs.select('//div[@class="mprod-summary-title fksk-mprod-summary-title"]/h1/text()').extract()
			if "".join (title).strip() == "":
				title = hxs.select("//div[@id='fk-mainbody-id']/div[@class='fk-content fksk-content enable-compare']/div[@class='fk-mproduct fk-mproduct-digital_ebook ']/div[@class='mprod-section unit']/div[@id='topsection']/div[@class='mprod-summary lastUnit']/ul[@class='digital-details-list']/li[1]/div/div[@class='digital-top-title unit']/h1[@id='prd-title']/text()").extract()
			if title:
				item['partner_title'] = title[0].strip ()
			else:
				item['partner_title'] = 'Not Found'
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select('//span[@class="fk-font-finalprice fk-font-verybig pprice fk-bold"]/text()').extract()
			if not price:
				price = hxs.select('//span[@class="fk-font-finalprice fk-font-big fk-bold final-price"]/text()').extract()
			if not price:
				price = hxs.select('//span[@class="fk-font-finalprice fk-font-verybig pprice fk-bold"]/text()').extract()
			if not price:
				price =hxs.select('//span[@class="fk-font-verybig pprice fk-bold"]/text()').extract()
			if not price:
				price = hxs.select("//div[@id='topsection']/div[@class='mprod-summary lastUnit']/div[@class='shop-section line bmargin10']/div[@class='unit size1of2']/div[@class='line']/div[@class='prices']/div/span[@class='fk-font-verybig pprice fk-bold']/text()").extract()
			if "".join (price).strip () == "":
				price =hxs.select("//div[@id='fk-mainbody-id']/div[@class='fk-content fksk-content enable-compare']/div[@class='fk-mproduct fk-mproduct-digital_ebook ']/div[@class='mprod-section unit']/div[@id='topsection']/div[@class='mprod-summary lastUnit']/div[@class='line price']/div[@class='unit media']/div[@class='discount-icon price-info fk-float-left']/span/span[@class='final-price']/text()").extract ()
			if "".join (price).strip () == "":
				price =hxs.select("//div[@class='prices']/meta[@itemprop='price']/@content").extract ()
			if price and not price[0].strip () == "":
				item['partner_price'] = price[0].replace ("Rs.", "").strip ()
			else:
				item['partner_price'] = 0
			items.append (item)
			return items
		except:
			pass

class Shopin1 (BaseSpider):
	name = 'shopin1'
	allowed_domains =['www.shop.inonit.in']
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'inonit.in':
				for j in range(len(data[i]['inonit.in'])):
					li.append(data[i]['inonit.in'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem()
			hxs = HtmlXPathSelector(response)
			item['site'] = 'inonit.in'
			item['partner_url'] = response.url
			title =hxs.select("//div[@class='ctl_aboutbrand']/h1/text() | //div[@id='main']/div[3]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/h1/text()").extract()
			if title:
				item['partner_title'] = title[0]
			else:
				item['partner_title'] = 'Not Found'
			item['partner_title'] = item['partner_title'].lower()
			price =hxs.select("//span[@id='ctl00_ContentPlaceHolder1_Price_ctl00_lblOfferPrice']/text() | //div[@class='ctl_productdetail']/div[@class='productprices']/ div[@class='productofferprice']/ span[@class='offer'] / span[@id='ctl00_ContentPlaceHolder1_Price_ctl00_lblOfferPrice']/text()").extract ()
			if price:
				item['partner_price'] = price[0].replace ("Rs.", "").replace (',', '')
				item['partner_price'] = item['partner_price'].strip()
			else:
				item['partner_price'] = 0
			items.append (item)
			return items
		except:
			pass

class Happilyunmarried_Spider(BaseSpider):
	name = 'Happily'
	allowed_domains =['www.happilyunmarried.com']
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'happilyunmarried.com':
				for j in range(len(data[i]['happilyunmarried.com'])):
					li.append(data[i]['happilyunmarried.com'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem()
			hxs =HtmlXPathSelector(response)
			item['site'] = 'happilyunmarried.com'
			item['partner_url'] = response.url
			title = hxs.select("//div[@class='product-shop']/div[@class='product-description-box product-description-box-long']/div[@class='product-name']/h1[@class='product-name-heading-main']/text()").extract()
			if "".join (title).strip () == "":
				title = hxs.select('//div[@class="wrapper"]/div[@class="page"]/div[@id="main-container_col1-layout"]/div[@class="main"]/div[@class="col-main"]/div[@class="happy-product-view"]/h1[@class="happy-title"]/text()').extract()
			if "".join (title).strip () == "":
				title =hxs.select("//form[@id='product_addtocart_form']/div[@class='product-shop']/div[@class='product-description-box']/div[@class='product-name']/h1[@class='product-name-heading-main']/text()").extract()
			if title:
				item['partner_title'] = title[0]
			else:
				item['partner_title'] = 'Not Found'
			item['partner_title'] = item['partner_title'].strip()			
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select("//form[@id='product_addtocart_form']/div[@class='product-shop']/div[@class='product-description-box product-description-box-long']/div[@class='product-page-price']/div[@class='price-box']/span/text()").extract()
			if "".join (price).strip () == "":
				price = hxs.select("//form[@id='product_addtocart_form']/div[@class='product-shop']/div[@class='product-description-box']/div[@class='product-page-price']/div[@class='price-box']/span/text()").extract()
			if "".join (price).strip () == "":
				price = hxs.select("//form[@id='product_addtocart_form']/div[@class='product-shop']/div[@class='product-description-box']/div[@class='product-page-price']/div[@class='price-box']/div[@class='special-price']/span/text()").extract()
			if "".join (price).strip () == "":
				price = hxs.select("//form[@id='product_addtocart_form']/div[@class='product-shop']/div[@class='product-description-box product-description-box-long']/div[@class='product-page-price']/div[@class='price-box']/div[@class='special-price']/span/text()").extract ()
			if "".join (price).strip () == "":
				price = hxs.select("//div[@class='product-shop']/div[@class='product-description-box product-description-box-long']/div[@class='product-page-price']/div[@class='price-box']/span/text()").extract()
			if "".join (price).strip () == "":
				price =hxs.select("//div[@id='fancybox-content']/div[@class='product-view']/div[@class='product-essential']/form[@id='product_addtocart_form']/div[@class='product-options-container']/div[@class='product-options-bottom quantity-price-addtocart-container']/div[@class='add-to-cart custom-add-to-cart']/div[@class='quantity_box']/div[@class='price_element']/div[@class='price-box']/span[@id='product-price-']/text()").extract ()
			if price:
				for prc in price:
					pp = prc.replace ("Rs. ", "").replace (" Rs", "").replace (",","").replace (" Rs","").strip()
					if pp.isdigit ():
						item['partner_price'] = pp
						break
					else:
						item['partner_price'] = 0
			else:
				item['partner_price'] = 0
			items.append(item)
			return items
		except:
			pass

class HealthKart_Spider (BaseSpider):
	name = 'Healthkart'
	allowed_domains =['www.healthkart.com']
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'healthkart.com':
				for j in range(len(data[i]['healthkart.com'])):
					li.append(data[i]['healthkart.com'][j]['partner_url'])
	start_urls = li
 

	def parse (self, response):
		try:
			items = []
			item = ScrapycrawlItem ()
			hxs = HtmlXPathSelector(response)
			item['site'] = 'healthkart.com'
			item['partner_url'] = response.url
			title = hxs.select("//div[@id='variant-page']/div[@class='container clearfix']/div[@class='js-hvr-rvw']/div[@class='ttl-cntnr']/h1/text()").extract()
			if "".join (title).strip () == "":
				title = hxs.select("//div[@class='marginBox']/div[@class='ttl-cntnr']/h1/text()").extract()
			if "".join (title).strip () == "":
				title = hxs.select('//div[@class="product_details"]/h2[@class="prod_title"]/text()').extract()
			if "".join (title).strip () == "":
				title = hxs.select("//div[@class='ttl-cntnr']/h1[@class='prod_title']/text()").extract()
			if title:
				item['partner_title'] = title[0].strip()
			else:
				item['partner_title'] = 'Not Found'
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select("//p[@class='mrgn-t-5 prc-svning']/span[@class='sucss-txt']/text()").extract()

			if "".join (price).strip () == "":
				price =hxs.select('//form[@class="addToCartForm"]/div[@class="row prods"]/div[@class="prices"]/div[@class="hk"]/span[@class="num"]/text()').extract()
			if not price:
				price =	hxs.select('//div[@class="product_details"]/div[@class="buy_prod"]/div[@class="left_col"]/div[@class="prices"]/div[@class="hk"]/span[@class="num"]/span/text()').extract()
			if not price:
				price = hxs.select('//div[@class="product_details"]/div[@id="tabs"]/div[@id="selection-tab"]/div[@class="prices"]/div[@class="hk"]/span[@class="num"]/text()').extract()
			if not price:
				price =	hxs.select('//div[@class="prices"]/div[@class="hk"]/span[@class="num"]/text()').extract()
			if not price:
				price = hxs.select('//div[@class="product_details"]/div[4]/form[@class="addToCartForm"]/div[@class="buy_prod"]/div[@class="left_col"]/div[@class="prices"]/div[@class="hk"]/span[@class="num"]/text()').extract()
			if not price:
				price = hxs.select('//div[@class="contentDiv"]/div[@class="container_24 containerDiv"]/form[@class="addToCartForm"]/div[@class="grid_24"]/div[@class="grid_8 buyDiv"]/div[@class="left_col"]/div[@class="prices"]/div[@class="hk"]/span[@class="num"]/text()').extract()
			if not price:
				price = hxs.select('//div[@class="product_details"]/div[@class="variants"]/div[@class="prod_table"]/div[@class="table_body"]/form[@class="addToCartForm"]/div[@class="row prods"]/div[@class="prices"]/div[@class="hk"]/span[@class="num"]/text()').extract()
			if not price:
				price = hxs.select ("//div[@class='prices cont-lft']/p[@class='hk']/span[@class='num']/text()").extract ()
			if price:
				p = price[0].replace (",", "")
				l = p.split()
				ip =[int (s) for s in l if s.isdigit ()]
				prc =ip
				item['partner_price'] = prc[0]
			else:
				item['partner_price'] = 0
			item['partner_price'] = str(item['partner_price'])
			items.append(item)
			return items
		except:
			pass

class Dezains_Spider (BaseSpider):
	name = 'Dezains'
	allowed_domains =['www.dezains.com']
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'dezains.com':
				for j in range(len(data[i]['dezains.com'])):
					li.append(data[i]['dezains.com'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem()
			hxs = HtmlXPathSelector (response)
			item['site'] = 'dezains.com'
			item['partner_url'] = response.url
			title = hxs.select ('//div[@id="eb-page"]/div[@id="eb-main"]/div[@id="eb-main-wrapper"]/div[@id="eb-main-wrapper-fix"]/div[@id="primary_block"]/article[@id="eb-product-content"]/div[@class="eb-product-pad"]/hgroup[@class="clearfix"]/h1/text()').extract()
			if title:
				item['partner_title'] = title[0]
			else:
				item['partner_title'] = 'Not Found'
			item['partner_title'] = item['partner_title'].strip().lower()
			
			price = hxs.select ('//div[@id="eb-page"]/div[@id="eb-main"]/div[@id="eb-main-wrapper"]/div[@id="eb-main-wrapper-fix"]/div[@id="primary_block"]/article[@id="eb-product-content"]/div[@class="eb-product-pad"]/div[@class="content_prices clearfix"]/div[@class="price"]/span[@class="our_price_display"]/span[@id="our_price_display"]/text()').extract()
			if price:
				p = price[0].replace (",", "")
				l = p.split()
				ip =[int (s) for s in l if s.isdigit ()]
				prc = ip
				item['partner_price']=prc[0]
			else:
				item['partner_price'] = 0
			item['partner_price'] = str(item['partner_price'])
			items.append (item)
			return items
		except:
			pass

class FNP_Spider (BaseSpider):
	name = 'Fnp'
	allowed_domains =['www.fnp.com']
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'fnp.com':
				for j in range(len(data[i]['fnp.com'])):
					li.append(data[i]['fnp.com'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem ()
			hxs = HtmlXPathSelector (response)
			item['partner_url'] = response.url
			item['site'] = 'fnp.com'
			title = hxs.select ('///div[@class="productDisplay"]/div[@class="productDesc"]/div[@class="productName"]/h1/text()').extract ()
			if title:
				item['partner_title'] = title[0]
			else:
				item['partner_title'] = 'Not Found' 
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select ('///div[@class="productDisplay"]/div[@class="productDesc"]/div[@id="itemPriceDiv"]/div[@class="productDescDetail"]/div[@class="offerPriceDiv"]/span[2]/text()').extract()
			if price:
				item['partner_price'] = price[0].strip()
			else:
				item['partner_price'] = 0
			items.append (item)
			return items
		except:
			pass 

class Vmate_Spider (BaseSpider):
	name = 'Vmate'
	allowed_domains =['www.vouchersmate.com']
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'vouchersmate.com':
				for j in range(len(data[i]['vouchersmate.com'])):
					li.append(data[i]['vouchersmate.com'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem ()
			hxs = HtmlXPathSelector (response) 
			item['site'] = 'vouchersmate.com' 
			item['partner_url'] = response.url
			title = hxs.select ("//div[@id='product']/div[@class='details']/h1/text()").extract()
			if "".join (title).strip () == "":
				title = hxs.select ('//div[@class="pivot"]/div[@class="center"]/div/h1/text()').extract()
			if title:
				item['partner_title'] = title[0].strip()
			else:
				item['partner_title'] = 'Not Found' 
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select ("//div[@id='product']/div[@class='details']/div[@class='prices']/div[@class='product-price']/span/text()").extract ()
			if "".join (price).strip () == "":
				price = hxs.select ("//div[@id='product']/div[@class='details']/div[@class='product-collateral']/div[@class='product-variant-list']/div[@class='product-variant-line']/div[@class='variant-overview']/div[@class='prices']/div[@class='product-price']/span/text()").extract()
			if "".join (price).strip () == "":
				price = hxs.select ('//section[@class="product-info"]/div[@class="right"]/div[@class="description"][1]/div[@class="price"]/div/div[@class="price-new"]/text()').extract()
			if price:
				p = price[0].replace (",", "")
				pp = p.replace (".00", "")
				l = pp.split ()
				ip =[int (s) for s in l if s.isdigit ()]
				prc =ip
				item['partner_price']=prc[0]
			else:
				item['partner_price'] = 0
			item['partner_price'] = str(item['partner_price'])
			items.append (item)
			return items
		except:
			pass


class Exlives_Spider (BaseSpider):
	name = 'Exlives'
	allowed_domains =['www.excitinglives.com']
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'excitinglives.com':
				for j in range(len(data[i]['excitinglives.com'])):
					li.append(data[i]['excitinglives.com'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem ()
			hxs = HtmlXPathSelector (response) 
			item['partner_url'] = response.url
			item['site'] = 'excitinglives.com' 
			title = hxs.select ("//div[@id='ngcenterbarnew']/font[@class='maintext']/div[@class='productnamebox']/font[@class='productname']/text()").extract ()
			if "".join (title).strip () == "":
				title = hxs.select ('//div[@class="ngcenterbar"]/font[@class="maintext"]/form/font[@class="productname"]/text() | //div[@class="ngcenterbar"]/font[@class="maintext"]/form/div[@class="productnamebox"]/font[@class="productname"]/text()').extract()
			if not title:
				title = hxs.select ('//form/div[@class="productnamebox"]/font[@class="productname"]/text()').extract()
			if title:
				item['partner_title'] = title[0]
			else:
				item['partner_title'] = 'Not Found'
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select ("//div[@id='ngcenterbarnew']/font[@class='maintext']/div[@class='productnamebox']/font[@class='biggertext']/text()").extract()
			if "".join (price).strip () == "":
				price = hxs.select ('//div[@class="ngcenterbar"]/font[@class="maintext"]/form/font[@class="biggertext"]/text() | //div[@class="ngcenterbar"]/font[@class="maintext"]/form/div[@class="productnamebox"]/font[@class="biggertext"]/text()').extract()
			if not price:
				price = hxs.select ('//form/div[@class="productnamebox"]/font[@class="biggertext"]/text()').extract()
			if price:
				item['partner_price'] = price[0].replace ("Rs.", "")
			else:
				item['partner_price'] = 0 
			items.append (item)
			return items 
		except:
			pass

class Dgifts_Spider (BaseSpider):
	name = 'Dgifts' 
	allowed_domains =['www.delightgifts.in'] 

	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'delightgifts.in':
				for j in range(len(data[i]['delightgifts.in'])):
					li.append(data[i]['delightgifts.in'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items = []
			item = ScrapycrawlItem()
			hxs = HtmlXPathSelector(response)
			item['site'] = 'delightgifts.in'
			item['partner_url'] = response.url
			title = hxs.select ('//div[@class="product-top-wrapper"]/div[@class="product-top"]/div[@class="product-top-inner clearer"]/div[@class="product-shop"]/div[@class="product-name"]/h1/text()').extract()
			if not title:
				title = hxs.select ("//div[@class='product-shop']/form[@id='product_addtocart_form']/div[@class='product-name']/h1/text()").extract()
			if title:
				item['partner_title'] = title[0]
			else:
				item['partner_title'] = 'Not Found'
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select ('//div[@class="product-top-wrapper"]/div[@class="product-top"]/div[@class="product-top-inner clearer"]/div[@class="product-shop"]/div[@class="container1-wrapper"]/div[@class="product-options-bottom"]/div[@class="price-box"]/span/span[@class="price"]/text()').extract()
			if not price:
				price = hxs.select ('//div[@class="product-top-wrapper"]/div[@class="product-top"]/div[@class="product-top-inner clearer"]/div[@class="product-shop"]/div[@class="add-to-box"]/div[@class="price-box"]/span/span[@class="price"]/text()').extract()
			if not price:
				price = hxs.select ("//div[@class='product-shop']/form[@id='product_addtocart_form']/div[@class='add-to-box']/div[@class='price-box']/span[@class='regular-price']/span[@class='price']/text()").extract()
			if not price:
				price = hxs.select ("//div[@class='container1-wrapper']/div[@class='product-options-bottom']/div[@class='price-box']/span/span[@class='price']/text()").extract()
			if not price:
				price = hxs.select ("//div[@class='product-shop']/form[@id='product_addtocart_form']/div[@class='product-type-data']/div[@class='price-box']/span/span[@class='price']/text()").extract()
			if price:
				pr = price[0].replace ("Rs. ", "") 
				prc = pr.replace (",", "") 
				item['partner_price'] = prc
			else:
				item['partner_price'] = 0 
			items.append (item) 
			return items 
		except:
			pass

class Babyoye_Spider (BaseSpider):
	name = 'Babyoye' 
	allowed_domains =['www.babyoye.com'] 
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'babyoye.com':
				for j in range(len(data[i]['babyoye.com'])):
					li.append(data[i]['babyoye.com'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem()
			hxs = HtmlXPathSelector(response)
			item['site'] = 'babyoye.com' 
			item['partner_url'] = response.url
			title = hxs.select("//div[@id='outer_wrapper']/section[@id='body_contentWrap']/div[@id='content']/div[@id='content_top']/div[@class='productDetail']/div[2]/div[@class='contentRight']/div[@class='productNameMain']/div[@class='productName']/span/h1/text()").extract()
			if "".join (title).strip () == "":
				title = hxs.select ("//div[@id='content_top']/div[@class='productDetail']/div[3]/div[@class='contentRight']/div[@class='productNameMain']/div[@class='productName']/span/h1/text()").extract()
			if "".join (title).strip () == "":
				title = hxs.select ("//div[@id='content']/div[@id='content_top']/div[@class='productDetail']/div[@class='contentRight']/div[@class='productNameMain']/div[@class='productName']/text()").extract()
			if not title:
				title = hxs.select ('//form[@id="product_addtocart_form"]/div[@class="head clearfix"]/h1/text()').extract()
			if not title:
				title = hxs.select ('//form[@id="product_addtocart_form"]/div[@class="productNameMain"]/div[@class="productName"]/h1/text()').extract()
			if not title:
				title = hxs.select ("//div[@id='content']/div[@id='content_top']/div[@class='productDetail']/div[2]/div[@class='contentRight']/div[@class='productNameMain']/div[@class='productName']/span/text()").extract()
			if not title:
				title = hxs.select ("//div[@class='productDetail']/div/div[@class='contentRight']/div[@class='productNameMain']/div[@class='productName']/span/text()").extract()
			if "".join (title).strip () == "":
				title = hxs.select ("//div[@id='content']/div[@id='content_top']/div[@class='productDetail']/div/div[@class='contentRight']/div[@class='productNameMain']/div[@class='productName']/span/text()").extract()
			if "".join (title).strip () == "":
				title = hxs.select ("//div[@class='productName']/span/text()").extract()
			if "".join (title).strip () != "":
				for t in title:
					item['partner_title'] = t.strip ()
			else:
				item['partner_title'] = 'Not Found' 
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select ("//div[@id='content']/div[@id='content_top']/div[@class='productDetail']/div[2]/div[@class='contentRight']/div[@class='productNameMain']/div[2]/div[@class='productPrice']/span[@id='current_product_price']/text()").extract()
			if not price:
				price = hxs.select ("//div[@id='content']/div[@id='content_top']/div[@class='productDetail']/div[@class='contentRight']/div[@class='productNameMain']/div[@class='productPrice']/span[@id='current_product_price']/text()").extract()
			if not price:
				price = hxs.select ("//div[@class='productDetail']/div/div[@class='contentRight']/div[@class='productNameMain']/div/div[@class='productPrice']/span[@id='current_product_price']/text()").extract()
			if not price:
				price = hxs.select ('//form[@id="product_addtocart_form"]/div[@class="detBox"]/p/span[@id="zooming"]/span[@id="totalPriceTextBox"]/text()').extract()
			if not price:
				price = hxs.select ('//span[@class="grey777"]/text()').extract()
			if not price:
				price = hxs.select ('//form[@id="product_addtocart_form"]/div[@class="productNameMain"]/div[@id="conf-price1"]/div[@class="productPrice"]/span[@id="totalPriceTextBox"]/text()').extract()
			if not price:
				price = hxs.select ('//form[@id="product_addtocart_form"]/div[@class="productNameMain"]/div[@class="productPrice"]/span[@id="totalPriceTextBox"]/text()').extract()
			if not price:
				price = hxs.select ('//form[@id="product_addtocart_form"]/div[@class="productNameMain"]/div[@class="productPrice"]/span[2]/text()').extract()
			if not price:
				price = hxs.select ("//span[@id='current_product_price']/text()").extract()
			if price:
				item['partner_price'] = price[0].strip().replace (',', '').partition ('.')[0]
			else:
				item['partner_price'] = 0 
			items.append (item)
			return items
		except:
			pass

class Purp_Spider (BaseSpider):
	name = 'Purp' 
	allowed_domains =['www.purplle.com'] 
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'purplle.com':
				for j in range(len(data[i]['purplle.com'])):
					li.append(data[i]['purplle.com'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem ()
			hxs = HtmlXPathSelector (response)
			item['site'] = 'purplle.com'
			item['partner_url'] = response.url
			title = hxs.select ('//div[@class="product-essential"]/div[@class="product-shop"]/h2/text()').extract()
			if title:
				item['partner_title'] = title[0]
			else:
				item['partner_title'] = 'Not Found'
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select ('//div[@class="product-essential"]/div[@class="product-shop"]/span[@class="price-box"]/font/text()').extract()
			if price:
				for i in price:
					l = i.split()
					prc =[int (s) for s in l if s.isdigit ()]
					if prc:
						item['partner_price'] = prc[0]
			else:
				item['partner_price'] = 0
			item['partner_price'] = str(item['partner_price'])
			items.append (item)
			return items 
		except:
			pass 

class Fabf_Spider (BaseSpider):
	name = 'Fabf'
	allowed_domains =['www.fabfurnish.com']
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'fabfurnish.com':
				for j in range(len(data[i]['fabfurnish.com'])):
					li.append(data[i]['fabfurnish.com'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem()
			hxs = HtmlXPathSelector (response)
			item['site'] = 'fabfurnish.com'
			item['partner_url'] = response.url
			title = hxs.select ('//h1[@class="prd-title-new"]/text()').extract ()
			if title:
				item['partner_title'] = title[0]
			else:
				item['partner_title'] = 'Not Found' 
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select ('//div[@class="special_price"]/span[@id="special_price_box"]/span[@id="product_special_price"]/text()').extract()
			if not price:
				price = hxs.select ('//span[@id="price_box"]/text()').extract()
			if not price:
				price = hxs.select ('//span[@id="price_box"]/span/text()').extract ()
			if price:
				item['partner_price'] = price[0].replace (",", "")
			else:
				item['partner_price'] = 0
			items.append (item)
			return items 
		except:
			pass

class Zansaar_Spider (BaseSpider):
	name = 'Zansaar' 
	allowed_domains =['www.zansaar.com'] 
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'zansaar.com':
				for j in range(len(data[i]['zansaar.com'])):
					li.append(data[i]['zansaar.com'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem ()
			hxs = HtmlXPathSelector (response)
			item['site'] = 'zansaar.com' 
			item['partner_url'] = response.url
			title = hxs.select ('//h1[@id="pdp_title"]/text()').extract()
			if title:
				item['partner_title'] = title[0]
			else:
				item['partner_title'] = 'Not Found'
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select ('//section[@id="pricesection"]/h2/strong/span[2]/text()').extract()
			if price:
				pr = price[0].replace (" ", "")
				prc = pr.replace (",", "") 
				item['partner_price'] = prc
			else:
				item['partner_price'] = 0
			items.append (item)
			return items
		except:
			pass

class Shop19_Spider (BaseSpider):
	name = 'Shop19'
	allowed_domains =['www.shopnineteen.com'] 
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'shopnineteen.com':
				for j in range(len(data[i]['shopnineteen.com'])):
					li.append(data[i]['shopnineteen.com'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem ()
			hxs = HtmlXPathSelector (response) 
			item['site'] = 'shopnineteen.com' 
			item['partner_url'] = response.url
			title = hxs.select ('//div[@class="product-name"]/h1/text()').extract()
			if title:
				item['partner_title'] = title[0]
			else:
				item['partner_title'] = 'Not Found' 
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select ('//div[@class="price-box"]/span/span[@class="price"]/text()').extract()
			if not price:
				price = hxs.select ('//div[@class="price-box"]/p[@class="special-price"]/span[@class="price"]/text()').extract()
			if not price:
				price = hxs.select ('//div[@class="col-main"]/div[@class="product-last f-right"]/div[1]/text()').extract()
			if price:
				pr = price[0].replace ("Rs. ", "")
				pr2 = pr.replace ("Rs ", "") 
				pr3 = pr2.replace (",", "") 
				prc = pr.replace (",", "") 
				prc = pr3.replace ("/-", "") 
				item['partner_price'] = str (prc)
			else:
				item['partner_price'] = 0 
			if price:
				if "sold out" in str (price[0].lower ()):
					item['partner_price'] = 0 
			item['partner_price'] = item['partner_price'].strip()
			items.append (item) 
			return items 
		except:
			pass

class Engrave_Spider (BaseSpider):
	name = 'Engrave' 
	allowed_domains =['www.engrave.in'] 
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'engrave.in':
				for j in range(len(data[i]['engrave.in'])):
					li.append(data[i]['engrave.in'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem ()
			hxs = HtmlXPathSelector (response) 
			item['site'] = 'engrave.in' 
			item['partner_url'] = response.url
			title = hxs.select ('//body/div[@id="content"]/h1/text()').extract()
			if not title:
				title = hxs.select ('//div[@id="wrapper"]/div[@id="content"]/div/h1/text()').extract()
			if not title:
				title = hxs.select ('//div[@class="description"]/div[@class="prodinfo"]/span/text()').extract()
			if title:
				if not 'Brand' in title[0]:
					item['partner_title'] = title[0]
				else:
					item['partner_title'] = 'Not Found'
			else:
				item['partner_title'] = 'Not Found' 
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select ('//dl[@id="product-price"]/dd/span[@class="price selling"]/text()').extract()
			if not price:
				price = hxs.select ('//div[@class="prodprice"]/div[@class="price-new"]/text()').extract()
			if not price:
				price = hxs.select ('//div[@class="prodprice"]/div[@class="price-new"]/text()').extract ()
			if price:
				pr = price[0].replace ("Rs. ", "").replace ("Rs.", "") 
				pr2 = pr.replace ("Rs ", "") 
				prc = pr2.replace (",", "") 
				item['partner_price'] = prc
			else:
				item['partner_price'] = 0 
			items.append (item) 
			return items 
		except:
			pass

class Carat_Spider (BaseSpider):
	name = 'Carat' 
	allowed_domains =['www.caratlane.com'] 
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'caratlane.com':
				for j in range(len(data[i]['caratlane.com'])):
					li.append(data[i]['caratlane.com'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem ()
			hxs = HtmlXPathSelector (response) 
			item['site'] = 'caratlane.com' 
			item['partner_url'] = response.url
			title = hxs.select ('//form[@id="product_addtocart_form"]/div[@class="metroDiamondR"]/h2/text()').extract()
			if title:
				item['partner_title'] = title[0]
			else:
				item['partner_title'] = 'Not Found' 
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select ("//form[@id='product_addtocart_form']/div[@class='metroDiamondR']/div[@class='product-a2c-prc']/h4/span/span[@class='custom-offer']/span/text()").extract()
			if not price:
				price = hxs.select ('//form[@id="product_addtocart_form"]/div[@class="metroDiamondR"]/div[@class="product-a2c-prc"]/h4/span/span/text()').extract()
			if not price:
				price = hxs.select ("//span[@class='custom-offer']/span[@class='offer_price']/text()").extract()
			if not price:
				price = hxs.select ("//span[@class='pro-price']/text()").extract()
			if not price:
				price = hxs.select ("//div[@class='metroDiamondR']/div[@class='product-a2c-prc']/h4/span/span").extract()
			item['partner_price'] = 0 
			if price:
				for a in price:
					b = a.strip ().split()
					for x in b:
						prc = x.replace("Rs. ", "").replace (",", "").split (".")[0]
						if prc.isdigit():
							item['partner_price'] = prc 
			items.append(item) 
			return items 
		except:
			pass 

class ToduGiftSpider (BaseSpider):
	name = 'Todu' 
	allowed_domains =['www.todugift.com'] 
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'todugift.com':
				for j in range(len(data[i]['todugift.com'])):
					li.append(data[i]['todugift.com'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem ()
			hxs = HtmlXPathSelector (response) 
			item['site'] = 'todugift.com' 
			item['partner_url'] = response.url
			title = hxs.select ("//div[@id='description']/h2/text()").extract()
			if not title:
				title = hxs.select ("//div[@id='productName']/font/text()").extract()
			if title:
				item['partner_title'] = title[0]
			else:
				item['partner_title'] = 'Not Found' 
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select ("//h2[@id='productPrices']/text()").extract()
			if price:
				p = price[0].strip().replace ("Your Price: Rs.", '').replace ("/-", '').replace (",", '')
				item['partner_price'] = p
			else:
				item['partner_price'] = 0 
			items.append(item)
			return items 
		except:
			pass 

class HitPlaySpider (BaseSpider):
	name = 'Hit' 
	allowed_domains =['www.hitplay.in'] 
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'hitplay.in':
				for j in range(len(data[i]['hitplay.in'])):
					li.append(data[i]['hitplay.in'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem ()
			hxs = HtmlXPathSelector (response) 
			item['site'] = 'hitplay.in' 
			item['partner_url'] = response.url
			title = hxs.select ("//form[@id='frmcart']/table/tr[2]/td[@class='product_name']/text()").extract()
			if title:
				item['partner_title'] = title[0]
			else:
				item['partner_title'] = 'Not Found' 
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select ("//form[@id='frmcart']/table/tr[5]/td/table/tr[2]/td[@class='price']/text()").extract()
			if price:
				p = price[0] 
				item['partner_price'] = p.replace("Rs.", "").split(".")[0].strip().replace (",", "")
			else:
				item['partner_price'] = 0 
			items.append (item) 
			return items 
		except:
			pass 

class LimeroadSpider (BaseSpider):
	name = 'Limeroad' 
	allowed_domains =['www.limeroad.com'] 
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'limeroad.com':
				for j in range(len(data[i]['limeroad.com'])):
					li.append(data[i]['limeroad.com'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem ()
			hxs = HtmlXPathSelector (response) 
			item['site'] = 'limeroad.com' 
			item['partner_url'] = response.url
			title = hxs.select ("//div[@id='product-overlay']/div[@class='row-fluid product-hdr-container']/div[@class='span12 display-table pull-left product-hdr pos-rel']/div[@class='row-fluid']/ul[@class='display-table-cell span9 margin0']/li/h1[@class='margin0']/span[@class='p_name']/text()").extract()
			if title:
				item['partner_title'] = title[0].strip()
			else:
				item['partner_title'] = 'Not Found' 
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select ("//div[@id='productDetails']/ul[@class='details']/li[@class='priceData']/p[@class='price']/text()").extract()

			if not price:
				price = hxs.select ("//div[@id='productDetails']/ul[@class='details']/li[@class='priceData']/p[@class='price sPrice']/text()").extract()
			if price and not price[0].strip () == "":
				item['partner_price'] = price[0].replace ("Rs.", "").strip ()
			else:
				item['partner_price'] = 0 
			items.append (item) 
			return items 
		except:
			pass 

class PerficoSpider (BaseSpider):
	name = 'Perfico' 
	allowed_domains =['www.perfico.com'] 
	li = []
	for i in range (len(data)):
		for key in data[i].keys():
			if key == 'perfico.com':
				for j in range(len(data[i]['perfico.com'])):
					li.append(data[i]['perfico.com'][j]['partner_url'])
	start_urls = li

	def parse (self, response):
		try:
			items =[]
			item = ScrapycrawlItem ()
			hxs = HtmlXPathSelector (response) 
			item['site'] = 'perfico.com' 
			item['partner_url'] = response.url
			title = hxs.select ("//div[@id='content-box']/div[@id='product_details_right']/div[@id='product_details_main']/div[@class='product_name']/h1/text()").extract()

			if title:
				item['partner_title'] = title[0]
			else:
				item['partner_title'] = 'Not Found' 
			item['partner_title'] = item['partner_title'].lower()
			price = hxs.select ("//div[@id='content-box']/div[@id='product_details_right']/div[@id='product_details_main']/div[@class='productdetails_box']/div[@class='row'][1]/div[@id='pr_mrp']/text()").extract()
			if price and not price[0].strip () == "":
				item['partner_price'] = price[0].replace("INR", "").split(".")[0].strip()
			else:
				item['partner_price'] = 0 
			items.append(item) 
			return items 
		except:
			pass
