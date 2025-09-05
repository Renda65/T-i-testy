# Automatizované testy pro www.rzp.gov.cz a www.kcht.cz

Tento projekt obsahuje ukázkové automatizované testy webů www.rzp.gov.cz a www.kcht.cz pomocí Pythonu a knihovny Playwright. 
Testy jsou vytvořené jako zkušební projekt v rámci akademie Engeto. Nad rámec zadání je přidán ještě jeden test.

## Struktura složek a souborů

- `conftest.py` – konfigurační soubor pro pytest
- `test_prvni.py` – testuje funkčnost hlavních tlačítek na stránce RZP.gov.cz
- `test_druhy.py` – testuje vyhledání subjektu podle názvu na stránce RZP.gov.cz
- `test_tri.py` – testuje vyhledání subjektu podle kódu živnosti a místa na stránce RZP.gov.cz
- `test_prihlaseni.py` – testuje přihlášení na stránce KCHT.cz s neplatnými údaji
- `zadání a popis projektu.txt` – zadání a popis projektu
- `README.md` – tento popis projektu.
- [Testovací plán](testovaci_plan.txt) – obsahuje cíle, scénáře a kritéria úspěšnosti testování
- [Test report](test_report.txt) – shrnutí výsledků posledního běhu testů

## Popis jednotlivých testů

### test_prvni.py
Ověřuje, že na hlavní stránce RZP.gov.cz jsou viditelná a funkční tlačítka „Vyhledání podnikatele“, „Adresář úřadů“ a „Žádost o výpis“. Test kliká na zadaná tlačítka a ověřuje, že dojde ke změně URL.

### test_druhy.py
Testuje vyhledání subjektu podle názvu. Do pole s id `nazev` zadá hodnotu „Novakova“, ověří její vložení a potvrdí Enterem. Test kontroluje, že input existuje a je editovatelný.

### test_tri.py
Testuje vyhledání subjektu podle kódu živnosti a místa. Vyplní pole pro kód živnosti a místo, potvrdí výběr, klikne na „VYHLEDAT SUBJEKTY“ a ověří, že se zobrazí stránka s výsledky (změna URL).Dále test ve svém průběhu prověří nábídku seznamu živností ve rolovacím seznamu. Také prověří při zadání obce, zda program navrhne uživateli po zadání obce úplný název obce a příslušný okres.

### test_prihlaseni.py
Testuje přihlášení na stránce KCHT.cz s neplatnými údaji. Vyplní pole pro jméno a heslo, klikne na tlačítko pro přihlášení a ověří, že zůstane na stránce s přihlášením (chybová hlášení).


## Požadavky

- Python 3.8+
- Playwright

## Spuštění testů

Spusťte libovolný test pomocí příkazu:

```bash
pytest -s test_prvni.py
```

nebo

```bash
pytest -s test_druhy.py
```

nebo

```bash
pytest -s test_tri.py
```

nebo

```bash
pytest -s test_prihlaseni.py
```

## Automatické generování HTML reportu

Pro přehledný report výsledků testů můžete použít plugin [pytest-html](https://github.com/pytest-dev/pytest-html):

1. Nainstalujte plugin:

   ```bash
   pip install pytest-html
   ```

2. Spusťte testy s generováním reportu:

   ```bash
   pytest --html=report.html
   ```

3. Výsledný soubor `report.html` bude obsahovat přehledný report všech testů.

## Poznámky

- Pro správné fungování testů je potřeba stabilní internetové připojení.
- Pokud testy selžou na vyhledání textu, zkontrolujte aktuální HTML stránky a případně upravte selektory.
- Pro zátěžové testování použijte specializované nástroje (Locust, k6, JMeter).

## Autor

Renato Vítek (2025)

