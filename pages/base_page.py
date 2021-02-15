from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """ Wrapper for selenium operations """

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def click(self, webelement):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        self._highlight_element(el, "green")
        el.click()

    def fill_text(self, webelement, txt):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        el.clear()
        self._highlight_element(el, "green")
        el.send_keys(txt)

    def clear_text(self, webelement):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        el.clear()

    def scroll_to_bottom(self):
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_text(self, webelement):
        el = self._wait.until(expected_conditions.visibility_of_element_located(webelement))
        self._highlight_element(el, "green")
        return el.text

    def wait_until_page_loaded(self):
        old_page = self._driver.find_element_by_tag_name('html')
        yield
        self._wait.until(expected_conditions.staleness_of(old_page))

    def _highlight_element(self, webelement, color):
        original_style = webelement.get_attribute("style")
        new_style = "background-color:yellow;border: 1px solid " + color + original_style
        self._driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + new_style + "');},0);", webelement)
        self._driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + original_style + "');},400);", webelement)

    def save_confirmation_model(self, webelement):
        self._driver.find_element_by_css_selector(webelement).screenshot("screen_shot.png")
