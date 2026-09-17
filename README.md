# Domácí Mazlíček

Vítejte u projektu **Domácí Mazlíček**! Jedná se o jednoduchou interaktivní hru v Pythonu, kde se staráte o svého virtuálního mazlíčka. Vaším cílem je udržovat ho co nejvíce spokojeného.

## Funkce hry

Mazlíček má svůj ukazatel **Spokojenosti**, který začíná na hodnotě 50 (maximum je 100, minimum 0). Podle úrovně spokojenosti mění svůj výraz (obrázky `1.png`, `2.png`, `3.png`).

S mazlíčkem můžete interagovat pomocí tří tlačítek:
*   🟢 **Krmit (+15)**: Přidá mazlíčkovi 15 bodů spokojenosti.
*   🔵 **Hrát (+25)**: Přidá mazlíčkovi 25 bodů spokojenosti.
*   🔴 **Zlobit (-30)**: Ubere mazlíčkovi 30 bodů spokojenosti.

## Jak hru spustit

Hra využívá knihovnu `play`. Pro její spuštění postupujte podle těchto kroků:

1.  Ujistěte se, že máte nainstalovaný Python.
2.  Nainstalujte potřebnou knihovnu (pokud ji ještě nemáte):
    ```bash
    pip install replit-play
    ```
3.  Spusťte hru:
    ```bash
    python main.py
    ```

Příjemnou zábavu s vaším virtuálním mazlíčkem!