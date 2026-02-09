from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://the-internet.herokuapp.com/login"


def login(driver, username, password):
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


def get_flash_message(driver):
    return driver.find_element(By.ID, "flash").text


def test_valid_login(driver):
    driver.get(BASE_URL)

    login(driver, "tomsmith", "SuperSecretPassword!")

    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    assert "You logged into a secure area!" in message


def test_invalid_login(driver):
    driver.get(BASE_URL)

    login(driver, "invalid", "invalid")

    message = get_flash_message(driver)
    assert "Your username is invalid!" in message


def test_empty_credentials(driver):
    driver.get(BASE_URL)

    login(driver, "", "")

    message = get_flash_message(driver)
    assert "Your username is invalid!" in message


def test_logout(driver):
    driver.get(BASE_URL)

    login(driver, "tomsmith", "SuperSecretPassword!")

    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.secondary.radius"))
    )
    logout_button.click()

    # Wait until we are back on the login page
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )

    message = get_flash_message(driver)
    assert "You logged out of the secure area!" in message

