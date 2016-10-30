import sys
from SOAPpy import SOAPProxy
from SOAPpy import WSDL
import xml.etree.ElementTree as ET
serverUrl='http://ec2-35-162-15-38.us-west-2.compute.amazonaws.com:8081/'
namespace='xml'
server = SOAPProxy(serverUrl, namespace)
#server.config.dumpSOAPOut = 1
# server.config.dumpSOAPIn = 1
# server.update_xml("movie name",["Adventure","Sifi"],["name1","name2"],"name3","1","oct","1234")
response = server.movieNameFromeType("Adventure")
print response
