# Common Utility
# Read data from EXEl, CSV file
# Set Headers



def headers():
    return {'Content-Type': 'application/json'}

def auth_headers(token):
    return {'Content-Type': 'application/json',
            'Cookie': "token="+ str(token)
            }