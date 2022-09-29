from re import sub
import sekrets
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.expected_conditions as EC
from selenium import webdriver
from time import sleep
import pyotp


def test_eight_components():
    # remove chrome's logs
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # create the driver
    driver = webdriver.Chrome(service=ChromeService(
        executable_path=ChromeDriverManager().install()), options=options)

    # go to the selfserve page
    driver.get("https://my.brocku.ca")
    driver.implicitly_wait(1)

    # sleep(1)

    url = driver.current_url
    title = driver.title
    # print(title)

    if (title.lower().find("sign in") != -1):
        if (url.find("microsoftonline.com")):
            assert title == "Sign in to your account"
            print("ms-signon")

            email_box = driver.find_element(
                By.XPATH, "//input[@type='email'][1]")
            email_box.send_keys(sekrets.EMAIL)

            submit_button = driver.find_element(
                By.XPATH, "//input[@type='submit'][1]")
            submit_button.click()

            WebDriverWait(driver, timeout=10).until(
                EC.url_changes(url))
            url = driver.current_url
            title = driver.title
        if (url.find("adfs.brocku.ca")):
            assert title == "Sign In"
            print("bu-signon")
            password_box = driver.find_element(
                By.XPATH, "//input[@type='password'][1]")
            password_box.send_keys(sekrets.PASSWORD)

            submit_button = driver.find_element(
                By.XPATH, "//span[@class='submit'][1]")
            submit_button.click()
            WebDriverWait(driver, timeout=10).until(
                EC.url_changes(url))
            url = driver.current_url
            title = driver.title

        if (url.find("microsoftonline.com")):
            assert title == "Sign in to your account"
            print("ms-code")

            otp_box = WebDriverWait(driver, timeout=10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@name='otc']")))

            # otp_box = driver.find_element(
            #     By.XPATH, "//input[@name='otc']")
            otp_box.send_keys(pyotp.TOTP(sekrets.TOTP_GEN).now())

            submit_button = driver.find_element(
                By.XPATH, "//input[@type='submit'][1]")
            submit_button.click()

            WebDriverWait(driver, timeout=10).until(
                EC.url_changes(url))
            url = driver.current_url
            title = driver.title

        driver.get("https://my.brocku.ca/BrockDB/reg_CourseAvailStudent.aspx")

        dropdown = Select(driver.find_element(
            By.ID, "ctl00_Content_bddlProgram"))
        dropdown.select_by_visible_text("Undergraduate")

        subjectbox = driver.find_element(By.ID, "ctl00_Content_txtName")
        subjectbox.send_keys("COSC")

        gobtn = driver.find_element(By.ID, "ctl00_Content_btnGo")
        gobtn.click()

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # driver.find_element(By.ID, "enter?")

        # assert title == "Web form"

        # text_box = driver.find_element(by=By.NAME, value="my-text")
        # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

        # text_box.send_keys("Selenium")
        # sleep(1)
        # submit_button.click()

        # message = driver.find_element(by=By.ID, value="message")
        # value = message.text
        # assert value == "Received!"

        # sleep(2)

    input()
    driver.quit()


test_eight_components()
