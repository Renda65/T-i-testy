from playwright.sync_api import Page, sync_playwright

def test_rzp_2(page: Page):
    '''Test vyhledání subjektu podle názvu na stránce RZP.gov.cz'''
    # prejdeme na stranku www.rzp.gov.cz
    page.goto("https://rzp.gov.cz/verejne-udaje/cs/udaje/vyber-subjektu")


    #vyhledáme místo pro zadání Název subjektu
    # vyhledáme input s id="Name" a vypíšeme jeho HTML
    input_elem = page.query_selector("#nazev")
    if input_elem:
        print("✔  Nalezen input s id=nazev:", input_elem.get_attribute('outerHTML')) 
        
        # Vložíme do inputu hodnotu "Novakova"
        page.fill("#nazev", "Novakova")
        
        # Ověření, že hodnota byla správně vložena
        assert page.input_value("#nazev") == "Novakova"
        print("✔  Hodnota 'Novakova' byla úspěšně vložena do inputu s id=nazev.")
        
        # Potvrzení inputu klávesou Enter
        page.press("#nazev", "Enter")

        print("✔  Stisknuta klávesa Enter v inputu s id=nazev.Je vidět nová adresa URL.")
        print("✔  Test byl úspěšně dokončen.")
    else:
        print("  Input s id=nazev nebyl nalezen.")

    # pro zobrazení výstupu v terminálu zadáme pytest -s test_druhy.py