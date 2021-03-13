import xml.etree.ElementTree as et
import sys
class XML_parser():
    def __init__(self, xml):
        self.xml = xml
    
    def parse(self, parse_type="doc"):
        if parse_type == "doc":
            root = et.parse(self.xml).getroot()
        else:
            root = et.fromstring(self.xml)
        tag = root.tag
        print("Root TAG is : - ",str(tag))
        attributes = root.attrib
        print("Attributes of Root are: - ")
        for k, v in attributes.items():
            print("\t"+str(k)+" : "+str(v))
        print("\n Only details, now Subtags : - ")
        for employee in root:
            print("\n")
            for element in employee:
                ele_name = element.tag
                ele_value = employee.find(element.tag).text
                print(f"\t {ele_name}, : {ele_value}")
        print("\n Details with subtag : - ")
        for employee in root.findall("employee"):
            print("\n")
            print(f"\t Name: {str(employee.find("name").text)}")
            print(f"\t Salary: {str(employee.find("salary").text)}")
            print(f"\t Age: {str(employee.find("age").text)}")
            print(f"\t Manager ID: {str(employee.find("manager_id").text)}")
            print(f"\t DOJ: {str(employee.find("doj").text)}")

obj = XML_parser(sys.argv[1])
obj.parse()
