import time
def test_check_basket_button_exists(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/') 
    time.sleep(30)
    assert browser.find_elements_by_css_selector(".btn-add-to-basket"), 'button is not exist'