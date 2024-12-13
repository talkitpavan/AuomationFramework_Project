from math import trunc


def check_status_code_200(response_data):
    if response_data.status_code ==200:
        return True
    else:
        return False

def check_status_code_201(response_data):
    if response_data.status_code ==201:
        return True
    else:
        return False