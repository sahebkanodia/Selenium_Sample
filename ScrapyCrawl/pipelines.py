import json
class JsonWriterPipeline(object):
	
	
	def __init__(self):
		self.file1 =  open('items.jl', 'a+')
	
	def process_item(self, item, spider):
		line = json.dumps(dict(item)) + ","
		self.file1.write(line)
		return item
