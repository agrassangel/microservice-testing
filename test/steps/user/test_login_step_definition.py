from pytest_bdd import scenarios, given, when, then, parsers
from test.common.data.user_credentials import credentials
import random
from .fixtures.schemas.login_schema import loging_response_schema
from assertpy import *

scenarios("user/login.feature")
common_path = "/login"


@given("User has a credentials", target_fixture="login_credentials")
def set_valid_credentials():
    nex_user = random.randint(0, len(credentials) - 1)
    return list(credentials)[nex_user]


@when("User requires access to the system", target_fixture="login_response")
def login_user_in_system(login_credentials, request_manager):
    return request_manager.login(common_path, str(login_credentials["username"]), str(login_credentials["password"]))


@then("System will authorize the user")
def check_valid_authentication(login_response, validate_response):
    validate_response.validate_valid_status_code(login_response, 'login')


@when(parsers.parse('User requires access to the system with the invalid field "{field}"'),
      target_fixture='login_error_response_list')
def set_invalid_credentials(field, request_manager, login_credentials, user_fail_profile):
    profile_list = user_fail_profile.get_fail_user_profile(field)
    response_error_list = []
    tmp = login_credentials.copy()
    for user_profile in profile_list:
        if field in tmp:
            tmp[field] = user_profile[field]
        else:
            tmp = user_profile
        response = request_manager.login(common_path, str(tmp["username"]),
                                         str(tmp["password"]))
        response_error_list.append(response)
        tmp = login_credentials.copy()
    return response_error_list


@then("System wont authorize the user")
def check_rejected_authentication(login_error_response_list, validate_response, request_manager, logger):
    with soft_assertions():
        for request_response in login_error_response_list:
            validate_response.validate_invalid_status_code(request_response, module_name=common_path)
    logger.info("User authentication fails. Test successful")
