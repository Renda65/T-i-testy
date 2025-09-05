from playwright.sync_api import Page, sync_playwright

def test_rzp(page: Page):
    '''Test ověření tlačítek na stránce RZP.gov.cz'''
    # prejdeme na stranku www.rzp.gov.cz
    page.goto("https://rzp.gov.cz")

    # oveříme, jestli je na stránce text  Vyhledání podnikatele, Adresář úřadů, Žádost o výpis
    for text in ["Vyhledání podnikatele", "Adresář úřadů", "Žádost o výpis"]:
        assert text in page.content()

    # ověříme, jetli je tlačítko s texty funkční,použijeme simulaci kliknutí.
    for text in ["Vyhledání podnikatele", "Adresář úřadů", "Žádost o výpis"]:
        page.goto("https://rzp.gov.cz")
        page.click(f"text={text}")
        assert page.url != "https://rzp.gov.cz"

    print("✔ Test byl úspěšně dokončen a všechny tlačítka s požadovanými texty byly nalezeny i kliknuty.")

    # pro zobrazení výstupu v terminálu zadáme pytest -s test_prvni.py