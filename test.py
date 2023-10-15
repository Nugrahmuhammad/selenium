import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from constants import (
    WOMEN_BUTTON,
    WIDGET_PRODUCT_1,
    SIZE_BUTTON_XS,
    COLLOR_BUTTON_BLUE,
    ADD_CART_BUTTON,
    CART_BUTTON,
    CHECKOUT_BUTTON,
    ADDED_ELEMENT,
    EMAIL_FORM,
    WIDGET_PRODUCT_2,
    WIDGET_PRODUCT_3,
    COLLOR_BUTTON_PURPLE,
    SIGN_BUTTON,
    SIGN_EMAIL_FORM,
    PASS,
    SUBMIT_SIGN,
    STREET_ADDRESS_CHECKOUT_FORM,
    CITY_CHECKOUT_FORM,
    ZIP_CHECKOUT_FORM,
    INDONESIA,
    PHONE_CHECKOUT_FORM,
    NEXT_BUTTON,
    PLACE_ORDER_BUTTON_CHECKOUT,
    THANKS_ELEMENT,
    PHONE_ELEMENT,
)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    
    

@allure.step("Open the marketplace")
def test_open_magento(driver):
        # User opens the marketplace
    driver.maximize_window()
    driver.get("https://magento.softwaretestingboard.com/")
    

@allure.step("User does SIGN")
def test_sign(driver):

    test_open_magento(driver)

    click_sign = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, SIGN_BUTTON))
    )
    click_sign.click()

    input_email_sign = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, SIGN_EMAIL_FORM))
    )
    
    input_email_sign.send_keys("nugrah@yopmail.com")

    input_pass_sign = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, PASS))
    )
    
    input_pass_sign.send_keys("Test1234")

    click_sign_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, SUBMIT_SIGN))
    )
    click_sign_button.click()

@allure.step("User add product and check out")
def test_add_product(driver):

    test_sign(driver)

    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, WOMEN_BUTTON))
    )
    element.click()

    # Repeat the product selection and add-to-cart steps for WIDGET_PRODUCT_1, WIDGET_PRODUCT_2, and WIDGET_PRODUCT_3
    for product_xpath in [WIDGET_PRODUCT_1, WIDGET_PRODUCT_2, WIDGET_PRODUCT_3]:
        product = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, product_xpath))
        )
        product.click()

        select_size = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, SIZE_BUTTON_XS))
        )
        select_size.click()

        select_color = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, COLLOR_BUTTON_BLUE if product_xpath == WIDGET_PRODUCT_1 else COLLOR_BUTTON_PURPLE))
        )
        select_color.click()

        add_cart = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ADD_CART_BUTTON))
        )
        add_cart.click()

        wait_added = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, ADDED_ELEMENT))
        )
        assert wait_added is not None, "Element not found"

        driver.back()

    click_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, CART_BUTTON))
    )
    click_cart.click()

    
    proceed_checkout = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, CHECKOUT_BUTTON))
    )
    proceed_checkout.click()

    time.sleep(10)
    # Add the remaining steps for entering address and placing an order
    click_next = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, NEXT_BUTTON))
    )
    click_next.click()

    phone_is_correct = driver.find_element_by_xpath(PHONE_ELEMENT)
    element_phone = phone_is_correct.text
    assert element_phone == "21312312312"

    time.sleep(5)

    click_placeorder = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, PLACE_ORDER_BUTTON_CHECKOUT))
    )
    click_placeorder.click()

    time.sleep(5)

    find_element = driver.find_elements(By.XPATH, THANKS_ELEMENT)

    assert find_element, "Element is not present"
    
    allure.attach("Test passed successfully!", name="Test Status", attachment_type=allure.attachment_type.TEXT)

    driver.quit()

if __name__ == "__main__":
    pytest.main()
