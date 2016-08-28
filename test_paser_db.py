import xml.etree.ElementTree as ET
import mysql.connector
tree = ET.parse('MovieAll_SPN.xml')
root = tree.getroot()
conn = mysql.connector.connect(host="localhost", 
                     user="root",        
                     passwd="1234",
                     db="selecttopic")   
c = conn.cursor()
for movie in root.findall('movie'):
	moviename = movie.find('name').text
	c.execute('insert into test values("'+moviename+'")')
	print (movie.find('name').text)
	
conn.commit() 
conn.close()

