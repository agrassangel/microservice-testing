import pytest
from faker import Faker
import random


class Cards():

    def __init__(self):
        super()


#     TODO: Implement once get the business rules

@pytest.fixture
def cards_fail_fixture():
    return Cards()
