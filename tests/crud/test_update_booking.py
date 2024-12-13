import pytest
import allure
import requests
from conftest import create_booking_id
from conftest import create_token_id
from src.constants.api_constants import url_get_booking, url_update_partial_booking, url_delete_booking
from src.helpers import *
from src.helpers.api_requests_wrapper import Api_Request
from src.helpers.payload_manager import update_booking_payload, partial_update_booking_payload
from src.utils.utils import headers, auth_headers


@pytest.mark.smoke
@allure.title("TC_03 Update Booking ")
def test_update_booking_by_id(create_booking_id,create_token_id):
    # base_url = "https://restful-booker.herokuapp.com"
    # base_path = "/booking"
    # url = base_url + base_path +"/"+ str(create_booking_id)
    # headers = {'Content-Type': 'application/json'}
    ar = Api_Request()
    response_data = ar.put_request(url_get_booking(create_booking_id), auth=None, headers=auth_headers(create_token_id), payload=update_booking_payload())
    assert response_data.status_code == 200

def test_get_booking_by_id(create_booking_id):
    # base_url = "https://restful-booker.herokuapp.com"
    # base_path = "/booking"
    # url = base_url + base_path +"/"+ str(create_booking_id)
    # headers = {'Content-Type': 'application/json'}
    ar = Api_Request()
    response_data = ar.get_request(url_get_booking(create_booking_id), auth=None, headers=headers())
    assert response_data.status_code == 200