import pytest

from assertpy import *


class Response():
    def __init__(self, logger, request_manager, schemavalidator_fixture):
        self.logger = logger
        self.request_manager = request_manager
        self.schemavalidator_fixture = schemavalidator_fixture
        self.module_name = ''
        self.schema = ''

    def __validate__(self, request_response=None, *content_type_values):
        with soft_assertions():
            content_type = request_response.headers.get("Content-Type")
            if len(content_type_values) == 0:
                assert_that(content_type,
                            f'Content-Type is not correct for module "{self.module_name}" ').contains_ignoring_case(
                    'application/json', 'charset=UTF-8')
            else:
                self.logger.error(f'Content-Type is not correct for module "{self.module_name}" ')
                assert_that(content_type,
                            f'Content-Type is not correct for module "{self.module_name}" ').contains_ignoring_case(
                    content_type_values)
            # Validate that schema response match with expected schema
            self.schemavalidator_fixture.validate_schema_response(request_response.json_r, self.schema)
        self.logger.info("User created successfully")

    def validate_valid_status_code(self, request_response=None, module_name="", schema={}, status_code=None,
                                   *content_type_values):
        self.module_name = module_name
        self.schema = schema
        with soft_assertions():
            min = (200 if status_code is None else status_code)
            max = (208 if status_code is None else status_code)
            assert_that(request_response.status_code,
                        f'Error detected during execution of module under test "{module_name}". Status code no valid:  {str(request_response.text)}') \
                .is_between(min, max)
            assert_that("Internal Server Error".lower() in str(request_response.text).lower(),
                        "An Internal Server Error was detected in a valid response.").is_false()
            # self.request_manager.valid_status_code() if status_code is None else status_code)
            self.__validate__(request_response, *content_type_values)

    def validate_invalid_status_code(self, request_response=None, module_name="", schema={}, *content_type_values):
        self.module_name = module_name
        self.schema = schema
        with soft_assertions():
            assert_that(request_response.status_code,
                        f'Error detected during execution of module under test "{module_name}":  {str(request_response.text)}') \
                .is_not_equal_to(self.request_manager.valid_status_code())
        self.__validate__(request_response, *content_type_values)


@pytest.fixture
def validate_response(logger, request_manager, schemavalidator_fixture):
    return Response(logger, request_manager, schemavalidator_fixture)
