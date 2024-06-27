from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        return self.driver.get(url)

    def find_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_element_click(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator)).click()

    def find_elements(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def scroll_and_click_element(self, locator, time=30):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def get_current_url(self):
        return self.driver.get_current_url()

    def element_wait_invisibility(self, locator, time=30):
        element = WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))
        return element

    def wait_for_invisibility(self, locator):
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element(locator))

    def drag_and_drop(self, driver, source_element, target_element):
        actions = ActionChains(driver)
        actions.drag_and_drop(source_element, target_element).perform()

    def wait_for_clickable(self, locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))

    def element_to_click(self, driver, locator):
        element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def wait_until_clickable(self, locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))

    def wait_for_visibility(self, locator, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element

    def wait_and_click_action_chains(self, locator):
        self.wait_until_clickable(locator)
        self.element_to_click(self.driver, locator)
