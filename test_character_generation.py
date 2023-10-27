import re
import string

def split_options(choice_desc: str) -> list[str]:
    """
    Splits a string of options, to return a
    list of options, using regex
    """
    options = re.findall(r'\([a-z]\)\s*([^()]+)', choice_desc)

    options = [option.replace(' or ', '').strip() for option in options]

    return options

print(split_options("(a) a shortbow and quiver of 20 arrows or (b) a shortsword"))
print(split_options("(a) a burglar’s pack, (b) a dungeoneer’s pack, or (c) an explorer’s pack, (d) egg"))


def make_starting_equipment_choice(choice_desc: str) -> str:
    options = split_options(choice_desc)
    
    valid_choices = set(string.ascii_lowercase[:len(options)])  # Generate valid choices a, b, c, ...
    
    while True:
        print("Choose your starting equipment:")
        for i, option in enumerate(options):
            print(f"({string.ascii_lowercase[i]}) {option}")
        
        user_choice = input("Enter your choice: ").strip().lower()
        
        if user_choice in valid_choices:
            return options[ord(user_choice) - ord('a')]
        else:
            print("Invalid choice. Please choose a valid option.")
            

# Example usage:
choice_description = "(a) a burglar’s pack, (b) a dungeoneer’s pack, or (c) an explorer’s pack, (d) egg"
chosen_option = make_starting_equipment_choice(choice_description)
print(f"You chose: {chosen_option}")