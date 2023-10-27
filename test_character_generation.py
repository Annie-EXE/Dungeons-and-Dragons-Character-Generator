import re

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

