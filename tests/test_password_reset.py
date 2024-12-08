import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_password_reset(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Login Page > Forgot Password
    page.goto("https://freevpnplanet.com/")
    page.get_by_role("link", name="login").click()
    expect(page.locator("#qa-forget-restore")).to_contain_text("Forgot your password?")
    expect(page.locator("#qa-forget-restore")).to_match_aria_snapshot(
        '- link "Forgot your password?"'
    )
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Forgot your password?").click()
    page.get_by_label("Enter email").click()
    page.get_by_label("Enter email").fill(
        "example@example.com"
    )  # TODO remove explicit email from code
    expect(page.locator("#qa-restore-button")).to_contain_text("Restore")
    page.get_by_role("button", name="Restore").click()
    expect(page.get_by_role("main")).to_contain_text(
        "We already sent you an email. Please check your E-mail"
    )
    page.get_by_role("link", name="Next").click()
    # Teardown
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_password_reset(playwright)
