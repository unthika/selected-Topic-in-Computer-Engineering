import xml.dom.minidom
import xml.dom
#dom = xml.dom.minidom.parse('test_create_xml.xml')
doc = xml.dom.minidom.Document()

root = doc.createElement("movie")
root.setAttribute( "name", 'abcd' )
doc.appendChild(root)
 
tempChild = doc.createElement("type")
root.appendChild(tempChild)

nodeText = doc.createTextNode("Action")
tempChild.appendChild(nodeText)

doc.writexml( open('test_create_xml.xml', 'w'),
              indent="  ",
              addindent="  ",
              newl='\n')
 
doc.unlink()
