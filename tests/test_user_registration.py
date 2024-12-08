import re
from playwright.sync_api import Playwright, sync_playwright, expect

# provide new user email below


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://freevpnplanet.com/")
    page.get_by_role("link", name="login").click()
    page.get_by_role("link", name="Sign Up").click()
    page.get_by_role("button", name="Create").click()
    page.get_by_label("Enter email").click()
    page.get_by_label("Enter email").fill(
        "new-user@example.com"  # provide new user email
    )
    page.get_by_role("button", name="Create").click()
    # Create Account Page Checks
    expect(page.get_by_role("main")).to_contain_text("Create your account")
    expect(page.locator("#qa-submit-button-create")).to_match_aria_snapshot(
        "- text: Create"
    )
    expect(page.get_by_role("button", name="Create")).to_be_visible()
    page.get_by_role("button", name="Create").click()
    expect(page.get_by_role("main")).to_contain_text(
        "Your account password has been sent to your email. Be sure to verify your account by clicking on the link in the email"
    )
    page.get_by_text("If you haven't received the").click()
    expect(page.get_by_role("main")).to_contain_text(
        "If you haven't received the email, please check the Spam folder."
    )
    expect(page.get_by_role("link", name="Next")).to_be_visible()
    page.get_by_role("link", name="Next").click()
    page.goto("https://account.freevpnplanet.com/download/")
    expect(page.locator("#qa-submit-button-next")).to_contain_text("Next")
    page.get_by_role("link", name="Profile").click()
    expect(page.locator("#qa-user-account-status")).to_contain_text("Inactive")
    expect(page.locator("#qa-user-account-status")).to_match_aria_snapshot(
        '- img "not active"\n- text: Inactive'
    )
    expect(page.get_by_role("button", name="Verify account")).to_be_visible()
    expect(page.locator("#qa-send-mail")).to_contain_text("Verify account")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
