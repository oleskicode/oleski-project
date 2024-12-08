from playwright.sync_api import Playwright, sync_playwright, expect


def test_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Login
    page.goto("https://freevpnplanet.com/")
    page.get_by_role("link", name="login").click()
    page.get_by_label("Enter email").fill(
        "example@example.com"
    )  # TODO remove explicit email from code
    page.get_by_label("Enter password").fill(
        "explicit-password"
    )  # TODO remove explicit password from code
    page.get_by_role("button", name="Login").click()
    # Check User Profile cabinet
    expect(page.locator("#qa-title-exit").get_by_text("Logout")).to_be_visible()
    expect(page.locator('[id="__layout"]')).to_contain_text("Account status: Active")
    expect(page.locator('[id="__layout"]')).to_contain_text("Subscription Information")
    # Logout
    page.get_by_role("img", name="Profile").click()
    page.get_by_text("Logout").first.click()
    expect(page.locator("#c-sidebar_header")).to_contain_text("login")
    expect(page.get_by_role("link", name="login")).to_be_visible()
    # Teardown
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_login(playwright)
