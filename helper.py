import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def check_email(email):
    if(re.search(regex,email)):
        return 1
    return 0
