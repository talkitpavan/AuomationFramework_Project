# payload required for requests

def booking_payload():
    booking_payload = {
        "firstname": "Vijay",
        "lastname": "Chauhan",
        "totalprice": 115,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },

        "additionalneeds": "Breakfast"
    }
    return booking_payload
def update_booking_payload():
    booking_payload = {
        "firstname": "Pavan",
        "lastname": "Prajakta",
        "totalprice": 115,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2014-01-01",
            "checkout": "2014-01-01"
        },

        "additionalneeds": "Lunch"
    }
    return booking_payload

def partial_update_booking_payload():
    booking_payload = {
        "firstname": "Neelam",
        "lastname": "Raj",
    }
    return booking_payload
def token_payload():
    token_payload = {
            "username": "admin",
            "password": "password123"
    }
    return token_payload