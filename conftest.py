import pytest
from allure_commons import fixture
# from src.constants.api_constants import url_create_booking, url_create_token
from src.helpers.api_requests_wrapper import Api_Request
from src.helpers.payload_manager import booking_payload, token_payload
from src.utils.utils import headers

@pytest.fixture(scope="session")
def create_token_id():
    create_post_request = Api_Request()
    response_data = create_post_request.post_request(url="https://restful-booker.herokuapp.com/auth",auth=None,headers=headers(),payload=token_payload())
    response_data=response_data.json()
    return response_data["token"]

@pytest.fixture(scope="session")
def create_booking_id():
    create_post_request = Api_Request()
    response_data = create_post_request.post_request(url="https://restful-booker.herokuapp.com/booking",auth=None,headers=headers(),payload=booking_payload())
    response_data=response_data.json()
    return response_data["bookingid"]


