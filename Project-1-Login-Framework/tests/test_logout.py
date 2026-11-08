from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage

def test_logout(page: Page):
    inventory_page = InventoryPage(page)
    inventory_page.login("standard_user", "secret_sauce")
    inventory_page.logout()
    assert inventory_page.is_logged_out()
    
