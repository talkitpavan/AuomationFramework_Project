import pytest
import allure
import requests
from conftest import create_booking_id
from conftest import create_token_id
from src.constants.api_constants import url_get_booking, url_update_partial_booking, url_delete_booking, \
    url_create_booking
from src.helpers import *
from src.helpers.api_requests_wrapper import Api_Request
from src.helpers.common_verification import check_status_code_200
from src.helpers.payload_manager import update_booking_payload, partial_update_booking_payload, booking_payload
from src.utils.utils import headers, auth_headers

class TestCreateBooking(object):
    @pytest.mark.smoke
    @allure.title("TC_01 Create Booking ")
    def test_create_booking(self):
        create_post_request = Api_Request()
        response_data = create_post_request.post_request(url=url_create_booking(),auth=None,headers=headers(),payload=booking_payload())
        id=response_data.json()["bookingid"]
        assert check_status_code_200(response_data)
        # assert response_data.status_code==200
        response_data=response_data.json()
        assert isinstance(response_data["booking"]["firstname"], str)
        assert response_data["booking"]["firstname"] == booking_payload()["firstname"]
        assert response_data["booking"]["lastname"] == booking_payload()["lastname"]
        assert response_data["bookingid"]>0
        return id


        # base_url = "https://restful-booker.herokuapp.com"
        # base_path = "/booking"
        # #bookingid = str(create_booking())
        # #URL = base_url + base_path +"/"+bookingid
        # URL = base_url + base_path +"/"+ str(create_booking())
        # headers = {'Content-Type': 'application/json'}
        # response_data = resquest.get(url,auth,header,data)
        # assert response_data.status_code == 200
        # response_data=response_data.json()
        # assert isinstance(response_data["firstname"], str)

