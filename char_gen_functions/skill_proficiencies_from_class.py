import requests
import json

def get_proficiencies_from_class(chosen_class: str):

    response = requests.get(f"https://www.dnd5eapi.co/api/classes/{chosen_class.lower()}")
    class_data = response.json()

    class_proficiencies = []

    for proficiency in class_data["proficiency_choices"][0]["from"]["options"]:
        class_proficiencies.append(proficiency["item"]["name"].replace("Skill: ", ""))

    return class_proficiencies

