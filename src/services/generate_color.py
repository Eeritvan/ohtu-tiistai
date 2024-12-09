    # TODO KESKEN: odottaa tietokantamuutoksia
# from services.tag_service import TagService

def generate_color(latest_id=None):
    """Generates CSS color for a tag.
    Takes latest tag_id from database or
    the number can be given on the function call.
    Color is returned as CSS compatible name.
    Returns: name of the color as string"""

    colors = {
        0: "255, 0, 0",        # Red
        1: "0, 128, 0",        # Green
        2: "0, 0, 255",        # Blue
        3: "0, 255, 255",      # Cyan
        4: "255, 0, 255",      # Magenta
        5: "255, 255, 0",      # Yellow
        6: "255, 165, 0",      # Orange
        7: "128, 0, 128",      # Purple
        8: "0, 255, 0",        # Lime
        9: "0, 128, 128",      # Teal
        10: "0, 0, 128",       # Navy
        11: "128, 0, 0",       # Maroon
        12: "128, 128, 0",     # Olive
        13: "128, 128, 128",   # Gray
        14: "255, 192, 203",   # Pink
        15: "165, 42, 42",     # Brown
        16: "250, 128, 114",   # Salmon
        17: "184, 134, 11",    # DarkGoldenRod
        18: "106, 90, 205",    # SlateBlue
        19: "0, 100, 0"        # DarkGreen
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
