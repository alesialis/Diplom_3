import allure
from pages.base_page import BasePage
from locators import Locators
from helpers import *


class MainFunctionsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_page(data.MAIN_PAGE_URL)

    @allure.step("Кликнуть Лента заказов")
    def click_order_feed(self):
        self.find_element_click(Locators.ORDER_FEED_BUTTON)

    @allure.step("Ожидание скрытия элемента")
    def wait_for_invisibility_preloader(self):
        self.wait_for_invisibility(Locators.PRELOADER_ANIMATION)

    @allure.step("Получить текст Лента заказов")
    def get_header_order_feed(self):
        element = self.find_element(Locators.ORDER_FEED_HEADER_TEXT).get_attribute("textContent")
        return element

    @allure.step("Кликнуть Конструктор")
    def click_constructor(self):
        self.find_element_click(Locators.CONSTRUCTOR_BUTTON)

    @allure.step("Получить текст Конструктор")
    def get_header_constructor(self):
        element = self.find_element(Locators.ORDER_CONSTRUCTOR_HEADER_TEXT).text
        return element

    @allure.step("Кликнуть по ингредиенту")
    def click_bun(self):
        self.find_element_click(Locators.CRATOR_BUN)

    @allure.step("Получить детали ингредиента")
    def get_ingredient_details(self):
        element = self.find_element(Locators.INGREDIENT_DETAILS).text
        return element

    @allure.step("Получить название ингредиента")
    def get_ingredient_name(self):
        element = self.find_element(Locators.INGREDIENT_NAME).text
        return element

    @allure.step("Закрыть детали ингредиента")
    def close_ingredient_details(self):
        self.find_element_click(Locators.INGREDIENT_POP_UP_CLOSE)

    @allure.step("Ожидание окна с деталями ингредиента")
    def find_ingredient_details_window(self):
        element = self.element_wait_invisibility(Locators.INGREDIENT_CONTEXT_WINDOW)
        return element

    @allure.step("Перетащить элемент - корзина")
    def drag_element_and_drop(self, source_locator, target_locator):
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)
        self.drag_and_drop(self.driver, source_element, target_element)

    @allure.step("Получение данных корзины")
    def get_total_sum(self):
        element = self.find_element(Locators.INGREDIENT_TOTAL_NUMBER).text
        return element

    @allure.step("Логин пользователя")
    def user_login(self):
        log_pass = create_new_user_return_log_pass()
        email, password, _ = log_pass
        self.find_element(Locators.EMAIL_LOGIN).send_keys(email)
        self.find_element(Locators.PASSWORD_LOGIN).send_keys(password)
        self.find_element(Locators.PROFILE_BUTTON_LOGIN).click()

    @allure.step("Кликнуть Создать заказ")
    def click_create_order(self):
        self.find_element_click(Locators.CREATE_ORDER_BUTTON)

    @allure.step("Получить детали заказа")
    def get_order_details(self):
        element = self.find_element(Locators.ORDER_CREATED_TEXT).text
        return element

    @allure.step("Кликнуть ЛК")
    def click_user_profile(self):
        self.find_element(Locators.PROFILE_BUTTON).click()

    @allure.step("Ожидание элемента и клик - лента заказов")
    def wait_then_click_action_chains_feed(self):
        self.wait_and_click_action_chains(Locators.ORDER_FEED_BUTTON)

    @allure.step("Ожидание элемента и клик - ингредиент")
    def wait_then_click_action_chains_ingredient(self):
        self.wait_and_click_action_chains(Locators.CRATOR_BUN)

    @allure.step("Ожидание элемента - оформление заказа")
    def wait_for_visibility_container(self):
        self.wait_for_visibility(Locators.ORDER_CONTAINER)



