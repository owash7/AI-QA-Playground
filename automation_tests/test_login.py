from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


BASE_URL = "https://the-internet.herokuapp.com/login"


def login(driver, username, password):
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

def dismiss_password_alert(driver):
    """Helper function to dismiss Google Password Manager alert if present"""
    try:
        # Wait for OK button and click it if present
        ok_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
        )
        ok_button.click()
        print("Password alert dismissed")
    except TimeoutException:
        # No alert present, continue
        pass


def get_flash_message(driver):
    return driver.find_element(By.ID, "flash").text

# Functional Test Cases

def test_valid_login(driver):
    driver.get(BASE_URL)

    login(driver, "tomsmith", "SuperSecretPassword!")

    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    assert "You logged into a secure area!" in message


def test_invalid_pw(driver):
    driver.get(BASE_URL)

    login(driver, "tomsmith", "invalid")

    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    assert "Your password is invalid!" in message


def test_invalid_username(driver):
    driver.get(BASE_URL)

    login(driver, "invalid", "SuperSecretPassword!")

    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    assert "Your username is invalid!" in message


def test_invalid_login(driver):
    driver.get(BASE_URL)

    login(driver, "invalid", "invalid")

    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    assert "Your username is invalid!" in message


def test_logout(driver):
    driver.get(BASE_URL)

    login(driver, "tomsmith", "SuperSecretPassword!")

    dismiss_password_alert(driver)

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

# Edge cases

def test_empty_username(driver):
    driver.get(BASE_URL)

    login(driver, "", "SuperSecretPassword!")

    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    assert "Your username is invalid!" in message


def test_empty_pw(driver):
    driver.get(BASE_URL)

    login(driver, "tomsmith", "")

    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    assert "Your password is invalid!" in message


def test_empty_creds(driver):
    driver.get(BASE_URL)

    login(driver, "", "")

    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    assert "Your username is invalid!" in message


def test_extra_space(driver):
    driver.get(BASE_URL)

    login(driver, " tomsmith ", " SuperSecretPassword! ")

    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    assert "Your username is invalid!" in message


def test_logout_refresh(driver):
    driver.get(BASE_URL)

    login(driver, "tomsmith", "SuperSecretPassword!")

    # Dismiss password alert if it appears
    dismiss_password_alert(driver)

    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.secondary.radius"))
    )
    logout_button.click()

    # Wait until we are back on the login page
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )
    driver.refresh()

    login_page = driver.find_element(By.XPATH, "//h2[text()='Login Page']")
    assert "Login Page" in login_page.text