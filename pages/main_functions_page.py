from pages.base_page import BasePage
from locators import Locators
from helpers import *


class MainFunctionsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Получить текст Лента заказов")
    def get_header_order_feed(self):
        element = self.find_element(Locators.ORDER_FEED_HEADER_TEXT).get_attribute("textContent")
        return element

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

    @allure.step("Получение данных корзины")
    def get_total_sum(self):
        element = self.find_element(Locators.INGREDIENT_TOTAL_NUMBER).text
        return element

    @allure.step("Ожидание элемента и клик - лента заказов")
    def wait_then_click_action_chains_feed(self):
        self.wait_and_click_action_chains(Locators.ORDER_FEED_BUTTON)

    @allure.step("Ожидание элемента и клик - ингредиент")
    def wait_then_click_action_chains_ingredient(self):
        self.wait_and_click_action_chains(Locators.CRATOR_BUN)




