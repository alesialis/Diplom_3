from selenium.webdriver.common.by import By


class Locators:
    # личный кабинет
    PROFILE_BUTTON = (By.XPATH, '//p[contains(text(), "Личный Кабинет")]')
    # email
    EMAIL_LOGIN = (By.XPATH, '//label[text()="Email"]/following-sibling::*')
    # password
    PASSWORD_LOGIN = (By.XPATH, '//input[@name="Пароль"]')
    # логин в ЛК
    PROFILE_BUTTON_LOGIN = (By.XPATH, '//button[contains(text(), "Войти")]')
    # кнопка Восстановить пароль
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")
    # кнопка подтверждения действия Восстановить пароль
    RESTORE_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    # поле email при восстановлении пароля
    RESTORE_PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@name="name"]')
    # текст раздела Восстановление пароля
    RESTORE_PASSWORD_HEADER_WORD = (By.XPATH, "//h2[text()='Восстановление пароля']")
    # кнопка подтверждения действия Восстановить пароль - вторая страница
    RESTORE_PASS_CONFIRM_BUTTON_NEXT = (By.XPATH, "//button[text()='Восстановить']")
    # поле new password
    RESTORE_PASSWORD_INPUT_NEW_PASS_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")
    # иконка показать/скрыть пароль
    RESTORE_PASSWORD_VISIBILITY = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    RESTORE_PASS_UNVISIBLE = (By.XPATH, '//input[@name="Введите новый пароль"]')
    # кнопка Конструктор в ЛК
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # кнопка Выход из ЛК
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    # кнопка История заказов в ЛК
    USER_PROFILE_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    # список Истории заказов
    USER_PROFILE_HISTORY_LIST = (By.XPATH, "//div[@class='OrderHistory_orderHistory__qy1VB']")
    # кнопка Лента заказов
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    # хэдер Ленты заказов
    ORDER_FEED_HEADER_TEXT = (By.XPATH, "//div/h1[text()='Лента заказов']")
    # хэдер Конструктора
    ORDER_CONSTRUCTOR_HEADER_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']")
    # булочка для теста
    CRATOR_BUN = (By.XPATH, "//img[@alt='Краторная булка N-200i']")
    # текст - детали ингредиента
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
    # текст - название ингредиента
    INGREDIENT_NAME = (By.XPATH, "//div/p[text()='Краторная булка N-200i']")
    # скрыть ингредиент
    INGREDIENT_POP_UP_CLOSE = (By.XPATH, "//div/section[1]/div[1]/button")
    # контекстное окно
    INGREDIENT_CONTEXT_WINDOW = (By.XPATH, '//div[@class="Modal_modal__contentBox__sCy8X pt-10 pb-15"]')
    # корзина
    TARGET_BASKET = (By.XPATH, "//div/main/section[2]/ul/li[1]")
    # счетчик ингредиента
    INGREDIENT_TOTAL_NUMBER = (By.XPATH, "//ul[1]/a[2]/div[1]/p")
    # текст идентификатора заказа
    ORDER_CREATED_TEXT = (By.XPATH, "//p[text()='идентификатор заказа']")
    # кнопка создать заказ
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_CONTAINER = (By.XPATH, '//*[@id="root"]/div/section/div[1]')
    # верхний заказ в ленте
    TOP_ORDER_IN_FEED = (By.XPATH, "//main/div/div/ul/li[1]")
    # окно с деталями заказа
    ORDER_DETAILS_WINDOW_FEED = (By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
    # номер заказа в истории
    ORDER_NUMBER_HISTORY = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul/li[1]/a/div[1]/p[1]')
    # кнопка закрыть заказ
    CLOSE_ORDER = (By.XPATH, "//div/section/div[1]/button")
    # номер заказа в ленте
    ORDER_FEED_NUMBER = (By.XPATH, "//li[1]/a/div[1]/p[1]")
    # заказы - за все время
    ALL_TIME_ORDERS_NUMBER = (By.XPATH, "//div/div[2]/p[2][@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    # заказы - сегодня
    TODAY_ORDERS_NUMBER = (By.XPATH, "//div[3]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    # заказы - в работе
    ORDER_IN_PROGRESS = (By.XPATH, "//div/div[1]/div[1]/div[1]/ul[2]/li[1][@class='text text_type_digits-default mb-2']")

    PRELOADER_ANIMATION = (By.XPATH, '//*[@id="root"]/div/div/img')
    LOADING_HISTORY = (By.XPATH, "//div/main/div/div/div[text()='Загрузка...']")
    MODAL_OVERLAY = (By.XPATH, '//div/div[@class="Modal_modal_overlay__x2ZCr"]')