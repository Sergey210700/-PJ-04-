from pages.labirint import LabirintPage
from config import TestData

import pytest


@pytest.mark.xfail
def test_loud_page(web_browser):
    page = LabirintPage(web_browser)
    page.wait_page_loaded()
    assert page.check_js_errors()


def test_go_to_main_page(web_browser):
    """ Проверка перехода на главную страницу """
    page = LabirintPage(web_browser)
    page.LOCATOR_SALE_LINC.click()
    page.LOCATOR_LOGO_LABIRINT.click()
    assert page.get_current_url() == TestData.base_url



def test_visible_block_icons(web_browser):
    """ Блок иконок виден на странице """
    page = LabirintPage(web_browser)
    assert page.LOCATOR_BLOCK_ICONS.is_visible()


def test_scroll_page(web_browser):
    """ Проверка скроллинга страницы """
    page = LabirintPage(web_browser)
    page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_ADVENTURE)
    page.LOCATOR_SEARCH_BAR_BTN.click()
    page.LOCATORS_PAGE_NUM_6.scroll_to_element()
    assert page.LOCATORS_PAGE_NUM_6.is_clickable()
    page.LOCATORS_PAGE_NUM_6.highlight_and_make_screenshot('scrolling.png')


def test_clic_icon_messages(web_browser):
    """ Название всплывающего окна 'Сообщения' соответствует параметрам """
    page = LabirintPage(web_browser)
    page.LOCATOR_ICON_MESSAGES.click()
    text = page.LOCATOR_AUTH_WINDOW.get_text()
    assert text == TestData.text_auth_window


def test_clic_icon_my_maze(web_browser):
    """ Название всплывающего окна 'Мой лабиринт' соответствует параметрам """
    page = LabirintPage(web_browser)
    page.LOCATOR_ICON_MY_MAZE.click()
    text = page.LOCATOR_AUTH_WINDOW.get_text()
    assert text == TestData.text_auth_window


def test_clic_icon_postponed(web_browser):
    """ Переход по кнопке Отложенное ведет на страницу Отложенное"""
    page = LabirintPage(web_browser)
    page.LOCATOR_ICON_POSTPONED.click()
    assert page.get_current_url() == TestData.postponed_url


def test_visible_up_navigation_panel(web_browser):
    """ Панель навигации видна на сайте """
    page = LabirintPage(web_browser)
    assert page.LOCATOR_UP_NAVIGATION_PANEL.is_visible()


def test_delivery_and_payment_linc(web_browser):
    """ Переход по ссылке Доставка и оплата ведет на соответствующую страницу """
    page = LabirintPage(web_browser)
    page.LOCATOR_DELIVERY_AND_PAYMENT.click()
    assert page.get_current_url() == TestData.delivery_and_payment_url


def test_certificate_linc(web_browser):
    """ Переход по ссылке Сертификаты ведет на соответствующую страницу """
    page = LabirintPage(web_browser)
    page.LOCATOR_CERTIFICATE_LINC.click()
    assert page.get_current_url() == TestData.certificate_url


def test_certificate_availability(web_browser):
    """ Проверяем что на странице сертификаты есть сертификаты """
    page = LabirintPage(web_browser)
    page.LOCATOR_CERTIFICATE_LINC.click()
    page.LOCATORS_CERTIFICATE_TITLES.scroll_to_element()
    # проверим что количество сертификатов равно 8
    assert page.LOCATORS_CERTIFICATE_TITLES.count() == 8


def test_rating_linc(web_browser):
    """ Переход по ссылке Рейтинг ведет на соответствующую страницу """
    page = LabirintPage(web_browser)
    page.LOCATOR_RATING_LINC.click()
    assert page.get_current_url() == TestData.rating_url


def test_rating_book(web_browser):
    """ Проверяем что на странице Рейтинги есть книги """
    page = LabirintPage(web_browser)
    page.LOCATOR_RATING_LINC.click()
    assert page.LOCATORS_RATING_BOOK_TITLE.count() == 60


def test_news_linc(web_browser):
    """ Переход по ссылке Новинки ведет на соответствующую страницу """
    page = LabirintPage(web_browser)
    page.LOCATOR_NEWS_LINC.click()
    assert page.get_current_url() == TestData.news_url


def test_sale_linc(web_browser):
    """ Переход по ссылке Скидки ведет на соответствующую страницу """
    page = LabirintPage(web_browser)
    page.LOCATOR_SALE_LINC.click()
    assert page.get_current_url() == TestData.sale_url


def test_phone_number_linc(web_browser):
    """ Переход по ссылке 8 800 600-95-25 """
    page = LabirintPage(web_browser)
    page.LOCATOR_PHONE_NUMBER_LINC.click()
    text = page.LOCATOR_PHONE_NUMBER_BTN.get_text()
    assert text == TestData.text_phone_number


def test_video_block(web_browser):
    """ Название блока видео соответствует параметрам """
    page = LabirintPage(web_browser)
    text = page.LOCATOR_BLOCK_VIDEO.get_text()
    assert text == TestData.text_video_block


def test_photo_product(web_browser):
    """ Проверяем что карточки в результатах поиска имеют фото """
    page = LabirintPage(web_browser)
    page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_ADVENTURE)
    page.LOCATOR_SEARCH_BAR_BTN.click()
    # проверим что атрибут src не пустой
    assert page.LOCATORS_SEARCH_BOOK_TITLE.get_attribute('src') != ''


def test_search_product_adventure(web_browser):
    """ Проверяем что поиск по запросу "Приключения" выдает результаты """
    page = LabirintPage(web_browser)
    page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_ADVENTURE)
    page.LOCATOR_SEARCH_BAR_BTN.click()
    # проверим что на странице 60 карточек книг
    assert page.LOCATORS_SEARCH_BOOK_TITLE.count() == 60


def test_search_product_adventure_error(web_browser):
    """ Проверяем что если перепутана раскладка, по запросу "Приключения", выдача правильная """
    page = LabirintPage(web_browser)
    page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_ADVENTURE_ERROR)
    page.LOCATOR_SEARCH_BAR_BTN.click()
    # проверим что в названии книг содержатся искомые слова
    for title in page.LOCATORS_SEARCH_BOOK_TITLE.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'Приключения' or 'приключения' in title(), msg


def test_add_book_in_cart(web_browser):
    """ Проверка добавления книги в корзину """
    page = LabirintPage(web_browser)
    page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_BOOK_DEAD)
    page.LOCATOR_SEARCH_BAR_BTN.click()
    page.LOCATOR_BOOK_DEAD.click()
    page.LOCATOR_BTN_ADD_TO_CART.click()
    page.LOCATOR_BTN_CART.click()
    # проверим что локатор книги виден в корзине
    assert page.LOCATOR_BOOK_DEAD.is_visible()
    # проверим что счетчик корзины изменился
    assert page.LOCATOR_COUNTER_CART.get_text() == '1'


@pytest.mark.xfail
def test_add_book_in_postponed(web_browser):
    """ Проверка добавления книги в отложенное """
    page = LabirintPage(web_browser)
    page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_BOOK_DEAD)
    page.LOCATOR_SEARCH_BAR_BTN.click()
    page.LOCATOR_BTN_POSTPONED.scroll_to_element()
    page.LOCATOR_BTN_POSTPONED.click()
    page.wait_page_loaded()
    page.LOCATOR_ICON_POSTPONED.scroll_to_element()
    assert page.LOCATOR_COUNTER_POSTPONED.get_text() == '1'