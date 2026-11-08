from playwright.sync_api import Page, expect

def wait_for_spinner_gone(page: Page, spinner_selector: str = ".spinner") -> None:
    """
    Wait for a loading spinner to disappear from the page.

    Args:
        page (Page): The Playwright page object.
        spinner_selector (str): The CSS selector for the spinner element. Default is ".spinner".
    """
    # Wait for the spinner to be hidden or detached from the DOM
expect(page.locator(spinner_selector)).to_be_hidden(timeout=5000)    