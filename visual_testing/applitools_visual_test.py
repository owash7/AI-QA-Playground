from applitools.selenium import Eyes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://the-internet.herokuapp.com/login"


def test_visual_login_page(driver):
    eyes = Eyes()
    eyes.open(
        driver=driver,
        app_name="AI QA Playground",
        test_name="Visual Test - Login Page"
    )

    driver.get(BASE_URL)

    # Visual checkpoint
    eyes.check_window("Login Page")

    eyes.close()


def test_visual_secure_area_after_login(driver):
    eyes = Eyes()
    eyes.open(
        driver=driver,
        app_name="AI QA Playground",
        test_name="Visual Test - Secure Area"
    )

    driver.get(BASE_URL)

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    # Visual checkpoint
    eyes.check_window("Secure Area")

    eyes.close()
