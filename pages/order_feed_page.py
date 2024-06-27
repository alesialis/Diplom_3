import allure
from pages.base_page import BasePage
from locators import Locators
from helpers import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FeedOrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_page(data.MAIN_PAGE_URL)

    @allure.step("Кликнуть Лента заказов")
    def click_order_feed(self):
        self.find_element_click(Locators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть на заказ")
    def click_top_order(self):
        self.find_element_click(Locators.TOP_ORDER_IN_FEED)

    @allure.step("Ожидание скрытия элемента")
    def wait_for_invisibility_preloader(self):
        self.wait_for_invisibility(Locators.PRELOADER_ANIMATION)

    @allure.step("Получить детали заказа")
    def get_order_details(self):
        element = self.find_element(Locators.ORDER_DETAILS_WINDOW_FEED)
        return element

    @allure.step("Кликнуть ЛК")
    def click_user_profile(self):
        self.find_element_click(Locators.PROFILE_BUTTON)

    @allure.step("Логин пользователя")
    def user_login(self):
        log_pass = create_new_user_return_log_pass()
        email, password, _ = log_pass
        self.find_element(Locators.EMAIL_LOGIN).send_keys(email)
        self.find_element(Locators.PASSWORD_LOGIN).send_keys(password)
        self.find_element(Locators.PROFILE_BUTTON_LOGIN).click()

    @allure.step("Перетащить элемент - корзина")
    def drag_element_and_drop(self, source_locator, target_locator):
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)
        self.drag_and_drop(self.driver, source_element, target_element)

    @allure.step("Кликнуть Создать заказ")
    def click_create_order(self):
        self.find_element_click(Locators.CREATE_ORDER_BUTTON)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(Locators.CLOSE_ORDER))

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
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(Locators.ALL_TIME_ORDERS_NUMBER))
        return element.text

    @allure.step("Кликнуть Конструктор")
    def click_constructor(self):
        self.find_element_click(Locators.CONSTRUCTOR_BUTTON)

    @allure.step("Ожидание кликабельности Ленты заказов")
    def wait_until_clickable_feed(self):
        self.wait_until_clickable(Locators.ORDER_FEED_BUTTON)

    @allure.step("Получить число заказов за сегодня")
    def get_orders_number_current(self):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(Locators.TODAY_ORDERS_NUMBER))
        return element.text

    @allure.step("Ожидание статуса 'в работе'")
    def wait_order_in_progress(self):
        self.wait_until_clickable(Locators.ORDER_IN_PROGRESS)

    @allure.step("Получить со статусом 'в работе'")
    def get_order_number_in_progress(self):
        element = self.find_element(Locators.ORDER_IN_PROGRESS)
        return element

    @allure.step("Кликнуть Историю заказов")
    def click_order_history(self):
        locator = Locators.USER_PROFILE_HISTORY_BUTTON
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Кликнуть Ленту заказов")
    def click_order_feed_with_wait(self):
        locator = Locators.ORDER_FEED_BUTTON
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ожидание элемента - скрыть заказ")
    def wait_for_invisibility_element_close_order(self):
        self.wait_for_invisibility(Locators.CLOSE_ORDER)

    def wait_for_invisibility_element_order(self):
        self.wait_for_invisibility(Locators.MODAL_OVERLAY)

    def wait_for_invisibility_element_history(self):
        self.wait_for_invisibility(Locators.LOADING_HISTORY)


