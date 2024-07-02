from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from helpers import *
from locators import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу")
    def open_page(self, url):
        return self.driver.get(url)

    @allure.step("Найти элемент")
    def find_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step("Найти элемент и кликнуть")
    def find_element_click(self, locator, time=30):
        return self.find_element(locator).click()

    @allure.step("Кликнуть Лента заказов")
    def click_order_feed(self):
        self.find_element_click(Locators.ORDER_FEED_BUTTON)

    @allure.step("Найти все элементы")
    def find_elements(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    @allure.step("Скролл и клик")
    def scroll_and_click_element(self, locator, time=30):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текущий url")
    def get_current_url(self):
        element = self.driver.current_url
        return element

    @allure.step("Ожидание скрытия элемента")
    def element_wait_invisibility(self, locator, time=30):
        element = WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))
        return element

    @allure.step("Ожидание скрытия")
    def wait_for_invisibility(self, locator):
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element(locator))

    @allure.step("Перетащить элемент")
    def drag_and_drop(self, driver, source_element, target_element):
        actions = ActionChains(driver)
        actions.drag_and_drop(source_element, target_element).perform()

    @allure.step("Ожидание кликабельности")
    def wait_for_clickable(self, locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидание доступности, скролл, клик")
    def element_to_click(self, driver, locator):
        element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Ожидание появления элемента")
    def wait_for_visibility(self, locator, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element

    @allure.step("Ожидание кликабельности, клик по элементу")
    def wait_and_click_action_chains(self, locator):
        self.wait_for_clickable(locator)
        self.element_to_click(self.driver, locator)

    @allure.step("Ожидание скрытия элемента")
    def wait_for_invisibility_preloader(self):
        self.wait_for_invisibility(Locators.PRELOADER_ANIMATION)

    @allure.step("Кликнуть Конструктор")
    def click_constructor(self):
        self.find_element_click(Locators.CONSTRUCTOR_BUTTON)

    @allure.step("Перетащить элемент - корзина")
    def drag_element_and_drop(self):
        source_locator = Locators.CRATOR_BUN
        target_locator = Locators.TARGET_BASKET
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)
        self.drag_and_drop(self.driver, source_element, target_element)

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
        self.find_element_click(Locators.PROFILE_BUTTON)

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_page(data.MAIN_PAGE_URL)

    @allure.step("Ожидание скрытия элемента - раздел история заказов")
    def wait_for_invisibility_element_history(self):
        self.wait_for_invisibility(Locators.LOADING_HISTORY)

    @allure.step("Поиск элемента и клик по скрипту")
    def find_then_click_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)