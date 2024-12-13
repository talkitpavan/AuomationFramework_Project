import pytest
import allure
import requests
from src.constants.api_constants import url_create_booking, url_create_token
from src.helpers.api_requests_wrapper import Api_Request
from src.helpers.payload_manager import booking_payload, token_payload
from src.utils.utils import headers
from src.helpers.common_verification import *
class TestCreateToken(object):
    @pytest.mark.smoke
    @allure.title("TC_01 Create Token")
    def test_create_token(self):
        create_post_request = Api_Request()
        response_data = create_post_request.post_request(url=url_create_token(),auth=None,headers=headers(),payload=token_payload())
        assert check_status_code_200(response_data)
        assert "token" in response_data.json()
