from playwright.sync_api import Playwright

from pom.POM import ContactPage


def test_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    contact_page = ContactPage(page)
    contact_page.navigate()
    contact_page.submit_form("Roshan", "123 macloead tr", "abc@gmail.com", "123456", "Test", "Test message")
    page.set_default_timeout(3000)