from pages.user_profile_page import *


class TestUserProfile:
    @allure.title("Переход по клику на «Личный кабинет»")
    @allure.description("Корректный переход к нужному разделу сайта")
    def test_click_user_profile_on_main_page(self, driver):
        user_profile = UserProfilePage(driver)
        user_profile.open_main_page()
        user_profile.wait_for_invisibility_preloader()
        user_profile.click_user_profile()
        assert user_profile.get_current_url() == data.LOGIN_PAGE_URL

    @allure.title("Переход в раздел «История заказов»")
    @allure.description("Корректное отображение раздела при переходе")
    def test_click_order_history(self, driver):
        user_profile = UserProfilePage(driver)
        user_profile.open_main_page()
        user_profile.wait_for_invisibility_preloader()
        user_profile.click_user_profile()
        user_profile.user_login()
        user_profile.wait_for_invisibility_preloader()
        user_profile.click_user_profile()
        user_profile.click_orders_history()
        assert user_profile.get_current_url() == data.ORDER_HISTORY_PAGE_URL

    @allure.title("Выход из аккаунта")
    @allure.description("При выходе из аккаунта осуществляется переход на страницу логина")
    def test_user_logout(self, driver):
        user_profile = UserProfilePage(driver)
        user_profile.open_main_page()
        user_profile.wait_for_invisibility_preloader()
        user_profile.click_user_profile()
        user_profile.user_login()
        user_profile.wait_for_invisibility_preloader()
        user_profile.wait_for_clickable_profile()
        user_profile.click_user_profile()
        user_profile.wait_for_invisibility_preloader()
        user_profile.wait_for_clickable_logout()
        user_profile.user_profile_logout()
        user_profile.wait_for_invisibility_preloader()
        user_profile.wait_for_visibility_login()
        assert user_profile.get_current_url() == data.LOGIN_PAGE_URL
