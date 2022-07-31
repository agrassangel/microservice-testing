from cerberus import Validator
from assertpy import *
import pytest


class SchemaValidator:
    def __init__(self, url_path):
        self.schema_v = Validator(purge_unknown=True)
        v = Validator()
        self.url_path = url_path

    # def validate_register_user(self, response,):
    #     self.validate_schema_response(response, register_user)

    def validate_schema_response(self, response, schema):
        is_valid = self.schema_v.validate(response, schema=schema)
        assert_that(is_valid,
                    description=f'Errors in url path {str(self.url_path)} \n' + str(self.schema_v.errors)).is_true()


@pytest.fixture
def schemavalidator_fixture(request_manager):
    return SchemaValidator(request_manager.get_current_path())

# @pytest.fixture
# def user_profile():
#     return {}
