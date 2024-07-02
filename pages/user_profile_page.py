from pages.base_page import BasePage
from helpers import *
from locators import Locators


class UserProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Открыть Историю Заказов")
    def click_orders_history(self):
        self.scroll_and_click_element(Locators.USER_PROFILE_HISTORY_BUTTON)

    @allure.step("Ожидание кликабельности - история")
    def wait_for_clickable_history(self):
        self.wait_for_clickable(Locators.USER_PROFILE_HISTORY_BUTTON)

    @allure.step("Ожидание появления - история")
    def wait_for_visibility_history(self):
        self.wait_for_visibility(Locators.USER_PROFILE_HISTORY_LIST)

    @allure.step("Ожидание кликабельности - ЛК")
    def wait_for_clickable_profile(self):
        self.wait_for_clickable(Locators.PROFILE_BUTTON)

    @allure.step("Ожидание кликабельности - выход из ЛК")
    def wait_for_clickable_logout(self):
        self.wait_for_clickable(Locators.LOGOUT_BUTTON)

    @allure.step("Выход из ЛК")
    def user_profile_logout(self):
        self.wait_for_visibility(Locators.LOGOUT_BUTTON)
        self.find_element_click(Locators.LOGOUT_BUTTON)

    @allure.step("Ожидание видимости - войти в ЛК")
    def wait_for_visibility_login(self):
        self.wait_for_visibility(Locators.PROFILE_BUTTON_LOGIN)