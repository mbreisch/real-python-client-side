# XML Parsing 1

from xml.etree import ElementTree as et

doc=et.parse("cars.xml")

print doc.find("CAR/MODEL").text
