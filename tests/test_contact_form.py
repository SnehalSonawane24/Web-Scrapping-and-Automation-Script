from playwright.sync_api import sync_playwright

# Test Data
USERNAME = "Admin45"
PASSWORD = "admin123"

# URL
URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


def test_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(URL)

        page.locator("//input[@placeholder='Username']").fill(USERNAME)
        page.locator("//input[@placeholder='Password']").fill(PASSWORD)
        page.locator("//button[normalize-space()='Login']").click()

        page.wait_for_timeout(3000)

        if "dashboard" in page.url.lower():
            print("PASS : Login successful")
        else:
            page.screenshot(path="screenshots/failure.png", full_page=True)
            print("FAIL : Login failed")

        browser.close()


if __name__ == "__main__":
    test_login()