from SOAPpy import SOAPServer
import xml.etree.ElementTree as ET
import sys, time
from SOAPpy import WSDL
class webservice:
    def return_xml():
        tree = ET.parse('MovieAll_SPN.xml')
        root = tree.getroot()
        return ET.tostring(root,encoding="us-ascii", method="xml")
    def movieNameFromeType(self,type):
        list_ = []
        tree = ET.parse('MovieAll_SPN.xml')
        root = tree.getroot()
        for movie in root.findall('movie'):
            for type_ in movie.find('types'):
                if type_.text == type:
					list_.append(movie.find('name').text)
					list_.append("time: "+movie.find('time').text)
					list_.append("resolution: "+movie.find('resolution').text)
        return list_
    def update_xml(self,name,type,name_actor,Director,day,month,year):
        tree = ET.parse('MovieAll_SPN.xml')
        root = tree.getroot()
        new_tag = ET.Element('movie')
        name_tag = ET.Element('name')
        name_tag.text = name
        types_tag = ET.Element('types')
        for t in type:
            type_tag = ET.Element('type')
            type_tag.text = t
            types_tag.append(type_tag)
        stars_tag = ET.Element('stars')
        for star in name_actor:
            actor_tag = ET.Element('name_actor')
            actor_tag.text = star
            stars_tag.append(actor_tag)
        director_tag = ET.Element('director_actor')
        director_tag.text = Director
        date_tag = ET.Element('date')
        day_tag = ET.Element('day')
        month_tag = ET.Element('month')
        year_tag = ET.Element('year')
        date_tag.append(day_tag)
        date_tag.append(month_tag)
        date_tag.append(year_tag)
        new_tag.append(name_tag)
        new_tag.append(types_tag)
        new_tag.append(stars_tag)
        new_tag.append(director_tag)
        new_tag.append(date_tag)
        root.insert(0,new_tag)
        tree.write('MovieAll_SPN.xml')

print "start"
server = SOAPServer(("172.31.43.127", 8081))
server.registerObject(webservice(), "xml")
server.serve_forever()



