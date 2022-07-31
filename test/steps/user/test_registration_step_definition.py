from pytest_bdd import scenarios, given, when, then, parsers
from faker import Faker
from json import dumps
from assertpy import *
from .fixtures.schemas.registration import register_user_schema
from test.steps.user.fixtures.schemas.registration import *

fake = Faker()
CONVERTERS = {
    'username': int
}
# given_basket = partial(given, target_fixture='basket', converters=CONVERTERS)
# when_basket = partial(given,  converters=CONVERTERS)

common_path = "/register"
scenarios("user/register.feature")


@given(parsers.parse('I am an invalid user profile "{field}"'), target_fixture="user_profile_list")
def setup_valid_user(field, user_fail_profile):
    # with soft_assertions():

    return user_fail_profile.get_fail_user_profile(field)


@when('I try to register in the system', target_fixture="request_response_list")
def register_invalid_user(user_profile_list, request_manager):
    response_error_list = []
    for user_profile in user_profile_list:
        response = execute_user_registration(user_profile, request_manager)
        response_error_list.append(response)
    return response_error_list


@then('Registration will fail')
def check_fail_registration_response(logger, validate_response, request_response_list, request_manager):
    with soft_assertions():
        for request_response in request_response_list:
            validate_response.validate_invalid_status_code(request_response, module_name=common_path)
    logger.info("User registration fails. Test successful")


def execute_user_registration(user_profile, request_manager):
    params = dumps({
        "username": str(user_profile["username"]),
        "password": str(user_profile["password"]),
        "email": str(user_profile["mail"])  # it's accepting email with wrong format
    })
    return request_manager.post(common_path, payload=params)


def get_fake_profile():
    return fake.simple_profile()


@given('I am a valid user', target_fixture="user_profile")
def setup_valid_user():
    fake_profile = get_fake_profile()
    fake_profile["password"] = fake.password()
    return fake_profile


@when('I register in the system', target_fixture="request_response")
def register_user(user_profile, request_manager):
    return execute_user_registration(user_profile, request_manager)


@then('System will register my account')
def check_account_creation_response(validate_response, request_response, request_manager, schemavalidator_fixture):
    validate_response.validate_valid_status_code(request_response, "Register new user", register_user_schema)
