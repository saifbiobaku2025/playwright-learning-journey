from playwright.sync_api import Page, expect
import pytest
from pages.login_page import Login_page
from utils.data_loder import data_loader

USERS = data_loader("data/users.json")
print(USERS)

# def test_home_page_title(page: Page):
#     login_page = Login_page(page)
#     login_page.navigate_to_login_page()
#     assert page.title() == "Swag Labs"

@pytest.mark.parametrize("case", USERS)
def test_login_with_valid_credentials(page: Page, case: dict):
    login_page = Login_page(page)
    login_page.navigate_to_login_page()
    login_page.login(case["username"], case["password"])
    expect(page.get_by_role("button", name="Open Menu")).to_be_visible()

# def test_invalid_username(page: Page):
#     login_page = Login_page(page)
#     login_page.navigate_to_login_page() 
#     login_page.login("invalid_user", "secret_sauce")
#     expect(page.locator("h3[data-test='error']")).to_have_text("Epic sadface: Username and password do not match any user in this service") 

# def test_invalid_password(page: Page):
#     page.goto("https://saucedemo.com/")
#     page.locator("input[id='user-name']").fill("standard_user")
#     page.locator("input[id='password']").fill("invalid_password")
#     page.locator("input[id='login-button']").click()
#     expect(page.locator("h3[data-test='error']")).to_have_text("Epic sadface: Username and password do not match any user in this service")    
         
# def test_blank_username(page: Page):
#     login_page = Login_page(page)
#     login_page.navigate_to_login_page()
#     login_page.login("", "secret_sauce")
#     expect(page.locator("h3[data-test='error']")).to_have_text("Epic sadface: Username is required")

# def test_blank_password(page: Page):
#     login_page = Login_page(page)
#     login_page.navigate_to_login_page()
#     login_page.login("standard_user", "")
#     expect(page.locator("h3[data-test='error']")).to_have_text("Epic sadface: Password is required")

