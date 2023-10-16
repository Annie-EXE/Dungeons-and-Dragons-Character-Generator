import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import json

def parse_xml_file_and_get_root(file_path: str) -> Element:
    """
    Parse an XML file and return 
    the root element of the XML tree.
    """
    tree = ET.parse(file_path)

    root = tree.getroot()

    return root


def get_info_for_background(root: Element, background_num: int) -> dict:
    """
    Will extract data on the
    specified background, and
    return it as a dictionary.
    """
    background = root.findall(".//background")[background_num]

    name = background.find(".//name").text
    traits = background.findall(".//trait")

    feature_name = None
    feature_desc = None
    skill_proficiencies = None
    equipment = None

    for trait in traits:

        if trait.find("name").text == "Skill Proficiencies":
            skill_proficiencies = trait.find("text").text
        
        elif "Feature" in trait.find("name").text:
            feature_name = trait.find("name").text.split(": ")[-1]
            feature_desc = trait.findall("text")[0].text
        
        if trait.find("name").text == "Equipment":
            equipment = trait.find("text").text

    background_info = {
        "Background Name": name,
        "Skill Proficiencies": skill_proficiencies,
        "Feature": {
            feature_name: feature_desc
        },
        "Equipment": equipment
    }

    return background_info


def get_info_for_all_backgrounds(root: Element) -> list[dict]:
    """
    Extracts useful information from
    each background in the .xml file,
    into a list of dictionaries.
    """
    backgrounds_list = []

    for i in range(len(root)):
        background = get_info_for_background(root, i)
        backgrounds_list.append(background)

    return backgrounds_list


def create_json_file(data: list[dict], file_path: str) -> str:
    """
    Creates a .json file and 
    uploads data to it.
    """
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    return "Data processed!"


if __name__ == "__main__":

    root = parse_xml_file_and_get_root("dnd_backgrounds.xml")

    background_data = get_info_for_all_backgrounds(root)

    background_data_file_path = "dnd_backgrounds_processed.json"

    create_json_file(background_data, background_data_file_path)