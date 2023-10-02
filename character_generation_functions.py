import requests
import json
import random

affirmative_responses = ['yes', 'y', ' y', 'yup', 'yurr', 'yas']
negative_responses = ['no', 'nope', 'nup', 'heck no', 'nada', 'n', ' n']

abilities = ["STRENGTH", "DEXTERITY", "CONSTITUTION", "INTELLIGENCE", "WISDOM", "CHARISMA"]

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


def give_user_option_to_choose_background(backgrounds_file_name: str): # WIP... thinking about how to implement

    user_input = input("""Would you like to add a 'background' 
                       to your character? (Y/N) """)

    if user_input.lower() in affirmative_responses:
        print("Excellent! Let's choose one.\n")
        chosen_background = choose_background(backgrounds_file_name)
        print(f"A {chosen_background}? You've lived an interesting life!")
        return chosen_background

    elif user_input.lower() in negative_responses:
        print("Fair enough! A blank slate.")
        return None

    else:
        print("I will take that as a no.")
        return None


def choose_background(backgrounds_file_name: str): # TODO: Use fuzzy matching?

    background_data = load_json_background_data(backgrounds_file_name)
    background_names = [background["Background Name"] for background in background_data]

    print("Your options are:\n")
    print(background_names)

    while True:
        chosen_background = input("\nSo, what background do you pick? ")
        if chosen_background.strip().title() in background_names:
            return chosen_background
        choose_again = input("\nThat doesn't exist - try again? (Y/N) ")
        if choose_again.lower() in negative_responses:
            print("\nNo background it is.")
            return None


def load_json_background_data(file_path: str) -> list[dict]:

    with open(file_path, "r") as json_file:
        loaded_data = json.load(json_file)
    
    return loaded_data


def add_custom_background():
    # Total WIP... thinking about how to implement
    pass


def generate_ability_score_numbers() -> list[int]:

    print("""\nYou can choose to roll for your ability score numbers
          or use the predetermined numbers [15, 14, 13, 12, 10, 8].""")
    
    while True:
        ability_score_decision = input("""\nDo you want to roll for your ability
                                   scores? (Y/N) """)
        if ability_score_decision.lower() in affirmative_responses or negative_responses:
            break
    
    if ability_score_decision.lower() in affirmative_responses:
        print("\nLet's roll!")
        ability_score_nums = roll_for_ability_scores()
        print(f"\nYour ability score numbers are {ability_score_nums}!")
        return ability_score_nums

    else:
        print("\nWe'll use the predetermined stats!")
        return [15, 14, 13, 12, 10, 8]
    

def roll_for_ability_scores() -> list[int]:

    ability_score_nums = []
    for i in range(6):
        rolls = rolls = [random.randint(1, 6) for _ in range(4)]
        rolls = sorted(rolls)
        rolls.pop(0)
        ability_score_nums.append(sum(rolls))
    print(f"\nYour ability score numbers are {ability_score_nums}!")
    return ability_score_nums


def assign_ability_scores(ability_score_nums: list[int]) -> dict:

    print(f"""Your abilities in DnD are STRENGTH, DEXTERITY,
          CONSTITUTION, INTELLIGENCE, WISDOM, and CHARISMA.\n""")

    print("""You need to assign one of your ability score
          numbers to each ability! The higher the number, 
          the stronger the ability.\n""")

    print(f"""Remember, your available ability score numbers
          are {ability_score_nums}.\n""")
    
    print(ability_score_nums)
    
    assigned_ability_scores = {}
    
    for ability in abilities:
        assigned = False

        while assigned is False:

            try:
                assigment_response = int(input(f"What score should go to {ability}? "))

                if assigment_response in ability_score_nums:
                    assigned_ability_scores[ability] = assigment_response
                    ability_score_nums.remove(assigment_response)
                    print(ability_score_nums)
                    assigned = True
                
                else:
                    print("""\nInvalid input! Input must be a number from
                      your available ability scores.\n""")
            
            except:
                print("""\nInvalid input! Input must be a number from
                      your available ability scores.\n""")
    
    return assigned_ability_scores



def calculate_ability_modifiers(ability_score_dict: dict) -> dict:

    ability_modifiers = {}

    for ability in ability_score_dict.keys():
        ability_modifiers[ability] = (ability_score_dict[ability] - 10) // 2
    
    return ability_modifiers



# print(retrieve_list_of_race_options())
# selected_race = check_selected_race_is_valid("dragonborn")
# provide_user_with_info_on_selected_race(selected_race)

# print(retrieve_list_of_class_options())
# selected_class = check_selected_class_is_valid("bard")

# backgrounds_file_name = "dnd_backgrounds_processed.json"
# choose_background(backgrounds_file_name)

ability_score_nums = generate_ability_score_numbers()
assigned_scores = assign_ability_scores(ability_score_nums)
print(assigned_scores)
print(calculate_ability_modifiers(assigned_scores))