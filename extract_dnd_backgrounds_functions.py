import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


def parse_xml_file_and_get_root(file_path: str) -> Element:
    """
    Parse an XML file and return 
    the root element of the XML tree.
    """
    tree = ET.parse(file_path)

    root = tree.getroot()

    return root


def get_info_for_background(root: Element, background_num: int):

    background = root.findall(".//background")[background_num]

    name = background.find(".//name")

    return name.text


root = parse_xml_file_and_get_root("dnd_backgrounds.xml")

print(get_info_for_background(root, 20))