import json

DBFILE = "database.json"
specifications_dict = {}


def _load_data(filename):
    with open(filename) as db:
        data = json.load(db)
        return data


def _parse_input(input_list):
    """
    Validate input, to check if Multiple types for one category found.
    Check if invalid item code is passed
    """
    modified = {
        "Screen": False, "Camera": False, "Port": False, "OS": False, "Body": False
    }
    
    for item_code in input_list:
        try:
            if modified[specifications_dict[item_code]["type"]]==False:
                modified[specifications_dict[item_code]["type"]]=True
            else:
                msg = "Invalid Input: Multiple types for one category found."
                print(msg)
                return False, msg
        except Exception as e:
            msg = "Invalid Input: Key error."
            print(msg)
            return False, msg

    return True, "valid Input"


def _parse_db():
    """
    This will create item code as key and the corresponding data as value
    """

    specifications_list = _load_data(DBFILE)
    for specification in specifications_list:
        specifications_dict[specification["code"]] = {
            "id": specification["id"],
            "price": specification["price"],
            "part": specification["part"],
            "type": specification["part"].split(" ")[1]
        }
