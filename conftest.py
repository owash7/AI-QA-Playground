import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime
from test_metrics.metrics import TestMetrics


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


metrics = TestMetrics()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # ---- Metrics tracking ----
        if report.passed:
            metrics.record_result("passed")
        elif report.failed:
            metrics.record_result("failed")
        elif report.skipped:
            metrics.record_result("skipped")

        # ---- Screenshot on failure ----
        if report.failed:
            driver = item.funcargs.get("driver")
            if driver:
                os.makedirs("screenshots", exist_ok=True)
                file_name = (
                    f"screenshots/"
                    f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                )
                driver.save_screenshot(file_name)


def pytest_sessionfinish(session, exitstatus):
    metrics.save_to_google_sheets()