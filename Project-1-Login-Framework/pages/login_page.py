from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("input[id='user-name']")
        self.password_input = page.locator("input[id='password']")
        self.login_button = page.locator("input[id='login-button']")
        self.error_message = page.locator("h3[data-test='error']")
        self.menu_button = page.get_by_role("button", name="Open Menu")

    def navigate_to_login_page(self):
        self.page.goto(self.URL, wait_until=self.LOAD_STATE)    
        self.wait_visible("input[id='user-name']")

    def is_login_page_visible(self) -> bool:
        return self.username_input.is_visible() 

    def login(self, username : str, password : str):
        self.expect_visible("input[id='user-name']")
        self.username_input.fill(username)
        self.expect_visible("input[id='password']")
        self.password_input.fill(password)
        self.expect_visible("input[id='login-button']")
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.text_content()