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

## Tipy na vylepšení hry

Pokud byste chtěli hru dále rozvíjet, zde jsou 4 nápady na vylepšení:

1. **Časové ubývání spokojenosti (Tamagotchi styl):** Přidat funkci, která bude spokojenost automaticky snižovat v průběhu času, čímž vznikne skutečná výzva starat se o mazlíčka pravidelně.
2. **Více různých statistik (Hlad, Energie, Zábava):** Místo jedné celkové proměnné sledovat více potřeb. Různá tlačítka pak budou tyto potřeby ovlivňovat rozdílně (např. spánek doplní energii, ale mazlíčkovi během něj vyhládne).
3. **Animace a zvukové efekty:** Oživit hru o zvuky (např. radostné mňouknutí/štěknutí při krmení) a jednoduché animace pohybu nebo změny velikosti, když s mazlíčkem interagujete.
4. **Bodování a herní prohra (Game Over):** Hra by se mohla ukončit ve chvíli, kdy spokojenost klesne na 0. Zároveň byste mohli sbírat body nebo mince za každou sekundu, kdy je mazlíček šťastný, a za ně nakupovat nová vylepšení.