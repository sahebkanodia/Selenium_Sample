'''
CHECKING THE SUBSCRIBE BUTTON IN REDIRECT PAGE. ALSO CROSS CHECKING PRICE, NAME WITH PARTNER SITE.

'''
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest, json
import random
import urllib2
import requests
import time
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1366, 768))
display.start()
log = open("error_9links.txt", 'a+')
file1 = open('data.jl', 'a')

PrPage = ""

p = {}
prt = ""

def check_ResponseCode(link):
	r = requests.get(link)
	if r.status_code != 200:
		print r.status_code
		print "Status Code Not OK, Please Check Error Logs!"
		log.write(str(link) + "[NOT OK]")
	else:
		print r.status_code
	return r.status_code

def convert_url(link):
	link = urllib2.unquote(link.decode("utf8"))
	link = link.split("url=")[-1]
	print link
	return link		

class root (unittest.TestCase):
	
	ff = webdriver.FirefoxProfile("/home/selenium_testing/firefox_test/FirefoxProfile")
	driver = webdriver.Firefox (ff)
	driver.implicitly_wait(30)
	driver.set_window_size(1366, 768)
	driver.maximize_window()
	driver.delete_all_cookies()
	driver.get ("http://www.wishpicker.com/office")

	driver.maximize_window()
	d = []

	def begin_flipkart(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for flipkart.com ..."
		search.send_keys("flipkart.com")
		global prt
		prt = 'flipkart.com'
		search.send_keys(Keys.RETURN)

	def begin_delightgifts(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for delightgifts.in ..."
		search.send_keys("delightgifts.in")
		global prt
		prt = 'delightgifts.in'
		search.send_keys(Keys.RETURN)

		
	def begin_engrave(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for engrave.in ..."
		search.send_keys("engrave.in")
		global prt
		prt = 'engrave.in'
		search.send_keys(Keys.RETURN)


	def begin_inonit(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for inonit.in ..."
		search.send_keys("inonit.in")
		global prt
		prt = 'inonit.in'
		search.send_keys(Keys.RETURN)
		
	def begin_happilyunmarried(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for happilyunmarried.com ..."
		search.send_keys("happilyunmarried.com")
		global prt
		prt = 'happilyunmarried.com'
		search.send_keys(Keys.RETURN)
		
	def begin_healthkart(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for healthkart.com ..."
		search.send_keys("healthkart.com")
		global prt
		prt = 'healthkart.com'
		search.send_keys(Keys.RETURN)
		
	def begin_dezains(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for dezains.com ..."
		search.send_keys("dezains.com")
		global prt
		prt = 'dezains.com'
		search.send_keys(Keys.RETURN)

	def begin_fnp(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for fnp.com ..."
		search.send_keys("fnp.com")
		global prt
		prt = 'fnp.com'
		search.send_keys(Keys.RETURN)

	def begin_vouchersmate(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for vouchersmate.com ..."
		search.send_keys("vouchersmate.com")
		global prt
		prt = 'vouchersmate.com'
		search.send_keys(Keys.RETURN)

	def begin_excitinglives(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for excitinglives.com ..."
		search.send_keys("excitinglives.com")
		global prt
		prt = 'excitinglives.com'
		search.send_keys(Keys.RETURN)

	def begin_babyoye(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for babyoye.com ..."
		search.send_keys("babyoye.com")
		global prt
		prt = 'babyoye.com'
		search.send_keys(Keys.RETURN)

	def begin_purplle(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for purplle.com ..."
		search.send_keys("purplle.com")
		global prt
		prt = 'purplle.com'
		search.send_keys(Keys.RETURN)

	def begin_fabfurnish(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for fabfurnish.com ..."
		search.send_keys("fabfurnish.com")
		global prt
		prt = 'fabfurnish.com'
		search.send_keys(Keys.RETURN)

	def begin_zansaar(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for zansaar.com ..."
		search.send_keys("zansaar.com")
		global prt
		prt = 'zansaar.com'
		search.send_keys(Keys.RETURN)


	def begin_shopnineteen(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for shopnineteen.com ..."
		search.send_keys("shopnineteen.com")
		global prt
		prt = 'shopnineteen.com'
		search.send_keys(Keys.RETURN)


	def begin_caratlane(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for caratlane.com ..."
		search.send_keys("caratlane.com")
		global prt
		prt = 'caratlane.com'
		search.send_keys(Keys.RETURN)


	def begin_todugift(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for todugift.com ..."
		search.send_keys("todugift.com")
		global prt
		prt = 'todugift.com'
		search.send_keys(Keys.RETURN)


	def begin_hitplay(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for hitplay.in ..."
		search.send_keys("hitplay.in")
		global prt
		prt = 'hitplay.in'
		search.send_keys(Keys.RETURN)


	def begin_perfico(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for perfico.com ..."
		search.send_keys("perfico.com")
		global prt
		prt = 'perfico.com'
		search.send_keys(Keys.RETURN)

	def begin_limeroad(self):
		driver = self.driver
		driver.delete_all_cookies()
		driver.get ("http://www.wishpicker.com/office")
		print "Opening Wishpicker ..."
		self.driver.get ("http://www.wishpicker.com/gifts-for")
		search = self.driver.find_element_by_name("q")
		print "Searching for limeroad.com ..."
		search.send_keys("limeroad.com")
		global prt
		prt = 'limeroad.com'
		search.send_keys(Keys.RETURN)
		
	def get_product(self):
		elem_f = self.driver.find_elements_by_class_name ("disable-click")
		rand = []

		WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, "check1")))

		elem_f = self.driver.find_elements_by_class_name ("disable-click")
		each_elem = random.choice(elem_f)
		linkstr = each_elem.get_attribute("href")
		print linkstr
		each_elem.click()


	def FRAME_BuyNow(self):
		#LINK1 - FRAME -BUY NOW
		driver = self.driver
		print "FRAME -BUY NOW"
		link1 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buy-Now")))
		link1.click()
		time.sleep(1)
		try:
			handle = driver.window_handles
			new_window = driver.switch_to_window(handle[1])
			try:
				url = driver.current_url
				self.assertIn("www.wishpicker.com/redirect/", url)
			except AssertionError:
				driver.close()
				handle = driver.window_handles
				org_window = driver.switch_to_window(handle[0])
				raise AssertionError("Error! Redirected to the wrong page.")
			stop_load = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "id_emailaddress")))
			stop_load.click()
			time.sleep(2)
			url = self.driver.current_url
			try:
				self.assertIn("www.wishpicker.com/redirect/", url)
			except AssertionError:
				driver.close()
				handle = driver.window_handles
				org_window = driver.switch_to_window(handle[0])
				raise AssertionError("Error! Page redirects on submitting wrong url!")
			if ('www.wishpicker.com/redirect/' in url):
				print "Page stops loading on Clicking [ OK ]"
				emailBox = self.driver.find_element_by_id("id_emailaddress")
				emailBox.send_keys("dnkjvf@")
				submit = self.driver.find_element_by_id("btn_email")
				submit.click()
				time.sleep(2)
				url = self.driver.current_url
				try:
					self.assertIn("www.wishpicker.com/redirect/", url)
				except AssertionError:
					driver.close()
					handle = driver.window_handles
					org_window = driver.switch_to_window(handle[0])
					raise AssertionError("Error! Page redirects on submitting wrong Email format!")
				emailBox = self.driver.find_element_by_id("id_emailaddress")
				emailBox.clear()
				emailBox.send_keys("wishpicker.test@outlook.com")
				submit = self.driver.find_element_by_id("btn_email")
				submit.click()
				time.sleep(3)
				url = self.driver.current_url
				try:
					self.assertNotIn("www.wishpicker.com/redirect/", url)
				except AssertionError:
					driver.close()
					org_window = driver.switch_to_window(handle[0])
					raise AssertionError("Error! Page does not redirects on submitting correct Email format!")
				r = requests.get(url)
				try:
					self.assertEqual(r.status_code, 200)
				except AssertionError:
					driver.close()
					handle = driver.window_handles
					org_window = driver.switch_to_window(handle[0])
					raise AssertionError("Response code not equal 200.")
		except TimeoutException:
			driver.close()
			handle = driver.window_handles
			org_window = driver.switch_to_window(handle[0])
			raise
		driver.close()
		handle = driver.window_handles
		org_window = driver.switch_to_window(handle[0])

	def ProductPage_BuyNow(self):
		#LINK5 - PRODUCT PAGE -BUY NOW
		print "PRODUCT PAGE -BUY NOW"
		pdt_name = ''
		price = ''
		r = {}
		driver = self.driver
		PPurl = driver.current_url
		global PrPage
		PrPage = driver.current_url
		driver.delete_all_cookies()
		driver.get("http://www.wishpicker.com/office")
		driver.get(PPurl)
		r['prPage'] = PPurl
		try:
			pdt_name = self.driver.find_element_by_xpath ("//h1[@id='modal_id']").text
			pdt_name = pdt_name.lower()
			r['our_name'] = pdt_name
			price = self.driver.find_element_by_xpath ("//span[@itemprop='price']").text
			r['our_price'] = price
		except NoSuchElementException:
			raise NoSuchElementException("Error! Could not extract data from product page.")
		link5 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "buyNow")))
		link5.click()
		time.sleep(1)

		handle = driver.window_handles
		new_window = driver.switch_to_window(handle[1])
		try:
			stop_load = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "id_emailaddress")))
			stop_load.click()
			time.sleep(2)
			url = self.driver.current_url
			try:
				self.assertIn("www.wishpicker.com/redirect/", url)
			except AssertionError:
				driver.close()
				handle = driver.window_handles
				org_window = driver.switch_to_window(handle[0])
				raise AssertionError("Error! Page redirects on submitting wrong url!")

			if ('www.wishpicker.com/redirect/' in url):
				print "Page stops loading on Clicking [ OK ]"
				emailBox = self.driver.find_element_by_id("id_emailaddress")
				emailBox.send_keys("dnkjvf@")
				submit = self.driver.find_element_by_id("btn_email")
				submit.click()
				time.sleep(2)
				url = self.driver.current_url
				try:
					self.assertIn("www.wishpicker.com/redirect/", url)
				except AssertionError:
					driver.close()
					handle = driver.window_handles
					org_window = driver.switch_to_window(handle[0])
					raise AssertionError("Error! Page redirects on submitting wrong Email format!")
				emailBox = self.driver.find_element_by_id("id_emailaddress")
				emailBox.clear()
				emailBox.send_keys("wishpicker.test@outlook.com")
				submit = self.driver.find_element_by_id("btn_email")
				submit.click()
				time.sleep(5)
				url = self.driver.current_url
				try:
					self.assertNotIn("www.wishpicker.com/redirect/", url)
				except AssertionError:
					driver.close()
					handle = driver.window_handles
					org_window = driver.switch_to_window(handle[0])
					raise AssertionError("Error! Page does not redirects on submitting correct Email format!")
				s = requests.get(url)
				try:
					self.assertEqual(s.status_code, 200)
				except AssertionError:
					driver.close()
					handle = driver.window_handles
					org_window = driver.switch_to_window(handle[0])
					raise AssertionError("Response code not equal 200.")
		except TimeoutException:
			driver.close()
			handle = driver.window_handles
			org_window = driver.switch_to_window(handle[0])
			raise
		url = driver.current_url
		r['partner_url'] = str(url)
		driver.close()
		handle = driver.window_handles
		org_window = driver.switch_to_window(handle[0])
		self.d.append(r)

	def ShortListPage_BuyNow(self):
		#SHORTLIST PAGE LINKS
		driver = self.driver
		global PrPage
		driver.delete_all_cookies()
		driver.get("http://www.wishpicker.com/office")
		driver.get(PrPage)
		WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "divID")))
		shortlist_item = driver.find_element_by_id("divID")
		shortlist_item.click()
		time.sleep(1)
		WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "ql_ListElementCancel")))
		driver.get("http://www.wishpicker.com/shortlist")

		#LINK9 - SHORT LIST - BUY NOW
		print "SHORTLIST PAGE - BUY NOW"
		link7 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "buyNow")))
		link7.click()
		time.sleep(1)
		try:
			handle = driver.window_handles
			new_window = driver.switch_to_window(handle[1])
			stop_load = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "id_emailaddress")))
			stop_load.click()
			time.sleep(2)
			url = self.driver.current_url
			try:
				self.assertIn("www.wishpicker.com/redirect/", url)
			except AssertionError:
				driver.close()
				handle = driver.window_handles
				org_window = driver.switch_to_window(handle[0])
				time.sleep(1)
				driver.get('http://www.wishpicker.com/shortlist')
				rem_srt = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "modal_remove")))
				rem_srt.click()
				time.sleep(1)
				raise AssertionError("Error! Page redirects on submitting wrong url!")
			if ('www.wishpicker.com/redirect/' in url):
				emailBox = self.driver.find_element_by_id("id_emailaddress")
				emailBox.click()
				emailBox.send_keys("dnkjvf@")
				submit = self.driver.find_element_by_id("btn_email")
				submit.click()
				time.sleep(2)
				url = self.driver.current_url
				try:
					self.assertIn("www.wishpicker.com/redirect/", url)
				except AssertionError:
					driver.close()
					handle = driver.window_handles
					org_window = driver.switch_to_window(handle[0])
					time.sleep(1)
					driver.get('http://www.wishpicker.com/shortlist')
					rem_srt = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "modal_remove")))
					rem_srt.click()
					time.sleep(1)
					raise AssertionError("Error! Page redirects on submitting wrong Email format!")
				emailBox = self.driver.find_element_by_id("id_emailaddress")
				emailBox.clear()
				emailBox.send_keys("wishpicker.test@outlook.com")
				submit = self.driver.find_element_by_id("btn_email")
				submit.click()
				time.sleep(5)
				url = self.driver.current_url
				try:
					self.assertNotIn("www.wishpicker.com/redirect/", url)
				except AssertionError:
					driver.close()
					handle = driver.window_handles
					org_window = driver.switch_to_window(handle[0])
					time.sleep(1)
					driver.get('http://www.wishpicker.com/shortlist')
					rem_srt = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "modal_remove")))
					rem_srt.click()
					time.sleep(1)
					raise AssertionError("Error! Page does not redirects on submitting correct Email format!")
				r = requests.get(url)
				try:
					self.assertEqual(r.status_code, 200)
				except AssertionError:
					driver.close()
					handle = driver.window_handles
					org_window = driver.switch_to_window(handle[0])
					time.sleep(1)
					driver.get('http://www.wishpicker.com/shortlist')
					rem_srt = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "modal_remove")))
					rem_srt.click()
					time.sleep(1)
					raise AssertionError("Response code not equal 200.")
		except:	
			driver.close()
			handle = driver.window_handles
			org_window = driver.switch_to_window(handle[0])
			raise
		driver.close()
		handle = driver.window_handles
		org_window = driver.switch_to_window(handle[0])
		time.sleep(1)
		driver.get('http://www.wishpicker.com/shortlist')
		rem_srt = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "modal_remove")))
		rem_srt.click()
		time.sleep(1)

	def reset(self):
		global p, prt
		p[prt] = self.d
		line = json.dumps(p) + ","
		file1.write(line)
		del self.d[:]
		p.clear()

	def quit(self):
		self.driver.quit()
		display.stop()

if __name__ == '__main__':
	unittest.main()
