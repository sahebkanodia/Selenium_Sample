'''
CHECKING THE SUBSCRIBE BUTTON IN REDIRECT PAGE. ALSO CROSS CHECKING PRICE, NAME WITH PARTNER SITE.

'''

import unittest
import HTMLTestRunner
from test import root

count = 0

'''
FLIPKART.COM
'''

class Flipkart (root):
	
	def test_a_beginFlipkart(self):
		self.begin_flipkart()
						
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	

	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	

	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	

	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()

flipkartTest = unittest.TestSuite()
for i in range (3):
	flipkartTest.addTest(Flipkart('test_a_beginFlipkart'))
	flipkartTest.addTest(Flipkart('test_b_getProduct'))		
	flipkartTest.addTest(Flipkart('test_c_FRAME_BuyNow'))
	flipkartTest.addTest(Flipkart('test_g_ProductPage_BuyNow'))
	flipkartTest.addTest(Flipkart('test_k_ShortListPage_BuyNow'))
flipkartTest.addTest(Flipkart('test_y_reset'))


'''
DELIGHTGIFTS.IN
'''

class DelightGifts (root):		
		
	def test_a_beginDelightgifts(self):
		self.begin_delightgifts()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	
	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


delightgiftsTest = unittest.TestSuite()
for i in range (3):
	delightgiftsTest.addTest(DelightGifts('test_a_beginDelightgifts'))
	delightgiftsTest.addTest(DelightGifts('test_b_getProduct'))		
	delightgiftsTest.addTest(DelightGifts('test_c_FRAME_BuyNow'))
	delightgiftsTest.addTest(DelightGifts('test_g_ProductPage_BuyNow'))
	delightgiftsTest.addTest(DelightGifts('test_k_ShortListPage_BuyNow'))
delightgiftsTest.addTest(DelightGifts('test_y_reset'))

'''
ENGARVE.IN

'''

class Engrave (root):		
		
	def test_a_beginEngrave(self):
		self.begin_engrave()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	
	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


engraveTest = unittest.TestSuite()
for i in range (3):
	engraveTest.addTest(Engrave('test_a_beginEngrave'))
	engraveTest.addTest(Engrave('test_b_getProduct'))		
	engraveTest.addTest(Engrave('test_c_FRAME_BuyNow'))
	engraveTest.addTest(Engrave('test_g_ProductPage_BuyNow'))
	engraveTest.addTest(Engrave('test_k_ShortListPage_BuyNow'))
engraveTest.addTest(Engrave('test_y_reset'))
engraveTest.addTest(Engrave('test_z_teardown'))

'''

INONIT.IN

'''

class Inonit (root):		
		
	def test_a_beginInonit(self):
		self.begin_inonit()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()

	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	
	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


inonitTest = unittest.TestSuite()
for i in range (3):
	inonitTest.addTest(Inonit('test_a_beginInonit'))
	inonitTest.addTest(Inonit('test_b_getProduct'))		
	inonitTest.addTest(Inonit('test_c_FRAME_BuyNow'))
	inonitTest.addTest(Inonit('test_g_ProductPage_BuyNow'))
	inonitTest.addTest(Inonit('test_k_ShortListPage_BuyNow'))
inonitTest.addTest(Inonit('test_y_reset'))



'''

#HAPPILYUNMARRIED.COM

'''

class HappilyUnmarried (root):		
		
	def test_a_beginHappilyUnmarried(self):
		self.begin_happilyunmarried()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()

	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


happilyunmarriedTest = unittest.TestSuite()
for i in range (3):
	happilyunmarriedTest.addTest(HappilyUnmarried('test_a_beginHappilyUnmarried'))
	happilyunmarriedTest.addTest(HappilyUnmarried('test_b_getProduct'))		
	happilyunmarriedTest.addTest(HappilyUnmarried('test_c_FRAME_BuyNow'))
	happilyunmarriedTest.addTest(HappilyUnmarried('test_g_ProductPage_BuyNow'))
	happilyunmarriedTest.addTest(HappilyUnmarried('test_k_ShortListPage_BuyNow'))
happilyunmarriedTest.addTest(HappilyUnmarried('test_y_reset'))


'''

#HEALTHKART.COM

'''

class Healthkart (root):		
		
	def test_a_beginHealthkart(self):
		self.begin_healthkart()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	

	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


healthkartTest = unittest.TestSuite()
for i in range (3):
	healthkartTest.addTest(Healthkart('test_a_beginHealthkart'))
	healthkartTest.addTest(Healthkart('test_b_getProduct'))		
	healthkartTest.addTest(Healthkart('test_c_FRAME_BuyNow'))
	healthkartTest.addTest(Healthkart('test_g_ProductPage_BuyNow'))
	healthkartTest.addTest(Healthkart('test_k_ShortListPage_BuyNow'))
healthkartTest.addTest(Healthkart('test_y_reset'))



'''

#DEZAINS.COM

'''

class Dezains (root):		
		
	def test_a_beginDezains(self):
		self.begin_dezains()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	
	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


dezainsTest = unittest.TestSuite()
for i in range (3):
	dezainsTest.addTest(Dezains('test_a_beginDezains'))
	dezainsTest.addTest(Dezains('test_b_getProduct'))		
	dezainsTest.addTest(Dezains('test_c_FRAME_BuyNow'))
	dezainsTest.addTest(Dezains('test_g_ProductPage_BuyNow'))
	dezainsTest.addTest(Dezains('test_k_ShortListPage_BuyNow'))
dezainsTest.addTest(Dezains('test_y_reset'))


'''

#FNP.COM

'''

class Fnp (root):		
		
	def test_a_beginFnp(self):
		self.begin_fnp()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	
	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


fnpTest = unittest.TestSuite()
for i in range (3):
	fnpTest.addTest(Fnp('test_a_beginFnp'))
	fnpTest.addTest(Fnp('test_b_getProduct'))		
	fnpTest.addTest(Fnp('test_c_FRAME_BuyNow'))
	fnpTest.addTest(Fnp('test_g_ProductPage_BuyNow'))
	fnpTest.addTest(Fnp('test_k_ShortListPage_BuyNow'))
fnpTest.addTest(Fnp('test_y_reset'))



'''

#VOUCHERSMATE.COM

'''

class Vouchersmate (root):		
		
	def test_a_beginVouchersmate(self):
		self.begin_vouchersmate()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	
	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


vouchersmateTest = unittest.TestSuite()
for i in range (3):
	vouchersmateTest.addTest(Vouchersmate('test_a_beginVouchersmate'))
	vouchersmateTest.addTest(Vouchersmate('test_b_getProduct'))		
	vouchersmateTest.addTest(Vouchersmate('test_c_FRAME_BuyNow'))
	vouchersmateTest.addTest(Vouchersmate('test_g_ProductPage_BuyNow'))
	vouchersmateTest.addTest(Vouchersmate('test_k_ShortListPage_BuyNow'))
vouchersmateTest.addTest(Vouchersmate('test_y_reset'))



'''

#EXCITINGLIVES.COM

'''

class ExcitingLives (root):		
		
	def test_a_beginExcitingLives(self):
		self.begin_excitinglives()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	

	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()

	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


excitinglivesTest = unittest.TestSuite()
for i in range (3):
	excitinglivesTest.addTest(ExcitingLives('test_a_beginExcitingLives'))
	excitinglivesTest.addTest(ExcitingLives('test_b_getProduct'))		
	excitinglivesTest.addTest(ExcitingLives('test_c_FRAME_BuyNow'))
	excitinglivesTest.addTest(ExcitingLives('test_g_ProductPage_BuyNow'))
	excitinglivesTest.addTest(ExcitingLives('test_k_ShortListPage_BuyNow'))
excitinglivesTest.addTest(ExcitingLives('test_y_reset'))



'''

#BABYOYE.COM

'''

class Babyoye (root):		
		
	def test_a_beginBabyoye(self):
		self.begin_babyoye()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	

	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()

	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


babyoyeTest = unittest.TestSuite()
for i in range (3):
	babyoyeTest.addTest(Babyoye('test_a_beginBabyoye'))
	babyoyeTest.addTest(Babyoye('test_b_getProduct'))		
	babyoyeTest.addTest(Babyoye('test_c_FRAME_BuyNow'))
	babyoyeTest.addTest(Babyoye('test_g_ProductPage_BuyNow'))
	babyoyeTest.addTest(Babyoye('test_k_ShortListPage_BuyNow'))
babyoyeTest.addTest(Babyoye('test_y_reset'))




'''

#PURPLLE.COM

'''

class Purplle (root):		
		
	def test_a_beginPurplle(self):
		self.begin_purplle()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	
	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


purplleTest = unittest.TestSuite()
for i in range (3):
	purplleTest.addTest(Purplle('test_a_beginPurplle'))
	purplleTest.addTest(Purplle('test_b_getProduct'))		
	purplleTest.addTest(Purplle('test_c_FRAME_BuyNow'))
	purplleTest.addTest(Purplle('test_g_ProductPage_BuyNow'))
	purplleTest.addTest(Purplle('test_k_ShortListPage_BuyNow'))
purplleTest.addTest(Purplle('test_y_reset'))



'''

#FABFURNISH.COM

'''

class Fabfurnish (root):		
		
	def test_a_beginFabfurnish(self):
		self.begin_fabfurnish()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	
	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


fabfurnishTest = unittest.TestSuite()
for i in range (3):
	fabfurnishTest.addTest(Fabfurnish('test_a_beginFabfurnish'))
	fabfurnishTest.addTest(Fabfurnish('test_b_getProduct'))		
	fabfurnishTest.addTest(Fabfurnish('test_c_FRAME_BuyNow'))
	fabfurnishTest.addTest(Fabfurnish('test_g_ProductPage_BuyNow'))
	fabfurnishTest.addTest(Fabfurnish('test_k_ShortListPage_BuyNow'))
fabfurnishTest.addTest(Fabfurnish('test_y_reset'))



'''

#ZANSAAR.COM

'''

class Zansaar (root):		
		
	def test_a_beginZansaar(self):
		self.begin_zansaar()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	
	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


zansaarTest = unittest.TestSuite()
for i in range (3):
	zansaarTest.addTest(Zansaar('test_a_beginZansaar'))
	zansaarTest.addTest(Zansaar('test_b_getProduct'))		
	zansaarTest.addTest(Zansaar('test_c_FRAME_BuyNow'))
	zansaarTest.addTest(Zansaar('test_g_ProductPage_BuyNow'))
	zansaarTest.addTest(Zansaar('test_k_ShortListPage_BuyNow'))
zansaarTest.addTest(Zansaar('test_y_reset'))


'''

#SHOPNINETEEN.COM

'''

class ShopNineteen (root):		
		
	def test_a_beginShopNineteen(self):
		self.begin_shopnineteen()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	
	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


shopnineteenTest = unittest.TestSuite()
for i in range (3):
	shopnineteenTest.addTest(ShopNineteen('test_a_beginShopNineteen'))
	shopnineteenTest.addTest(ShopNineteen('test_b_getProduct'))		
	shopnineteenTest.addTest(ShopNineteen('test_c_FRAME_BuyNow'))
	shopnineteenTest.addTest(ShopNineteen('test_g_ProductPage_BuyNow'))
	shopnineteenTest.addTest(ShopNineteen('test_k_ShortListPage_BuyNow'))
shopnineteenTest.addTest(ShopNineteen('test_y_reset'))


'''

#CARATLANE.COM

'''

class Caratlane (root):		
		
	def test_a_beginCaratlane(self):
		self.begin_caratlane()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()

	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


caratlaneTest = unittest.TestSuite()
for i in range (3):
	caratlaneTest.addTest(Caratlane('test_a_beginCaratlane'))
	caratlaneTest.addTest(Caratlane('test_b_getProduct'))		
	caratlaneTest.addTest(Caratlane('test_c_FRAME_BuyNow'))
	caratlaneTest.addTest(Caratlane('test_g_ProductPage_BuyNow'))
	caratlaneTest.addTest(Caratlane('test_k_ShortListPage_BuyNow'))
caratlaneTest.addTest(Caratlane('test_y_reset'))



'''

#TODUGIFT.COM

'''

class Todugift (root):		
		
	def test_a_beginTodugift(self):
		self.begin_todugift()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	
	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


todugiftTest = unittest.TestSuite()
for i in range (3):
	todugiftTest.addTest(Todugift('test_a_beginTodugift'))
	todugiftTest.addTest(Todugift('test_b_getProduct'))		
	todugiftTest.addTest(Todugift('test_c_FRAME_BuyNow'))
	todugiftTest.addTest(Todugift('test_g_ProductPage_BuyNow'))
	todugiftTest.addTest(Todugift('test_k_ShortListPage_BuyNow'))
todugiftTest.addTest(Todugift('test_y_reset'))



'''

#HITPLAY.IN

'''

class Hitplay (root):		
		
	def test_a_beginHitplay(self):
		self.begin_hitplay()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	
	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


hitplayTest = unittest.TestSuite()
for i in range (3):
	hitplayTest.addTest(Hitplay('test_a_beginHitplay'))
	hitplayTest.addTest(Hitplay('test_b_getProduct'))		
	hitplayTest.addTest(Hitplay('test_c_FRAME_BuyNow'))
	hitplayTest.addTest(Hitplay('test_g_ProductPage_BuyNow'))
	hitplayTest.addTest(Hitplay('test_k_ShortListPage_BuyNow'))
hitplayTest.addTest(Hitplay('test_y_reset'))


'''

#PERFICO.COM

'''

class Perfico (root):		
		
	def test_a_beginPerfico(self):
		self.begin_perfico()
				
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	
	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()


perficoTest = unittest.TestSuite()
for i in range (3):
	perficoTest.addTest(Perfico('test_a_beginPerfico'))
	perficoTest.addTest(Perfico('test_b_getProduct'))		
	perficoTest.addTest(Perfico('test_c_FRAME_BuyNow'))
	perficoTest.addTest(Perfico('test_g_ProductPage_BuyNow'))
	perficoTest.addTest(Perfico('test_k_ShortListPage_BuyNow'))
perficoTest.addTest(Perfico('test_y_reset'))


'''
#LIMEROAD.COM
'''

class Limeroad (root):
	
	def test_a_beginLimeroad(self):
		self.begin_limeroad()
						
	def test_b_getProduct(self):
		self.get_product()
	
	def test_c_FRAME_BuyNow(self):
		self.FRAME_BuyNow()
	
	def test_g_ProductPage_BuyNow(self):
		self.ProductPage_BuyNow()
	
	def test_k_ShortListPage_BuyNow(self):
		self.ShortListPage_BuyNow()
	
	def test_y_reset(self):
		self.reset()

	def test_z_teardown(self):
		self.quit()

limeroadTest = unittest.TestSuite()
for i in range (3):
	limeroadTest.addTest(Limeroad('test_a_beginLimeroad'))
	limeroadTest.addTest(Limeroad('test_b_getProduct'))		
	limeroadTest.addTest(Limeroad('test_c_FRAME_BuyNow'))
	limeroadTest.addTest(Limeroad('test_g_ProductPage_BuyNow'))
	limeroadTest.addTest(Limeroad('test_k_ShortListPage_BuyNow'))
limeroadTest.addTest(Limeroad('test_y_reset'))


all_tests = unittest.TestSuite([flipkartTest, delightgiftsTest, engraveTest, inonitTest, happilyunmarriedTest, healthkartTest, dezainsTest, fnpTest, vouchersmateTest, excitinglivesTest, babyoyeTest, purplleTest, fabfurnishTest, zansaarTest, shopnineteenTest, caratlaneTest, todugiftTest, hitplayTest, perficoTest, limeroadTest])

# HTMLTestRunner is a package which creates reports generated by 'unnittest' module in HTML format.
# For more see - https://pypi.python.org/pypi/HTMLTestRunner
buf = file("redirectPage_subscribe" + ".html", 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=buf, title = 'Test of subscribe button in redirect page for 3 product of each partner website. Also cross check name, price with partner site.', description='Results on Browser : Firefox')

if __name__ == '__main__':
	runner.run(all_tests)
