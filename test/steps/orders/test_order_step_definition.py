from pytest_bdd import scenarios, given, when, then
from .fixtures.schemas.order_schema import *
import random
from assertpy import soft_assertions, assert_that
from .fixtures.schemas.order_schema import *

scenarios("orders/orders.feature")
common_path = "/orders"


@when("User attempts to get orders", target_fixture="orders_response")
@when("User attempts to get orders without being logged", target_fixture="auth_fails_response")
def get_orders(request_manager):
    return request_manager.get(common_path)


@then("System will display all orders")
def check_orders(logger, orders_response, validate_response):
    validate_response.validate_valid_status_code(orders_response, f'GET orders "{common_path}" should be performed.',
                                                 get_orders_response_schema, 200,
                                                 'application/hal+json', "charset=UTF-8")
    logger.info(" GET orders successful. Test passed")
