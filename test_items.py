import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.get(link)

    time.sleep(30)  # for your comfort :P

    basket_button = browser.find_elements_by_css_selector("button[type='submit'].btn-add-to-basket")
    assert basket_button, "Error: basket button does not exist"


