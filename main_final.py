import unittest
import time
import HTMLTestRunner
from test2 import Flipkart, Delightgifts, Engrave, Dezains, Fnp, Fabfurnish, Excitinglives, Babyoye, Caratlane, Inonit, Happilyunmarried, Healthkart, Vouchersmate, Purplle, Zansaar, Shopnineteen, Todugift, Hitplay, Perfico, Limeroad

log = open("error_9links.txt", 'a+')

i = -1

'''
FLIPKART.COM
'''

class flipkart (Flipkart):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

flipkartTest = unittest.TestSuite()
for v in range (3):
	flipkartTest.addTest(flipkart('test_a_title'))
	flipkartTest.addTest(flipkart('test_b_price'))
flipkartTest.addTest(flipkart('test_c_reset'))

class delightgifts (Delightgifts):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

delightgiftsTest = unittest.TestSuite()
for v in range (3):
	delightgiftsTest.addTest(delightgifts('test_a_title'))
	delightgiftsTest.addTest(delightgifts('test_b_price'))
delightgiftsTest.addTest(delightgifts('test_c_reset'))


class engrave (Engrave):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

engraveTest = unittest.TestSuite()
for v in range (3):
	engraveTest.addTest(engrave('test_a_title'))
	engraveTest.addTest(engrave('test_b_price'))
engraveTest.addTest(engrave('test_c_reset'))



class inonit (Inonit):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

inonitTest = unittest.TestSuite()
for v in range (3):
	inonitTest.addTest(inonit('test_a_title'))
	inonitTest.addTest(inonit('test_b_price'))
inonitTest.addTest(inonit('test_c_reset'))



class dezains (Dezains):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

dezainsTest = unittest.TestSuite()
for v in range (3):
	dezainsTest.addTest(dezains('test_a_title'))
	dezainsTest.addTest(dezains('test_b_price'))
dezainsTest.addTest(dezains('test_c_reset'))


class fnp (Fnp):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

fnpTest = unittest.TestSuite()
for v in range (3):
	fnpTest.addTest(fnp('test_a_title'))
	fnpTest.addTest(fnp('test_b_price'))
fnpTest.addTest(fnp('test_c_reset'))



class excitinglives (Excitinglives):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

excitinglivesTest = unittest.TestSuite()
for v in range (3):
	excitinglivesTest.addTest(excitinglives('test_a_title'))
	excitinglivesTest.addTest(excitinglives('test_b_price'))
excitinglivesTest.addTest(excitinglives('test_c_reset'))


class happilyunmarried (Happilyunmarried):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

happilyunmarriedTest = unittest.TestSuite()
for v in range (3):
	happilyunmarriedTest.addTest(happilyunmarried('test_a_title'))
	happilyunmarriedTest.addTest(happilyunmarried('test_b_price'))
happilyunmarriedTest.addTest(happilyunmarried('test_c_reset'))




class healthkart (Healthkart):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

healthkartTest = unittest.TestSuite()
for v in range (3):
	healthkartTest.addTest(healthkart('test_a_title'))
	healthkartTest.addTest(healthkart('test_b_price'))
healthkartTest.addTest(healthkart('test_c_reset'))



class vouchersmate (Vouchersmate):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

vouchersmateTest = unittest.TestSuite()
for v in range (3):
	vouchersmateTest.addTest(vouchersmate('test_a_title'))
	vouchersmateTest.addTest(vouchersmate('test_b_price'))
vouchersmateTest.addTest(vouchersmate('test_c_reset'))



class babyoye (Babyoye):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

babyoyeTest = unittest.TestSuite()
for v in range (3):
	babyoyeTest.addTest(babyoye('test_a_title'))
	babyoyeTest.addTest(babyoye('test_b_price'))
babyoyeTest.addTest(babyoye('test_c_reset'))



class purplle (Purplle):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

purplleTest = unittest.TestSuite()
for v in range (3):
	purplleTest.addTest(purplle('test_a_title'))
	purplleTest.addTest(purplle('test_b_price'))
purplleTest.addTest(purplle('test_c_reset'))



class fabfurnish (Fabfurnish):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

fabfurnishTest = unittest.TestSuite()
for v in range (3):
	fabfurnishTest.addTest(fabfurnish('test_a_title'))
	fabfurnishTest.addTest(fabfurnish('test_b_price'))
fabfurnishTest.addTest(fabfurnish('test_c_reset'))



class zansaar (Zansaar):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

zansaarTest = unittest.TestSuite()
for v in range (3):
	zansaarTest.addTest(zansaar('test_a_title'))
	zansaarTest.addTest(zansaar('test_b_price'))
zansaarTest.addTest(zansaar('test_c_reset'))




class shopnineteen (Shopnineteen):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

shopnineteenTest = unittest.TestSuite()
for v in range (3):
	shopnineteenTest.addTest(shopnineteen('test_a_title'))
	shopnineteenTest.addTest(shopnineteen('test_b_price'))
shopnineteenTest.addTest(shopnineteen('test_c_reset'))



class caratlane (Caratlane):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

caratlaneTest = unittest.TestSuite()
for v in range (3):
	caratlaneTest.addTest(caratlane('test_a_title'))
	caratlaneTest.addTest(caratlane('test_b_price'))
caratlaneTest.addTest(caratlane('test_c_reset'))


class todugift (Todugift):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

todugiftTest = unittest.TestSuite()
for v in range (3):
	todugiftTest.addTest(todugift('test_a_title'))
	todugiftTest.addTest(todugift('test_b_price'))
todugiftTest.addTest(todugift('test_c_reset'))



class hitplay (Hitplay):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

hitplayTest = unittest.TestSuite()
for v in range (3):
	hitplayTest.addTest(hitplay('test_a_title'))
	hitplayTest.addTest(hitplay('test_b_price'))
hitplayTest.addTest(hitplay('test_c_reset'))




class perfico (Perfico):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

perficoTest = unittest.TestSuite()
for v in range (3):
	perficoTest.addTest(perfico('test_a_title'))
	perficoTest.addTest(perfico('test_b_price'))
perficoTest.addTest(perfico('test_c_reset'))




class limeroad (Limeroad):

	def test_a_title(self):
		global i
		i += 1
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.title(i)
						
	def test_b_price(self):
		global i
		print ">>>>>>>>>  " + str(i)
		time.sleep(1)
		self.price(i)

	def test_c_reset(self):
		global i
		i = -1
	

limeroadTest = unittest.TestSuite()
for v in range (3):
	limeroadTest.addTest(limeroad('test_a_title'))
	limeroadTest.addTest(limeroad('test_b_price'))
limeroadTest.addTest(limeroad('test_c_reset'))



all_tests = unittest.TestSuite([flipkartTest, delightgiftsTest, engraveTest, dezainsTest, fnpTest, fabfurnishTest, excitinglivesTest, babyoyeTest, caratlaneTest, inonitTest, happilyunmarriedTest, healthkartTest, vouchersmateTest, purplleTest, zansaarTest, shopnineteenTest, todugiftTest, hitplayTest, perficoTest, limeroadTest])

buf = file("TestReport" + ".html", 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=buf, title = 'Response Code From 9 Links of a product', description='Results on Browser : Firefox')

if __name__ == '__main__':

	runner.run(all_tests)
