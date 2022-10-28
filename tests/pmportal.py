from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    # page.goto("https://confluence.arcurve.com/login.action?os_destination=%2Fpages%2Fviewpage.action%3FspaceKey%3DPMP%26title%3D1.%2BOverview&permissionViolation=true")
    #
    # page.get_by_role("link", name="Login with Azure AD").click()
    # page.wait_for_url("https://login.microsoftonline.com/d43c9f02-70b9-44ce-adfc-e244b5a619ac/saml2?sso_reload=true")
    #
    # page.get_by_placeholder("someone@example.com").click()
    #
    # page.get_by_placeholder("someone@example.com").fill("roshan.nair@arcurve.com")
    #
    # page.get_by_placeholder("someone@example.com").press("Enter")
    # page.wait_for_url("https://login.microsoftonline.com/d43c9f02-70b9-44ce-adfc-e244b5a619ac/saml2?sso_reload=true")
    #
    # page.get_by_placeholder("Password").click()
    #
    # page.get_by_placeholder("Password").click()
    #
    # page.get_by_placeholder("Password").fill("Pwcwelcome@125")
    #
    # page.get_by_role("button", name="Sign in").click()
    # page.wait_for_url("https://login.microsoftonline.com/d43c9f02-70b9-44ce-adfc-e244b5a619ac/login")
    #
    # page.get_by_placeholder("Password").click()
    #
    # page.get_by_placeholder("Password").fill("Pwcwelcome@126")
    #
    # page.get_by_placeholder("Password").press("Enter")
    # page.wait_for_url("https://login.microsoftonline.com/d43c9f02-70b9-44ce-adfc-e244b5a619ac/login")
    #
    # page.get_by_placeholder("Code").click()
    #
    # page.get_by_placeholder("Code").fill("183679")
    #
    # page.get_by_role("button", name="Verify").click()
    page.goto("https://confluence.arcurve.com/pages/viewpage.action?spaceKey=PMP&title=1.+Overview")

    page.get_by_role("link", name="https://app-pmp-test-canadacentral.azurewebsites.net/").click()
    page.wait_for_url("https://app-pmp-test-canadacentral.azurewebsites.net/")

    page.get_by_role("link", name="Log in").click()
    page.wait_for_url("https://app-pmp-test-canadacentral.azurewebsites.net/projects")wcwe

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
