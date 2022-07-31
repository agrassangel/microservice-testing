from pytest_bdd import scenarios, given, when, then
from .fixtures.schemas.catalogue_schema import *
import random
from assertpy import soft_assertions, assert_that

scenarios("catalogue/catalogue.feature")
common_path = "/catalogue"


@given("User has a catalogue", target_fixture="catalogue_response")
@when("User attempts to get whole catalogues list", target_fixture="catalogue_response")
def get_all_catalogue(request_manager):
    return request_manager.get(common_path)


@then("System response with the catalogues")
def check_catalogue_response(catalogue_response, logger, validate_response):
    __get_catalogue__(validate_response, catalogue_response, logger, catalogue_response_schema,
                      f' Get catalogue was successful. Test successful')


@when("User attempts to get catalogues by its id", target_fixture="catalogue_response_id")
def get_catalogue_by_id(catalogue_response, request_manager):
    catalogue = __extract_catalogue_id__(catalogue_response)
    return request_manager.get(common_path + f'/{str(catalogue["id"])}')


@then("System response with the catalogue selected")
def check_catalogue_response_by_id(catalogue_response_id, validate_response, logger):
    __get_catalogue__(validate_response, catalogue_response_id, logger, catalogue_by_id_response_schema,
                      f' Get catalogue by id was successful. Test successful')


def __get_catalogue__(validate_response, catalogue_response, logger, schema, msg=""):
    validate_response.validate_valid_status_code(catalogue_response,
                                                 f'GET catalogue "{common_path}" should be performed',
                                                 schema)
    logger.info(msg)


def __extract_catalogue_id__(catalogue_response):
    list_catalogue = catalogue_response.json_r
    catalogue = list(list_catalogue)[random.randint(0, len(list_catalogue) - 1)]
    customer_id = str(catalogue["id"])
    return {"id": customer_id, "catalogue": catalogue}


@when("User attempts to get total of catalogue", target_fixture="catalogue_response_size")
def get_total_catalogue(request_manager):
    return request_manager.get(common_path + "/size")


@then("System response with the total of catalogue available")
def step_impl(catalogue_response_size, logger, validate_response, request_manager):
    list_catalogue = request_manager.get(common_path)
    with soft_assertions():
        validate_response.validate_valid_status_code(catalogue_response_size, common_path,
                                                     catalogue_by_size_response_schema)
        assert_that(int(catalogue_response_size.json_r["size"]),
                    " Total of catalogue doesnt match with the list of catalogues").is_equal_to(
            len(list_catalogue.json_r))
    logger.info(" GET total catalogue size successful. Test successfully")


@when("User attempts to get all tags", target_fixture="tags_response")
def get_catalogue_tags(request_manager):
    return request_manager.get(common_path + "/tags")


@then("System returns all tags available")
def check_tags(tags_response, logger, validate_response):
    """
       Test on hitting People GET API, we get a user named kent in the list of people
       """
    logger.info(" GET tags successful. Test successfully")
    validate_response.validate_valid_status_code(tags_response, common_path + " and tags",
                                                 catalogue_tags_response_schema)

