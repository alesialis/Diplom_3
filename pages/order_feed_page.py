from pages.base_page import BasePage
from locators import Locators
from helpers import *


class FeedOrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    @allure.step("Кликнуть на заказ")
    def click_top_order(self):
        self.find_element_click(Locators.TOP_ORDER_IN_FEED)


    @allure.step("Получить детали заказа")
    def get_order_details(self):
        element = self.find_element(Locators.ORDER_DETAILS_WINDOW_FEED)
        return element

    @allure.step("Кликнуть Создать заказ")
    def click_create_order_wait(self):
        self.click_create_order()
        self.wait_for_visibility(Locators.CLOSE_ORDER)

    @allure.step("Закрыть заказ")
    def close_order(self):
        self.find_element_click(Locators.CLOSE_ORDER)

    @allure.step("Получить число заказов")
    def get_order_number(self):
        elements = self.find_elements(Locators.ORDER_FEED_NUMBER)
        numbers = [element.text for element in elements]
        return numbers

    @allure.step("Получить число в Истории заказов")
    def get_order_number_history(self):
        element = self.find_element(Locators.ORDER_NUMBER_HISTORY).text
        return element

    @allure.step("Получить число заказов за все время")
    def get_number_all_orders(self):
        element = self.wait_for_visibility(Locators.ALL_TIME_ORDERS_NUMBER)
        return element.text

    @allure.step("Ожидание кликабельности Ленты заказов")
    def wait_until_clickable_feed(self):
        self.wait_for_clickable(Locators.ORDER_FEED_BUTTON)

    @allure.step("Получить число заказов за сегодня")
    def get_orders_number_current(self):
        element = self.wait_for_visibility(Locators.TODAY_ORDERS_NUMBER)
        return element.text

    @allure.step("Ожидание статуса 'в работе'")
    def wait_order_in_progress(self):
        self.wait_for_clickable(Locators.ORDER_IN_PROGRESS)

    @allure.step("Получить со статусом 'в работе'")
    def get_order_number_in_progress(self):
        element = self.find_element(Locators.ORDER_IN_PROGRESS)
        return element

    @allure.step("Кликнуть Историю заказов")
    def click_order_history(self):
        locator = Locators.USER_PROFILE_HISTORY_BUTTON
        self.wait_for_visibility(locator)
        self.wait_for_clickable(locator)
        self.find_then_click_js(locator)


    @allure.step("Ожидание элемента - скрыть заказ")
    def wait_for_invisibility_element_close_order(self):
        self.wait_for_invisibility(Locators.CLOSE_ORDER)

    @allure.step("Ожидание скрытия элемента - раздел заказы")
    def wait_for_invisibility_element_order(self):
        self.wait_for_invisibility(Locators.MODAL_OVERLAY)




