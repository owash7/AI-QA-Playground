import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()

    # Disable password manager and save prompts
    chrome_options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,  # Block notifications
            "autofill.profile_enabled": False,  # Disable autofill
        }
    )

    # Additional arguments to suppress dialogs
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-features=PasswordManager")
    chrome_options.add_argument("--start-maximized")

    # Use incognito mode (optional but helpful)
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()