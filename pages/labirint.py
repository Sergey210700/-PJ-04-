import os
from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class LabirintPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'
        super().__init__(web_driver, url)


# ----------------------------------------= локаторы для строки поиска --------------------------------------------------

    LOCATOR_SEARCH_BAR = WebElement(id='search-field')
    LOCATOR_SEARCH_BAR_BTN = WebElement(class_name='b-header-b-search-e-btn')


# -------------------------------------- локаторы тестов корзины ------------------------------------------------

    # локатор добавить в отложенное
    LOCATOR_LINK_POSTPONED = WebElement(class_name='fave')

    # локатор счетчика отложено
    LOCATOR_COUNTER_POSTPONED = WebElement(css_selector='.b-header-b-personal-e-icon-count-m-putorder.basket-in-dreambox-a')

    # локатор книги
    LOCATOR_BOOK_DEAD = WebElement(xpath='//img[@src="https://img4.labirint.ru/rc/6d6c66d9efe7891957aa3b979e308c60/'
                                         '363x561q80/books84/833976/cover.jpg?1637666730"]')
    # кнопка добавить в корзину
    LOCATOR_BTN_ADD_TO_CART = WebElement(css_selector='.btn.btn-small.btn-primary.btn-buy')

    # ссылка очистить корзину
    LOCATOR_LINC_CLEAR_TO_CART = WebElement(xpath='//a[@class="b-link-popup"]')

    # ссылка восстановить удаленное
    LOCATOR_LINC_CLEAR_CART_BACK_UP = WebElement(css_selector='.b-link-popup.g-alttext-deepblue')

    # локатор корзины
    LOCATOR_BTN_CART = WebElement(css_selector='.b-header-b-personal-e-list-item.have-dropdown.last-child')

    # локатор счетчика корзины
    LOCATOR_COUNTER_CART = WebElement(css_selector='.b-header-b-personal-e-icon-count-m-cart.basket-in-cart-a')

    # локатор пустой корзины
    LOCATOR_EMPTY_CART = WebElement(xpath='//span[@class="g-alttext-small g-alttext-grey g-alttext-head" and '
                                          'contains (text(), "Ваша корзина пуста. Почему?")]')

# ---------------------------------- локаторы панели навигации в шапке сайта ----------------------------------------

    # Лого Лабиринт
    LOCATOR_LOGO_LABIRINT = WebElement(class_name='b-header-b-logo-e-logo')

    # верхняя панель навигации
    LOCATOR_UP_NAVIGATION_PANEL = WebElement(class_name='b-header-b-menu-e-list')

    # ссылка доставка и оплата
    LOCATOR_DELIVERY_AND_PAYMENT = WebElement(xpath='//a[@href="/help/" and @class="b-header-b-sec-menu-e-link"]')

    # ссылка сертификаты
    LOCATOR_CERTIFICATE_LINC = WebElement(xpath='//a[@href="/top/certificates/" and '
                                                '@class="b-header-b-sec-menu-e-link"]')
    # ссылка рейтинги
    LOCATOR_RATING_LINC = WebElement(xpath='//a[@href="/rating/?id_genre=-1&nrd=1"]')

    # ссылка новинки
    LOCATOR_NEWS_LINC = WebElement(xpath='//a[@href="/novelty/"]')

    # ссылка скидки
    LOCATOR_SALE_LINC = WebElement(xpath='//a[@href="/sale/"]')

    # ссылка телефонного номера
    LOCATOR_PHONE_NUMBER_LINC = WebElement(css_selector='.b-header-b-sec-menu-e-list-'
                                                        'item.have-dropdown.have-dropdown-clickable.analytics-click-js')
    # кнопка вызова по телефону
    LOCATOR_PHONE_NUMBER_BTN = WebElement(xpath='//*[@id="_support_call_number"]/a')

    # ссылка поддержка
    LOCATOR_SUPPORT_IN_FOOTER = WebElement(xpath='//a[@href="/support/" and @data-event-content="Поддержка"]')


# ----------------------------------- локаторы иконок справа от строки поиска ---------------------------------------

    # блок иконок
    LOCATOR_BLOCK_ICONS = WebElement(css_selector='.b-header-b-personal')

    # иконка сообщения
    LOCATOR_ICON_MESSAGES = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.'
                                                    'have-dropdown-touchlink.top-link-main_notification')
    # иконка мой лабиринт
    LOCATOR_ICON_MY_MAZE = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.'
                                                   'top-link-main_cabinet.js-b-autofade-wrap')
    # иконка отложено
    LOCATOR_ICON_POSTPONED = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.top-link-main_putorder')

    # кнопка сердечко Отложено
    LOCATOR_BTN_POSTPONED = WebElement(xpath='//a[@data-id_book="833976" and @data-hasqtip="4"]')

    # локатор всплывающего окна сообщения
    LOCATOR_AUTH_WINDOW = WebElement(xpath='//div[@class="js-auth__title new-auth__title" and contains'
                                           ' (text(),"Полный доступ к Лабиринту")]')

# ----------------------------------------- Локаторы блока видео ---------------------------------------------------
    # блок видео
    LOCATOR_BLOCK_VIDEO = WebElement(xpath='//span[@onclick="return false;" and contains (text(),'
                                           ' "Буктрейлеры и видеорецензии недели")]')

# ------------------------------------------------------------------------------------------------------------------

    # локатор всех элементов из поиска
    LOCATORS_SEARCH_BOOK_TITLE = ManyWebElements(css_selector='.product-title-link')

    # локатор всех элементов из поиска
    LOCATORS_CERTIFICATE_TITLES = ManyWebElements(class_name='card-column')

    # локатор всех элементов из поиска
    LOCATORS_RATING_BOOK_TITLE = ManyWebElements(css_selector='.product.need-watch')

# ------------------------------------------- локаторы номера страниц ----------------------------------------------

    # страница 6
    LOCATORS_PAGE_NUM_6 = WebElement(xpath='//a[@class="pagination-number__text" and @href="?stype=0&page=6"]')