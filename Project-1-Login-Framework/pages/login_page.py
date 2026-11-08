from pages.base_page import Base_page

class Login_page(Base_page):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("input[id='user-name']")
        self.password_input = page.locator("input[id='password']")
        self.login_button = page.locator("input[id='login-button']")
        self.error_message = page.locator("h3[data-test='error']")
        self.menu_button = page.get_by_role("button", name="Open Menu")

    def navigate_to_login_page(self):
        self.page.goto("https://saucedemo.com/")    
        self.wait_visible("input[id='user-name']")

    def login(self, username, password):
        self.expect_visible("input[id='user-name']")
        self.username_input.fill(username)
        self.expect_visible("input[id='password']")
        self.password_input.fill(password)
        self.expect_visible("input[id='login-button']")
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.text_content()