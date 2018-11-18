import xml.dom.minidom
DOM = xml.dom.minidom
doc = DOM.parse(open("example.xml"))
a = doc.getElementsByTagName("note")[0]
a.tagName = 'letter'
print a.toxml("utf-8")
