# author: zzq

import xml.etree.cElementTree as ET

new_xml = ET.Element("namelist")
personinfo = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "yes"})
name = ET.SubElement(personinfo, "name")
age = ET.SubElement(personinfo, "age", attrib={"checked": "no"})
sex = ET.SubElement(personinfo, "sex")

name.text = 'Alex'
age.text = '33'
sex.text = 'M'

personinfo2 = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "no"})
name = ET.SubElement(personinfo2, "name")
age = ET.SubElement(personinfo2, "age")
sex = ET.SubElement(personinfo2, "sex")

name.text = 'Oldboy Ran'
age.text = '19'
sex.text = 'M'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式