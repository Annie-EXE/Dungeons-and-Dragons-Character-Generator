import requests
import json

def get_proficiencies_from_class(chosen_class: str):

    response = requests.get(f"https://www.dnd5eapi.co/api/classes/{chosen_class.lower()}")
    class_data = response.json()

    class_proficiencies = []

    for proficiency in class_data["proficiency_choices"][0]["from"]["options"]:
        class_proficiencies.append(proficiency["item"]["name"].replace("Skill: ", "").lower())

    if len(class_proficiencies) > 2:
        filtered_proficiencies = []
        first_pick = select_proficiency_option(class_proficiencies, filtered_proficiencies)
        filtered_proficiencies.append(first_pick)
        second_pick = select_proficiency_option(class_proficiencies, filtered_proficiencies)
        filtered_proficiencies.append(second_pick)
        return filtered_proficiencies

    return class_proficiencies


def select_proficiency_option(proficiency_options: list,
                                  filtered_proficiencies: list):

    pick = input("""Please pick a proficiency from the list 
                       of background proficiencies: """).lower()
    while pick not in proficiency_options and pick not in filtered_proficiencies:
        pick = input("Not a valid background proficiency - please pick again: ").lower()
        
    return pick


print(get_proficiencies_from_class("druid"))