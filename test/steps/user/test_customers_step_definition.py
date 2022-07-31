from pytest_bdd import scenarios, given, when, then, parsers
from .fixtures.schemas.customers_schema import *
import random

scenarios("user/customers.feature")
common_path = "/customers"


@given("User has a customers", target_fixture="customer_response")
@when("User attempts to get customers", target_fixture="customer_response")
@when("User attempts to get customers without being logged", target_fixture="auth_fails_response")
def get_customers(request_manager):
    return request_manager.get(common_path)


@then("System response with the customers")
def check_customer(logger, customer_response, validate_response):
    validate_response.validate_valid_status_code(customer_response,
                                                 " GET with unauthorized user '" + common_path + "' should fail",
                                                 schema=customer_response_schema)
    logger.info(" Get customers successfully. Test successful")


# DELETE


@when("User attempts to delete customers", target_fixture="delete_customer_response")
def delete_customer(customer_response, request_manager):
    customer_id = str(__extract_customer_id__(customer_response)["customer_id"])
    return {"customer_id": customer_id,
            "response": request_manager.delete(common_path + "/" + customer_id)}


@then("System response will delete the customers")
def check_delete_customer(logger, delete_customer_response, validate_response, request_manager):
    validate_response.validate_valid_status_code(delete_customer_response["response"],
                                                 " DELETE customers '" + common_path + "' should be performed",
                                                 schema=delete_customer_by_id_response_schema)

    get_response = __get_customer_using_id__(request_manager, delete_customer_response["customer_id"])
    validate_response.validate_invalid_status_code(get_response,
                                                   " GET customers after its deletion '" + common_path +
                                                   "' should not be performed")


@when("User attempts to get customers by its id", target_fixture="customer_response")
def get_customer_by_id(customer_response, request_manager):
    temp_dict = __extract_customer_id__(customer_response)
    return __get_customer_using_id__(request_manager, str(temp_dict["customer_id"]))


@when(parsers.parse('User attempts to get customers "{property}" by its id'),
      target_fixture="customer_response_with_property")
def get_customer_property_by_id(property, customer_response, request_manager):
    temp_dict = __extract_customer_id__(customer_response)
    return __get_customer_using_id__(request_manager, str(temp_dict["customer_id"]), str(property))


@then(parsers.parse('System response with the property selected "{property}"'))
def check_customer_property_response(property, logger, validate_response, customer_response_with_property):
    # default schema CARDS schema
    schema_to_evaluate = get_customer_by_id_card_response_schema
    if "address" in property:
        schema_to_evaluate = get_customer_by_id_address_response_schema

    validate_response.validate_valid_status_code(customer_response_with_property,
                                                 f' GET customer by its property "{common_path}/{str(property)} '
                                                 f'should be performed.',
                                                 schema=schema_to_evaluate)
    logger.info(f' Get customers by its property "{str(property)}"  successfully. Test successful')


def __get_customer_using_id__(request_manager, customer_id, extra_path=None):
    return request_manager.get(
        common_path + "/" + str(customer_id) + ("/" + str(extra_path) if extra_path is not None else ''))


def __extract_customer_id__(customer_response):
    list_custom = customer_response.json_r["_embedded"]["customer"]
    customer = list(list_custom)[random.randint(0, len(list_custom) - 1)]
    customer_id = str(customer["id"])
    return {"customer_id": customer_id, "customer": customer}
