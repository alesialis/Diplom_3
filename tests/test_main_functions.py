from pages.main_functions_page import *


class TestMainFunctions:
    @allure.title("Переход по клику на «Конструктор»")
    @allure.description("Осуществляется переход на страницу конструктора бургера")
    def test_click_constructor(self, driver):
        main_functions = MainFunctionsPage(driver)
        main_functions.open_main_page()
        main_functions.wait_for_invisibility_preloader()
        main_functions.wait_then_click_action_chains_feed()
        main_functions.click_order_feed()
        main_functions.click_constructor()
        text = main_functions.get_header_constructor()
        assert driver.current_url == data.MAIN_PAGE_URL
        assert text == data.CONSTRUCTOR_TEXT

    @allure.title("Переход по клику на «Лента заказов»")
    @allure.description("Осуществляется переход на страницу ленты заказов")
    def test_click_order_feed(self, driver):
        main_functions = MainFunctionsPage(driver)
        main_functions.open_main_page()
        main_functions.wait_for_invisibility_preloader()
        main_functions.click_order_feed()
        text = main_functions.get_header_order_feed()
        assert driver.current_url == data.FEED_PAGE_URL
        assert text == data.ORDER_FEED_TEXT

    @allure.title("При клике на ингредиент появится всплывающее окно с деталями")
    @allure.description("Корректное отображение деталей конкретного ингредиента")
    def test_click_ingredient_details(self, driver):
        main_functions = MainFunctionsPage(driver)
        main_functions.open_main_page()
        main_functions.wait_for_invisibility_preloader()
        main_functions.wait_then_click_action_chains_ingredient()
        ingredient_details = main_functions.get_ingredient_details()
        ingredient_name = main_functions.get_ingredient_name()
        assert ingredient_details == data.INGREDIENT_DETAILS_TEXT
        assert ingredient_name == data.INGREDIENT_NAME_TEXT

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    @allure.description("Корректное закрытие окна деталей")
    def test_close_ingredient_details(self, driver):
        main_functions = MainFunctionsPage(driver)
        main_functions.open_main_page()
        main_functions.wait_for_invisibility_preloader()
        main_functions.click_bun()
        main_functions.close_ingredient_details()
        element = main_functions.find_ingredient_details_window()
        assert not element.is_displayed()

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается")
    @allure.description("Корректное добавление ингредиента и пересчет корзины")
    def test_add_ingredient_changes_amount(self, driver):
        main_functions = MainFunctionsPage(driver)
        main_functions.open_main_page()
        main_functions.wait_for_invisibility_preloader()
        main_functions.drag_element_and_drop(Locators.CRATOR_BUN, Locators.TARGET_BASKET)
        total_after = main_functions.get_total_sum()
        assert total_after != 0

    @allure.title("Залогиненный пользователь может оформить заказ")
    @allure.description("Корректное оформление заказа пользователем")
    def test_make_order_by_login_user(self, driver):
        main_functions = MainFunctionsPage(driver)
        main_functions.open_main_page()
        main_functions.wait_for_invisibility_preloader()
        main_functions.click_user_profile()
        main_functions.user_login()
        main_functions.drag_element_and_drop(Locators.CRATOR_BUN, Locators.TARGET_BASKET)
        main_functions.click_create_order()
        main_functions.wait_for_visibility_container()
        result = main_functions.get_order_details()
        assert result == data.MADE_ORDER_TEXT
