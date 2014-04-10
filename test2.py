import json, unittest

json_data2 = open('data.jl')
our_data = json.load(json_data2)
json_data2.close()


with open('items.jl', 'a+') as json_data:
	crawled_data = json_data.read().rstrip(',')
	crawled_data = '[' + crawled_data + ']'
	json_data.seek(0)
	json_data.truncate()
	json_data.write(crawled_data)

json_data = open('items.jl')
crawled_data = json.load(json_data)
json_data.close()



class Flipkart(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'flipkart.com':
#					print our_data[i]['flipkart.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'flipkart.com' and crawled_data[k]['partner_url'] == our_data[i]['flipkart.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['flipkart.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['flipkart.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['flipkart.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'flipkart.com':
#					print our_data[i]['flipkart.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'flipkart.com' and crawled_data[k]['partner_url'] == our_data[i]['flipkart.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['flipkart.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['flipkart.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['flipkart.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")


class Inonit(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'inonit.in':
#					print our_data[i]['delightgifts.in'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'inonit.in' and crawled_data[k]['partner_url'] == our_data[i]['inonit.in'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['inonit.in'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['inonit.in'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['inonit.in'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'inonit.in':
#					print our_data[i]['inonit.in'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'inonit.in' and crawled_data[k]['partner_url'] == our_data[i]['inonit.in'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['inonit.in'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['inonit.in'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['inonit.in'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Delightgifts(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'delightgifts.in':
#					print our_data[i]['delightgifts.in'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'delightgifts.in' and crawled_data[k]['partner_url'] == our_data[i]['delightgifts.in'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['delightgifts.in'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['delightgifts.in'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['delightgifts.in'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'delightgifts.in':
#					print our_data[i]['delightgifts.in'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'delightgifts.in' and crawled_data[k]['partner_url'] == our_data[i]['delightgifts.in'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['delightgifts.in'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['delightgifts.in'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['delightgifts.in'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Engrave(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'engrave.in':
#					print our_data[i]['engrave.in'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'engrave.in' and crawled_data[k]['partner_url'] == our_data[i]['engrave.in'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['engrave.in'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['engrave.in'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['engrave.in'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'engrave.in':
#					print our_data[i]['engrave.in'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'engrave.in' and crawled_data[k]['partner_url'] == our_data[i]['engrave.in'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['engrave.in'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['engrave.in'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['engrave.in'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Happilyunmarried(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'happilyunmarried.com':
#					print our_data[i]['happilyunmarried.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'happilyunmarried.com' and crawled_data[k]['partner_url'] == our_data[i]['happilyunmarried.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['happilyunmarried.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['happilyunmarried.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['happilyunmarried.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'happilyunmarried.com':
#					print our_data[i]['happilyunmarried.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'happilyunmarried.com' and crawled_data[k]['partner_url'] == our_data[i]['happilyunmarried.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['happilyunmarried.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['happilyunmarried.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['happilyunmarried.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Healthkart(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'healthkart.com':
#					print our_data[i]['healthkart.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'healthkart.com' and crawled_data[k]['partner_url'] == our_data[i]['healthkart.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['healthkart.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['healthkart.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['healthkart.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'healthkart.com':
#					print our_data[i]['healthkart.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'healthkart.com' and crawled_data[k]['partner_url'] == our_data[i]['healthkart.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['healthkart.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['healthkart.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['healthkart.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Dezains(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'dezains.com':
#					print our_data[i]['dezains.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'dezains.com' and crawled_data[k]['partner_url'] == our_data[i]['dezains.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['dezains.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['dezains.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['dezains.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'dezains.com':
#					print our_data[i]['dezains.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'dezains.com' and crawled_data[k]['partner_url'] == our_data[i]['dezains.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['dezains.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['dezains.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['dezains.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Fnp(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'fnp.com':
#					print our_data[i]['fnp.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'fnp.com' and crawled_data[k]['partner_url'] == our_data[i]['fnp.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['fnp.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['fnp.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['fnp.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'fnp.com':
#					print our_data[i]['fnp.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'fnp.com' and crawled_data[k]['partner_url'] == our_data[i]['fnp.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['fnp.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['fnp.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['fnp.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Vouchersmate(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'vouchersmate.com':
#					print our_data[i]['vouchersmate.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'vouchersmate.com' and crawled_data[k]['partner_url'] == our_data[i]['vouchersmate.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['vouchersmate.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['vouchersmate.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['vouchersmate.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'vouchersmate.com':
#					print our_data[i]['vouchersmate.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'vouchersmate.com' and crawled_data[k]['partner_url'] == our_data[i]['vouchersmate.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['vouchersmate.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['vouchersmate.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['vouchersmate.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Excitinglives(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'excitinglives.com':
#					print our_data[i]['excitinglives.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'excitinglives.com' and crawled_data[k]['partner_url'] == our_data[i]['excitinglives.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['excitinglives.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['excitinglives.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['excitinglives.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'excitinglives.com':
#					print our_data[i]['excitinglives.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'excitinglives.com' and crawled_data[k]['partner_url'] == our_data[i]['excitinglives.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['excitinglives.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['excitinglives.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['excitinglives.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Babyoye(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'babyoye.com':
#					print our_data[i]['babyoye.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'babyoye.com' and crawled_data[k]['partner_url'] == our_data[i]['babyoye.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['babyoye.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['babyoye.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['babyoye.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'babyoye.com':
#					print our_data[i]['babyoye.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'babyoye.com' and crawled_data[k]['partner_url'] == our_data[i]['babyoye.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['babyoye.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['babyoye.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['babyoye.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Purplle(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'purplle.com':
#					print our_data[i]['purplle.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'purplle.com' and crawled_data[k]['partner_url'] == our_data[i]['purplle.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['purplle.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['purplle.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['purplle.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'purplle.com':
#					print our_data[i]['purplle.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'purplle.com' and crawled_data[k]['partner_url'] == our_data[i]['purplle.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['purplle.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['purplle.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['purplle.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Fabfurnish(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'fabfurnish.com':
#					print our_data[i]['fabfurnish.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'fabfurnish.com' and crawled_data[k]['partner_url'] == our_data[i]['fabfurnish.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['fabfurnish.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['fabfurnish.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['fabfurnish.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'fabfurnish.com':
#					print our_data[i]['fabfurnish.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'fabfurnish.com' and crawled_data[k]['partner_url'] == our_data[i]['fabfurnish.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['fabfurnish.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['fabfurnish.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['fabfurnish.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Zansaar(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'zansaar.com':
#					print our_data[i]['zansaar.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'zansaar.com' and crawled_data[k]['partner_url'] == our_data[i]['zansaar.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['zansaar.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['zansaar.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['zansaar.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'zansaar.com':
#					print our_data[i]['zansaar.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'zansaar.com' and crawled_data[k]['partner_url'] == our_data[i]['zansaar.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['zansaar.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['zansaar.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['zansaar.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Shopnineteen(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'shopnineteen.com':
#					print our_data[i]['shopnineteen.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'shopnineteen.com' and crawled_data[k]['partner_url'] == our_data[i]['shopnineteen.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['shopnineteen.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['shopnineteen.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['shopnineteen.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'shopnineteen.com':
#					print our_data[i]['shopnineteen.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'shopnineteen.com' and crawled_data[k]['partner_url'] == our_data[i]['shopnineteen.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['shopnineteen.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['shopnineteen.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['shopnineteen.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Caratlane(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'caratlane.com':
#					print our_data[i]['caratlane.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'caratlane.com' and crawled_data[k]['partner_url'] == our_data[i]['caratlane.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['caratlane.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['caratlane.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['caratlane.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'caratlane.com':
#					print our_data[i]['caratlane.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'caratlane.com' and crawled_data[k]['partner_url'] == our_data[i]['caratlane.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['caratlane.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['caratlane.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['caratlane.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Todugift(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'todugift.com':
#					print our_data[i]['todugift.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'todugift.com' and crawled_data[k]['partner_url'] == our_data[i]['todugift.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['todugift.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['todugift.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['todugift.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'todugift.com':
#					print our_data[i]['todugift.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'todugift.com' and crawled_data[k]['partner_url'] == our_data[i]['todugift.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['todugift.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['todugift.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['todugift.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Hitplay(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'hitplay.in':
#					print our_data[i]['hitplay.in'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'hitplay.in' and crawled_data[k]['partner_url'] == our_data[i]['hitplay.in'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['hitplay.in'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['hitplay.in'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['hitplay.in'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'hitplay.in':
#					print our_data[i]['hitplay.in'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'hitplay.in' and crawled_data[k]['partner_url'] == our_data[i]['hitplay.in'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['hitplay.in'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['hitplay.in'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['hitplay.in'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Perfico(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'perfico.com':
#					print our_data[i]['perfico.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'perfico.com' and crawled_data[k]['partner_url'] == our_data[i]['perfico.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['perfico.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['perfico.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['perfico.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'perfico.com':
#					print our_data[i]['perfico.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'perfico.com' and crawled_data[k]['partner_url'] == our_data[i]['perfico.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['perfico.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['perfico.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['perfico.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")

class Limeroad(unittest.TestCase):

	def title(self, x):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'limeroad.com':
#					print our_data[i]['limeroad.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'limeroad.com' and crawled_data[k]['partner_url'] == our_data[i]['limeroad.com'][x]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['limeroad.com'][x]['prPage'])
							print "Found data [at partner site]: " 
							print str(crawled_data[k]['partner_title'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['limeroad.com'][x]['our_name'])

							try:
								self.assertEqual(crawled_data[k]['partner_title'], our_data[i]['limeroad.com'][x]['our_name'])
								print '[OK]'
							except AssertionError:
								print "[NOT OK]"
								raise AssertionError("Name does not match")


	def price(self, y):
		for i in range (len(our_data)):
			for key in our_data[i].keys():
				if key == 'limeroad.com':
#					print our_data[i]['limeroad.com'][j]['partner_url']
					for k in range (len(crawled_data)):
						if (crawled_data[k]['site'] == 'limeroad.com' and crawled_data[k]['partner_url'] == our_data[i]['limeroad.com'][y]['partner_url']):
							print "PRODUCT : " + str(our_data[i]['limeroad.com'][y]['prPage'])
							print "Found data [at partner site]: "
							print str(crawled_data[k]['partner_price'])
							print "Expected data [from wishpicker]: " 
							print str(our_data[i]['limeroad.com'][y]['our_price'])
							try:
								self.assertEqual(crawled_data[k]['partner_price'], our_data[i]['limeroad.com'][y]['our_price'])
								print "[OK]"
							except AssertionError:
								print '[NOT OK]'
								raise AssertionError("Price does not match")



if __name__ == '__main__':
	unittest.main()
