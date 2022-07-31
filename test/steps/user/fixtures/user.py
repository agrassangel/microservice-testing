import string

import faker
import pytest
from faker import Faker
import random
from test.common.file_manager import read_file


class UserFail():
    def __init__(self):
        super().__init__()
        value = read_file("users")
        self.faker = Faker()
        self.profile_list = []
        self.user_errors = read_file("users")["field_errors"]
        self.username = ""
        self.password = ""
        self.email = ""
        self.id = ""

    def get_fail_user_profile(self, field):
        if field in ["username", "password"]:
            # Max limited
            self.__create_set_of_fail_profile__(field, 20, 40)
            # Empty
            self.__create_set_of_fail_profile__(field, 0, 0)
        elif field in ["mail"]:
            choice_ra = random.choice(string.ascii_letters)
            username = ''.join(choice_ra for x in range(6))
            domain = ''.join(choice_ra for x in range(5))
            extension = ''.join(choice_ra for x in range(3))
            # Missing domain
            self.__create_set_of_fail_profile__(field, 0, 0, username.join('@'))
            # Missing extension
            self.__create_set_of_fail_profile__(field, 0, 0, username.join(f'@{domain}.'))
            # Missing username
            self.__create_set_of_fail_profile__(field, 0, 0, ''.join(f'@{domain}.{extension}'))
            # Username with spaces
            self.__create_set_of_fail_profile__(field, 0, 0,
                                                username.join(f' {username}@{domain}.{extension}'))
            # Domain with spaces
            self.__create_set_of_fail_profile__(field, 0, 0,
                                                username.join(f'@{domain} .{extension}'))
        return self.profile_list

    def __create_set_of_fail_profile__(self, field, x: int, y: int, value=""):
        profile = self.faker.simple_profile()
        profile["invalid_field"] = field
        profile["password"] = self.faker.password()
        if x == 0:
            profile[field] = value
        else:
            profile[field] = self.faker.paragraph(nb_sentences=random.randint(x, y))
        self.profile_list.append(profile)

    def register_new_user(self):
        return {"username": self.username,
                "password": self.password,
                "email": self.email}

    def set_user_id(self, identification_token):
        self.id = identification_token


@pytest.fixture
def user_fail_profile():
    return UserFail()
