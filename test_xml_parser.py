import xml.etree.ElementTree as ET
tree = ET.parse('MovieAll_SPN.xml')
root = tree.getroot()
for movie in root.findall('movie'):
	print (movie.find('name').text)
	print ("\tType:")
	for type_ in movie.find('types'):
		print("\t\t"+type_.text)
	print ("\tMain character:")
	for name_actor in movie.find('stars'):
		print("\t\t"+name_actor.text)
	print ("\tDirector:")
	print ("\t\t"+movie.find('director').text)
	print ("\tDate:")
	date_ = movie.find('date')
	print ("\t\t"+date_.find('day').text+"-"+date_.find('month').text+"-"+date_.find('year').text)
	print("===============================")

name_serch = "Tom Hanks"
print ("Tom Hanks:")
for movie in root.findall('movie'):
        for name_actor in movie.find('stars'):
                if(name_serch == name_actor.text):
                        print ("\t"+movie.find('name').text)
print("===============================")
types_serch = "Action"
print ("Action movie:")
for movie in root.findall('movie'):
        for type_ in movie.find('types'):
                if(types_serch == type_.text):
                        print ("\t"+movie.find('name').text)
