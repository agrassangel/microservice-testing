from pytest_bdd import scenarios, given, when, then
from .fixtures.schemas.cards_schema import *
from faker import Faker
from json import dumps
from assertpy import assert_that, soft_assertions
import random

from .test_registration_step_definition import fake

scenarios("user/cards.feature")
common_path = "/cards"


@given("User has a card", target_fixture="cards_response")
@when("User attempts to get cards", target_fixture="cards_response")
@when("User attempts to get cards without being logged", target_fixture="auth_fails_response")
def get_cards(request_manager):
    return request_manager.get(common_path)


@then("System response with the list of cards")
def step_impl(cards_response, logger, validate_response):
    validate_response.validate_valid_status_code(cards_response, common_path, get_cards_response_schema,
                                                 status_code=200)


@when("User attempts to create a new card", target_fixture="post_card_creation")
@when("User attempts to create a new cards without being logged", target_fixture="auth_fails_response")
def post_create_new_card(login_data, request_manager):
    # Validate all scenarios when we get the business rules
    return __create_card__(request_manager)


def __create_card__(request_manager):
    faker = Faker()
    card = faker.credit_card_full()
    parameter = dumps({
        "longNum": faker.credit_card_number(),
        "expires": faker.credit_card_expire(),
        "ccv": faker.credit_card_security_code(),
        "userID": ""
    })
    return request_manager.post(common_path, payload=parameter)


@then("System should create the new card")
def check_card_creation(post_card_creation, logger, validate_response, request_manager):
    # According to doc should return 200 status code
    with soft_assertions():
        validate_response.validate_valid_status_code(post_card_creation, common_path, post_cards_response_schema, 200)
        id_card = str(post_card_creation.json_r["id"])
        card_request = __get_card_by_id(id_card, request_manager)
        assert_that(len(card_request), f'There is not card created with id {id_card}').is_equal_to(1)
    logger.info("Card creation successful. Test passed")


def __get_card_by_id(card_id, request_manager):
    return request_manager.get(f'{common_path}/{card_id}')


@when("User attempts to get cards by id", target_fixture="cards_by_id_response")
def get_card_by_id(request_manager):
    resp = __create_card__(request_manager)
    id_card = str(resp.json_r["id"])
    return __get_card_by_id(id_card, request_manager)


@then("System response with the card")
def check_get_card_by_id(cards_by_id_response, logger, validate_response):
    validate_response.validate_valid_status_code(cards_by_id_response,
                                                 f' GET card by id  in module {common_path} should be performed',
                                                 get_cards_by_id_response_schema,
                                                 200)
    logger.info("Get card by id successful. Test passed")


@when("User attempts to delete a card by its id", target_fixture="delete_card_response")
def delete_card_by_id(cards_response, request_manager):
    list_c = list(cards_response.json_r["_embedded"]["card"])
    card = list_c[random.randint(0, len(list_c) - 1)]
    id_card = str(card["id"])
    return {"id_card": id_card, "response": request_manager.delete(f'{common_path}/{request_manager}')}


@then("Card should not exists in the system")
def check_card_deletion(delete_card_response, validate_response, logger, request_manager):
    with soft_assertions():
        id_card = delete_card_response["id_card"]
        validate_response.validate_valid_status_code(delete_card_response["response"],
                                                     f' GET card by id  in module {common_path} should be performed',
                                                     delete_cards_response_schema, 200)
        res = __get_card_by_id(id_card, request_manager)
        assert_that(len(res), f'Card with id {id_card} should be deleted but it was not').is_equal_to(0)
