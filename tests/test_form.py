from playwright.sync_api import Playwright, sync_playwright
from pom.POM import ContactPage
import pytest


@pytest.mark.regression
def test_form(set_up) -> None:
    page = set_up


# The below lines are only needed if pytest is not installed, otherwise pytest will run the test automatically even if the below lines are not written
# with sync_playwright() as playwright:
#     test_form(playwright)


