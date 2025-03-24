import re

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
    
def is_pure_str(str):
    return bool(re.fullmatch(r'[A-Za-z]+', str))