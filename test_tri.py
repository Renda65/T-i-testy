from playwright.sync_api import Page, sync_playwright

def test_rzp_3(page: Page):
    '''Test vyhledání subjektu podle kódu živnosti na stránce RZP.gov.cz'''
    # prejdeme na stranku www.rzp.gov.cz
    page.goto("https://rzp.gov.cz/verejne-udaje/cs/")
    print("✔ Stranka https://rzp.gov.cz/verejne-udaje/cs/ se načetla .")

    # najedeme myší na VÝBĚR ÚDAJŮ
    page.hover("text=VÝBĚR ÚDAJŮ")
    print("✔ Myš najela na požadovanou pozici")

    # kliknutí na VÝBĚR ÚDAJŮ otevřeme přislušnou stránku 
    page.click("text=VÝBĚR ÚDAJŮ")
    print("✔ Kliknuto na VÝBĚR ÚDAJŮ a otevřena přislušná stránka.")  

    # najedeme myší na ŽIVNOSTI
    page.hover("text=ŽIVNOSTI")
    print("✔ Myš najela na požadovanou pozici")

    # kliknutím na ŽIVNOSTI otevřeme přislušnou stránku,otevře se stránka s URL končící na /zivnosti 
    # a rolovací seznam  živností
    page.click("text=ŽIVNOSTI")
    print("✔ Kliknuto na ŽIVNOSTI a otevřena přislušná stránka.")

    #najdeme myší na input "Název nebo kód živnosti, případně oboru"
    page.hover("#predmet")
    print("✔ Myš najela na požadovanou pozici")

    # do inputu vložíme hodnotu kodu živnosti
    page.fill("#predmet", "Z01008")
    print("✔ Do pole pro kód živnosti bylo zapsáno 'Z01008'.")

    # Najedeme myší na input pro zadání místa živnosti
    page.hover("#misto")
    page.click("#misto")
    print("✔ Myš najela na požadovanou pozici,Kliknutím se otevřel input pro zadání místa živnosti.")

    # zápis do inputu pro zadání místa živnosti (Lipník nad Bečvou) - použijeme přesnější selektor
    page.fill("#main-panel > div > div.content.grid.asides.searches > div:nth-child(3) > form > fieldset > fieldset > div:nth-child(2) > div.form-control-group > component > div > div > input", "Lipník nad Bečvou")
    print("✔ Do pole pro místo živnosti bylo zapsáno 'Lipník nad Bečvou'.")
    assert page.input_value("#main-panel > div > div.content.grid.asides.searches > div:nth-child(3) > form > fieldset > fieldset > div:nth-child(2) > div.form-control-group > component > div > div > input") == "Lipník nad Bečvou"

    # Potvrzení inputu výběru kliknutím myší na nabidnutý výběr
    page.hover("#misto0")
    page.click("#misto0")
    # najedeme myší na tlačitko VYHLEDAT SUBJEKTY
    page.hover("text=VYHLEDAT SUBJEKTY")
    print("✔ Myš najela na požadovanou pozici")

    # po zadání údaju kliknutím na VYHLEDAT SUBJEKTY otevřeme přislušnou stránku s informacemi o subjektech
    page.click("text=VYHLEDAT SUBJEKTY")
    print("✔ Kliknuto na VYHLEDAT SUBJEKTY. ")

    # Ověření, že se zobrazila stránka na kterou vyhledávání odkazuje (změna URL)
    page.wait_for_load_state("networkidle")
    print("Aktuální URL:", page.url)
    assert page.url != "https://rzp.gov.cz/verejne-udaje/cs/udaje/vyber-zivnosti", "URL se nezměnila, stránka nebyla zobrazena."
    print("✔ Stránka po vyhledávání byla zobrazena.")
    print("✔ TEST BYL USPĚŠNĚ UKONČEN.")

    # pro zobrazení výstupu v terminálu zadáme pytest -s test_tri.py


