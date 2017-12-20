import re
def validate_pin(pin):
    return re.search(re.compile(r"^\d\d\d\d(\d\d)?$"),pin) != None