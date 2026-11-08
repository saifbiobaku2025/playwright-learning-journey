from playwright.sync_api import Page, expect, Locator

class BasePage:
    DEFAULT_TIMEOUT = 5000  # Default timeout in milliseconds
    LOAD_STATE = "domcontentloaded"  # Default load state for page navigation

    def __init__(self, page: Page):
        self.page = page

    def wait_visible(self, selector: str) -> None:
        """Wait for an element to be visible on the page."""
        self.page.wait_for_selector(selector, state="visible", timeout=self.DEFAULT_TIMEOUT)

    def wait_url(self, url: str) -> None:
        """Wait for the page to navigate to a specific URL."""
        self.page.wait_for_url(url, timeout=self.DEFAULT_TIMEOUT)

    def expect_visible(self, selector: str) -> None:
        """Expect an element to be visible on the page."""
        expect(self.page.locator(selector)).to_be_visible(timeout=self.DEFAULT_TIMEOUT)

    def expect_visible_now(self, locator: Locator):
        expect(locator).to_be_visible(
            timeout=self.DEFAULT_TIMEOUT
        )

    def click(self, locator: Locator):
        self.expect_visible(locator)
        locator.click()

    def fill(self, locator: Locator, value: str):
        self.expect_visible(locator)
        locator.fill(value)