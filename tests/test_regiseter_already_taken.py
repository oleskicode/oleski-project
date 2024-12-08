import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test_username_already_taken(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://freevpnplanet.com/")
    page.get_by_role("link", name="login").click()
    page.get_by_role("link", name="Sign Up").click()
    page.get_by_label("Enter email").click()
    expect(page.get_by_role("main")).to_contain_text("Your email address will be used as your username")
    expect(page.get_by_role("main")).to_contain_text("Create your account")
    page.get_by_label("Enter email").click()
    page.get_by_label("Enter email").fill("example@example.com") #TODO remove explicit email from code
    page.get_by_role("button", name="Create").click()
    expect(page.locator("#qa-error-text")).to_contain_text("The email has already been taken")
    expect(page.locator("#qa-error-text")).to_match_aria_snapshot("- text: The email has already been taken")
    # Teardown
    context.close()
    browser.close()

with sync_playwright() as playwright:
    test_username_already_taken(playwright)
