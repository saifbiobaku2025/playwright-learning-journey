from playwright.sync_api import Page, expect
import pytest
from pages.login_page import LoginPage
from utils.data_loder import data_loader

USERS = data_loader("data/users.json")
print(USERS)

def test_home_page_title(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()
    assert page.title() == "Swag Labs"

@pytest.mark.parametrize("case", USERS)
def test_login_with_valid_credentials(page: Page, case: dict):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()
    login_page.login(case["username"], case["password"])
    expect(page).to_have_url(
    "https://www.saucedemo.com/inventory.html"
    ) 
    expect(login_page.menu_button).to_be_visible()

def test_invalid_username(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page() 
    login_page.login("invalid_user", "secret_sauce")
    expect(login_page.error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_invalid_password(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()
    login_page.login("standard_user", "invalid_password")
    expect(login_page.error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")    
         
def test_blank_username(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()
    login_page.login("", "secret_sauce")
    expect(login_page.error_message).to_have_text("Epic sadface: Username is required")

def test_blank_password(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_to_login_page()
    login_page.login("standard_user", "")
    expect(login_page.error_message).to_have_text("Epic sadface: Password is required")

