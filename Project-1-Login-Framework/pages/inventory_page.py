from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.login_page import LoginPage

class InventoryPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.open_menu_button = page.locator("[data-test=\"open-menu\"]")
        self.logout_sidebar_link = page.locator("[data-test=\"logout-sidebar-link\"]")
        
    def login(self, username: str, password: str):
        login_page = LoginPage(self.page)
        login_page.navigate_to_login_page()
        login_page.login(username, password)

    def logout(self):
        self.click(self.open_menu_button)
        self.expect_visible_now(self.logout_sidebar_link)
        self.click(self.logout_sidebar_link)

    def is_logged_out(self) -> bool:
        login_page = LoginPage(self.page)
        return login_page.is_login_page_visible()
     