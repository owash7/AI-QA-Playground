from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://the-internet.herokuapp.com"


def test_dynamic_loading_hidden_element(driver):
    driver.get(f"{BASE_URL}/dynamic_loading/1")

    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    hello_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    ).text

    assert "Hello World!" in hello_text


def test_dynamic_loading_rendered_element(driver):
    driver.get(f"{BASE_URL}/dynamic_loading/2")

    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    hello_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "finish"))
    ).text

    assert "Hello World!" in hello_text


def test_dynamic_controls_enable_input(driver):
    driver.get(f"{BASE_URL}/dynamic_controls")

    enable_button = driver.find_element(By.XPATH, "//button[text()='Enable']")
    enable_button.click()

    input_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
    )

    input_field.send_keys("QA Automation")
    assert input_field.is_enabled()


def test_dynamic_controls_remove_checkbox(driver):
    driver.get(f"{BASE_URL}/dynamic_controls")

    remove_button = driver.find_element(By.XPATH, "//button[text()='Remove']")
    remove_button.click()

    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "checkbox"))
    )

    assert len(driver.find_elements(By.ID, "checkbox")) == 0
