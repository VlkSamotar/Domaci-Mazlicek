import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

import play

play.set_backdrop('lightgrey')

spokojenost = 50

background = play.new_box(color='black', x=0, y=100, width=200, height=200)

img1 = play.new_image(image='assets/1.jpg', x=0, y=100, size=20)
img2 = play.new_image(image='assets/2.jpg', x=0, y=100, size=20)
img3 = play.new_image(image='assets/3.jpg', x=0, y=100, size=20)

ukazatel = play.new_text(words=f'Spokojenost: {spokojenost}', x=0, y=230, font_size=30, color='black')

def aktualizuj_vyraz():
    global spokojenost

    if spokojenost > 100:
        spokojenost = 100
    elif spokojenost < 0:
        spokojenost = 0

    ukazatel.words = f'Spokojenost {spokojenost}'

    if spokojenost < 35:
        img1.show()
        img2.hide()
        img3.hide()
    elif spokojenost <= 70:
        img1.hide()
        img2.show()
        img3.hide()
    else:
        img1.hide()
        img2.hide()
        img3.show()

aktualizuj_vyraz()

tlacitko1 = play.new_text(words='Krmit (+15)', x=-140, y=-150, font_size=30, color='green')
tlacitko2 = play.new_text(words='Hrát (+25)', x=0, y=-150, font_size=30, color='blue')
tlacitko3 = play.new_text(words='Zlobit (-30)', x=140, y=-150, font_size=30, color='red')

@tlacitko1.when_clicked
def krmit():
    global spokojenost
    spokojenost += 15
    aktualizuj_vyraz()

@tlacitko2.when_clicked
def hrat():
    global spokojenost
    spokojenost += 25
    aktualizuj_vyraz()

@tlacitko3.when_clicked
def zlobit():
    global spokojenost
    spokojenost -= 30
    aktualizuj_vyraz()

play.start_program()