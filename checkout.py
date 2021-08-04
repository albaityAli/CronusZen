from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Profiles:
    def __init__(self, email, fname, lname, postcode, address, phone, city, card_number, security_code, expiry,
                 name_on_card):
        self.email = email
        self.fname = fname
        self.lname = lname
        self.postcode = postcode
        self.address = address
        self.phone = phone
        self.city = city
        self.card_number = card_number
        self.security_code = security_code
        self.expiry = expiry
        self.name_on_card = name_on_card

    def type(self, xpath, keys):
        return driver.find_element_by_xpath(xpath).send_keys(keys)

    def press(self, xpath):
        x = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        x.click()

    def buy(self, count):
        if count != 1:
            return

        global driver
        driver = webdriver.Chrome(executable_path=r"C:\Users\aalba\OneDrive\Desktop\chromedriver.exe")
        driver.get(
            "https://collectiveminds-uk.myshopify.com/products/cronus-zen")
        self.press("//*[@id='AddToCartForm-product-template']/div[2]/div/div/div/div/button[1]")

        driver.implicitly_wait(8)

        driver.find_element_by_xpath("//*[@id='checkout_email_or_phone']").send_keys(self.email)


        self.type("//*[@id='checkout_shipping_address_first_name']", self.fname)
        self.type("//*[@id='checkout_shipping_address_last_name']", self.lname)
        self.type("//*[@id='checkout_shipping_address_address1']", self.address)
        self.type("//*[@id='checkout_shipping_address_city']", self.city)
        self.type("//*[@id='checkout_shipping_address_phone']", self.phone)
        self.type("//*[@id='checkout_shipping_address_zip']", self.postcode)

        self.press("//*[@id='continue_button']")

        self.press("//*[@id='continue_button']")

        driver.switch_to.frame(driver.find_element_by_xpath("//*[contains(@id, 'card-fields-number-')]"))
        for letter in self.card_number:
            driver.find_element_by_id("number").send_keys(letter)
            time.sleep(0.05)
        driver.switch_to.parent_frame()

        driver.switch_to.frame(driver.find_element_by_xpath("//*[contains(@id, 'card-fields-name-')]"))
        driver.find_element_by_id("name").send_keys(self.card_number)
        driver.switch_to.parent_frame()

        driver.switch_to.frame(driver.find_element_by_xpath("//*[contains(@id, 'card-fields-expiry-')]"))
        for num in self.expiry:
            driver.find_element_by_id("expiry").send_keys(num)
            time.sleep(0.05)
        driver.switch_to.parent_frame()

        driver.switch_to.frame(driver.find_element_by_xpath("//*[contains(@id, 'card-fields-verification_value-')]"))
        driver.find_element_by_id("verification_value").send_keys(self.security_code)
        driver.switch_to.parent_frame()

        self.press("//*[@id='continue_button']")


        try:
            order = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/main/div[1]/div[1]/div[2]/div/div[1]/div[2]/h2")))
            if order.text == "Your order is successful":
                url = driver.current_url()
                return ["successful", self.name_on_card, self.email, url]
        except:
            return ["failed", self.name_on_card, self.email]








