from .common.fixtures.logger import *
from .common.fixtures.local_request import *
from .common.fixtures.schema_validator import *
from .common.fixtures.response_validation import *

from pytest_bdd import given, then
from test.common.data.user_credentials import credentials
import random


@given("User is not login in the system")
def step_impl(request_manager):
    request_manager.clear_cookies_from_session()


@given("User logged into the system", target_fixture="login_data")
def user_logging(request_manager):
    nex_user = random.randint(0, len(credentials) - 1)
    login_credentials = list(credentials)[nex_user]
    return request_manager.login('/login', str(login_credentials["username"]), str(login_credentials["password"]))


@then("An error should be shown by the system")
def step_impls(logger, auth_fails_response, validate_response):
    # Parameter: auth_fails_response parameter
    validate_response.validate_invalid_status_code(auth_fails_response,
                                                   " GET with unauthorized user should fail")
    logger.info(" Request an API with not authorization fails. Test successful")
