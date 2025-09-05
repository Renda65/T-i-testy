from playwright.sync_api import Page

def test_login(page: Page):
    '''Test přihlášení na stránce KCHT.cz s neplatnými údaji'''
    page.goto("https://www.kcht.cz/prihlaseni")
    print("✔  Stranka https://www.kcht.cz/prihlaseni se načetla .")

    page.fill("#formLogin","Karel Podlaha")
    print("✔  Do pole pro jméno bylo zapsáno 'Karel Podlaha'.")

    page.fill("#formPassword","Mojeheslo")
    print("✔  Do pole pro heslo bylo zapsáno 'Mojeheslo'.")

    #kliknutí na tlačítko pro přihlášení
    page.click("form button")

    # po neuspěšném přihlášení jsou na stránce vidět chybová hlášení.
    page.wait_for_url("https://www.kcht.cz/prihlaseni")
    assert page.url == "https://www.kcht.cz/prihlaseni"

    print("✔  Test byl úspěšně dokončen a chybová hlášení na stránce jsou vidět.")

# pro zobrazení výstupu v terminálu zadáme pytest -s test_prihlaseni.py