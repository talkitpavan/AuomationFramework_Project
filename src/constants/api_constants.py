# API constants all which contains all the end points
# Keep the URLS
from conftest import create_booking_id

def base_url():
    return "https://api.test.auomationframework.com"
def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"
def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"
def url_get_booking(bookingid):
        return "https://restful-booker.herokuapp.com/booking/"+str(bookingid)
def url_update_booking(bookingid):
        return "https://restful-booker.herokuapp.com/booking/"+str(bookingid)
def url_update_partial_booking(bookingid):
        return "https://restful-booker.herokuapp.com/booking/"+str(bookingid)
def url_delete_booking(bookingid):
        return "https://restful-booker.herokuapp.com/booking/"+str(bookingid)

