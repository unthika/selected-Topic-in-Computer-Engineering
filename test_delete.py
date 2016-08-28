import xml.dom.minidom

dom = xml.dom.minidom.parse('test_create_xml.xml')
#movie = dom.getElementsByTagName("movie")[0]
dom.removeChild(dom.childNodes[0])
dom.writexml( open('test_create_xml.xml', 'w'),
              indent="  ",
              addindent="  ",
              newl='\n')
