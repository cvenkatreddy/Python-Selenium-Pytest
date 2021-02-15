import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignPage(BasePage):
    """ Scrive Sign Page """
    ARROW_LINK = (By.XPATH, "//span[text()='ARROW']")
    ARROW_ICON_IMAGE = (By.CSS_SELECTOR, "path.actioncolor")
    USERNAME_FIELD = (By.CSS_SELECTOR, "#name")
    NEXT_BUTTON = (By.XPATH, "//div/span[contains(text(), 'Next')]")
    SIGN_BUTTON = (By.XPATH, "//div/span[text()='Sign']")
    SUCCESS_MESSAGE = (By.XPATH, "//h1/span[text()='Document signed!']")
    CONFIRMATION_MODEL = "div.section.sign.above-overlay"

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Enter Full name")
    def enter_fullname(self, username):
        self.click(self.ARROW_LINK)
        self.fill_text(self.USERNAME_FIELD, username)

    @allure.step("Click Next")
    def click_next(self):
        self.scroll_to_bottom()
        self.click(self.NEXT_BUTTON)

    @allure.step("Capture Confirmation Model")
    def capture_confirmation_model(self):
        self.save_confirmation_model(self.CONFIRMATION_MODEL)

    @allure.step("Click Save")
    def click_save(self):
        self.click(self.SIGN_BUTTON)

    @allure.step("Get success message")
    def get_success_message(self):
        self.wait_until_page_loaded()
        return self.get_text(self.SUCCESS_MESSAGE)

    @allure.step("Get page title")
    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)
