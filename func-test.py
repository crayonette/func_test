# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser Chrome"
# или "Open Browser [Chrome]"
# на ваш выбор.


def get_func_name(func, *args):
    func_name = func.__name__.title().replace('_', ' ').title()
    print(func_name, end=" ")
    print(*args)


def open_browser(browser_name):
    get_func_name(open_browser, browser_name)

def go_to_companyname_homepage(page_url):
    get_func_name(go_to_companyname_homepage, page_url)

def find_catalogue_button_on_main_page(page_url, button_text):
    get_func_name(find_catalogue_button_on_main_page, page_url, button_text)

open_browser("Chrome")
go_to_companyname_homepage("https://www.ozon.ru/")
find_catalogue_button_on_main_page("https://www.ozon.ru/", "Каталог")