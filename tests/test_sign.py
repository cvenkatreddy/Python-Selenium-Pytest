import allure
import pytest

from assertpy import assert_that
from tests.test_base import BaseTest


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("Sign")
@allure.story("Sign Feature Functionality")
@allure.severity(allure.severity_level.BLOCKER)
class TestSign(BaseTest):

    @allure.description("sign test")
    @allure.title("Sign Test")
    @pytest.mark.run()
    def test_valid_sign(self):
        username = self.config_reader.config_section_dict("AUT")["username"]
        self.pages['sign_page'].enter_fullname(username)
        self.pages['sign_page'].click_next()
        self.pages['sign_page'].capture_confirmation_model()
        self.pages['sign_page'].click_save()
        expected_success_message = self.json_reader.read_from_json()["sign"]["success_message"]
        assert_that(expected_success_message).is_equal_to(self.pages['sign_page'].get_success_message())
