from pages.base_page import BasePage
from locators import Locators
from helpers import *


class PasswordRecoveryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    @allure.step("Кликнуть Восстановить пароль")
    def click_password_recovery(self):
        self.find_element_click(Locators.RESTORE_PASSWORD_BUTTON)

    @allure.step("Ввести email")
    def input_user_email(self):
        test_email = generate_email()
        element = self.find_element(Locators.RESTORE_PASSWORD_INPUT_FIELD).send_keys(test_email)
        return element

    @allure.step("Кликнуть подтвердить")
    def click_confirm(self):
        self.find_element_click(Locators.RESTORE_PASS_CONFIRM_BUTTON_NEXT)


    @allure.step("Получить заголовок")
    def get_element(self):
        element = self.find_element(Locators.RESTORE_PASSWORD_HEADER_WORD)
        return element

    @allure.step("Ввести новый пароль")
    def input_new_password(self):
        test_password = generate_random_string(10)
        element = self.find_element(Locators.RESTORE_PASSWORD_INPUT_NEW_PASS_FIELD).send_keys(test_password)
        return element

    @allure.step("Получить атрибут подсветки")
    def get_elements_attribute(self):
        element = self.find_element(Locators.RESTORE_PASS_UNVISIBLE).get_attribute('type')
        return element

    @allure.step("Кликнуть иконку видимости")
    def click_password_icon(self):
        self.find_element_click(Locators.RESTORE_PASSWORD_VISIBILITY)

    @allure.step("Ожидание иконки видимости")
    def wait_for_visibility_icon(self):
        self.wait_for_visibility(Locators.RESTORE_PASSWORD_VISIBILITY)
