import  xml.etree.ElementTree as ET

tree = ET.parse('book.xml')
root = tree.getroot()
print(root.tag)
print(root[0][1].text)
d = root.attrib
for child in root:
	print(child.tag,child.attrib)
	for childs in child:
		print(childs.tag,childs.attrib)





