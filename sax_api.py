#!/usr/bin/python
import xml.sax
class MovieHandler( xml.sax.ContentHandler ):
	def __init__(self):
		self.CurrentData = ""
		self.title = ""
		self.type = ""
		self.day = ""
		self.month = ""
		self.year = ""
		self.stars = ""
		self.director = ""
	# Call when an element starts
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == "movie":
			print "*****Movie*****"
		elif tag == "types":
			print "Type:"
		elif tag == "stars":
			print "Stars:"
		elif tag == "director":
			print "Director:"
		elif tag == "name":
			print "Title:"
		elif tag == "date":
			print "Date:"
	def endElement(self, tag):
		if self.CurrentData == "name":
			print " ", self.title
		elif self.CurrentData == "type":
			print " ", self.type
		elif self.CurrentData == "date":
			print "Date:", self.date
		elif self.CurrentData == "name_actor":
			print " ", self.stars
		elif self.CurrentData == "director":
			print " ", self.director
		elif self.CurrentData == "day":
			print " ", self.day,self.month,self.year
		self.CurrentData = ""
		# Call when a character is read
	def characters(self, content):
		if self.CurrentData == "type":
			self.type = content
		elif self.CurrentData == "day":
			self.day = content
		elif self.CurrentData == "month":
			self.month = content
		elif self.CurrentData == "year":
			self.year = content
		elif self.CurrentData == "name":
			self.title = content	
		elif self.CurrentData == "name_actor":
			self.stars = content
		elif self.CurrentData == "director":
			self.director = content

if ( __name__ == "__main__"):
	# create an XMLReader
	parser = xml.sax.make_parser()
	# turn off namepsaces
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	# override the default ContextHandler
	Handler = MovieHandler()
	parser.setContentHandler( Handler )
	parser.parse("MovieAll_SPN.xml")