from playwright.sync_api import Page, sync_playwright
import pytest

@pytest.fixture
def page():
    """
    Fixture pro vytvoření nové stránky v prohlížeči Chromium pomocí Playwrightu.
    Spouští prohlížeč v režimu headless=False (viditelný) a zpomaluje akce pro lepší sledování (slow_mo=3000).
    Vrací objekt stránky pro použití v testech.
    """
    with sync_playwright() as pw:
        # chromium(Chrome, Edge), webkit(Safari), firefox
        browser = pw.chromium.launch(headless=False, slow_mo=3000) # 3 sekundy
        page = browser.new_page()
        yield page