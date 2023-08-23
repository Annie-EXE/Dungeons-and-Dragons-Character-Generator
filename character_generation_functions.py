import requests
import json

def retrieve_list_of_race_options() -> list[str]:

    response = requests.get("https://www.dnd5eapi.co/api/races")
    races_data = response.json()

    valid_race_count = races_data["count"]

    print(f"There are {valid_race_count} races to play as in DnD 5e.")

    valid_races = []

    for i in range(len(races_data["results"])):
        race_name = races_data["results"][i]["name"]
        valid_races.append(race_name)

    return valid_races


def check_selected_race_is_valid(input_race: str) -> str:

    response = requests.get("https://www.dnd5eapi.co/api/races")
    races_data = response.json()

    for i in range(len(races_data["results"])):
        race_name = races_data["results"][i]["name"]

        if input_race.lower() == race_name.lower():
            print(f"Ah, so you'd like to play as a {race_name}?")
            return race_name

    raise ValueError("Sorry, 5e doesn't offer that race!")


def provide_user_with_info_on_selected_race(chosen_race: str) -> None:

    response = requests.get(f"https://www.dnd5eapi.co/api/races/{chosen_race.lower()}")
    race_data = response.json()

    size_description = race_data["size_description"]

    print("\n" + size_description + "\n")

    print("You have the following traits:\n") #Add functionality for users to search up traits

    for item in race_data["traits"]:
        print(item["name"])


def retrieve_list_of_class_options() -> list[str]:

    response = requests.get("https://www.dnd5eapi.co/api/classes")
    class_data = response.json()

    valid_class_count = class_data["count"]

    print(f"There are {valid_class_count} classes to play as in DnD 5e.")

    valid_races = []

    for i in range(len(class_data["results"])):
        class_name = class_data["results"][i]["name"]
        valid_races.append(class_name)

    return valid_races


def check_selected_class_is_valid(input_class: str) -> str:

    response = requests.get("https://www.dnd5eapi.co/api/classes")
    class_data = response.json()

    for i in range(len(class_data["results"])):
        class_name = class_data["results"][i]["name"]

        if input_class.lower() == class_name.lower():
            print(f"""I used to be a {class_name} too, but felt that 
            'disembodied voice' was my calling.""")
            return class_name

    raise ValueError("Sorry, 5e doesn't offer that class!")


print(retrieve_list_of_race_options())
selected_race = check_selected_race_is_valid("dragonborn")
provide_user_with_info_on_selected_race(selected_race)

print(retrieve_list_of_class_options())
selected_class = check_selected_class_is_valid("bard")
