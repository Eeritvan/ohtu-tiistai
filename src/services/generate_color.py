    # TODO KESKEN: odottaa tietokantamuutoksia
# from services.tag_service import TagService

def generate_color(latest_id=None):
    """Generates CSS color for a tag.
    Takes latest tag_id from database or
    the number can be given on the function call.
    Color is returned as CSS compatible name.
    Returns: name of the color as string"""

    colors = {
    0: "Red",
    1: "Green",
    2: "Blue",
    3: "Cyan",
    4: "Magenta",
    5: "Yellow",
    6: "Orange",
    7: "Purple",
    8: "Lime",
    9: "Teal",
    10: "Navy",
    11: "Maroon",
    12: "Olive",
    13: "Gray",
    14: "Pink",
    15: "Brown",
    16: "Salmon",
    17: "DarkGoldenRod",
    18: "SlateBlue",
    19: "DarkGreen"
    }

    # Kysy tietokannasta viimeisin id
    # tag_service = TagService()
    # latest_id = tag_service.get_latest_id()

    # Selects from color dictionary based on modulo operator
    # Default is Black
    color = "Black"
    if latest_id is not None:
        remainder = (latest_id+1)%20
        color = colors.get(remainder, "Black")
    return color

# For testing
# print("Color:", generate_color())
