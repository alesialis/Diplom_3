from pages.password_recovery_page import *
from helpers import *


class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    @allure.description("Корректный переход на страницу")
    def test_open_password_recovery_by_click(self, driver):
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.open_main_page()
        password_recovery.wait_for_invisibility_preloader()
        password_recovery.click_user_profile()
        password_recovery.click_password_recovery()
        assert driver.current_url == data.FORGOT_PASSWORD_PAGE_URL

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    @allure.description("Переход на страницу ввода кода из письма при клике на восстановление пароля")
    def test_input_email_reset_page(self, driver):
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.open_main_page()
        password_recovery.wait_for_invisibility_preloader()
        password_recovery.click_user_profile()
        password_recovery.click_password_recovery()
        password_recovery.input_user_email()
        password_recovery.click_confirm()
        password_recovery.wait_for_visibility_icon()
        assert driver.current_url == data.RESET_PASSWORD_PAGE_URL

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    @allure.description("Корректное поведение иконки на странице восстановления пароля")
    def test_password_recovery_icon_makes_field_shown(self, driver):
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.open_main_page()
        password_recovery.wait_for_invisibility_preloader()
        password_recovery.click_user_profile()
        password_recovery.click_password_recovery()
        password_recovery.input_user_email()
        password_recovery.click_confirm()
        password_recovery.input_new_password()
        element_before = password_recovery.get_elements_attribute(Locators.RESTORE_PASS_UNVISIBLE)
        password_recovery.click_password_icon()
        element_after = password_recovery.get_elements_attribute(Locators.RESTORE_PASS_UNVISIBLE)
        assert element_after != element_before
