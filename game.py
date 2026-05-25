# =====================================================================
# PROJECT: Terminal Dungeon Crawler
# AUTHOR: Marcel
# =====================================================================
ekwipunek = {}
def pokaz_status(hp, ekwipunek):
    """
    ZADANIE 1: PANEL GRACZA
    Funkcja ma ładnie wypisać w konsoli aktualne HP gracza
    szuflada po szufladzie (pętla for po słowniku ekwipunku).
    """
    print(f"\n=== TWOJE HP: {hp} ===")
    print("Twój ekwipunek:")

    for item, ilosc in ekwipunek:
        if item == ekwipunek:
            print(f"-{item}: {ilosc} szt")
    print("=======================")


def walka_z_gobliniem(ekwipunek):

    if "Miecz" in ekwipunek:
        print("Pokonałeś goblina i zdobyłeś 50 złota!")
        ekwipunek["Złoto"] += 50
        return True(wygrana)
    else:
        if "Miecz" not in ekwipunek:
            print("Goblin ciebie zranił")
            return False(przegrana)
    
    pass


def gra():
    hp = 100
    ekwipunek = {"Mikstura": 2, "Złoto": 10}
    
    print("Budzisz się w ciemnej celi. Drzwi są uchylone.")
    print("Na stole widzisz leżący 'Miecz'. Chcesz go podnieść?")
    wybor1 = input("(tak / nie): ").lower()
    
    if wybor1 == "tak":
        print("Podniosłeś Miecz!")
        ekwipunek["Miecz"] = 1
    if wybor1 == "nie":
        print("Nie podniosłeś miecza")
    pokaz_status(hp, ekwipunek)
    
    print("\nWychodzisz na korytarz i nagle atakuje Cię Goblin!")
    wygrana = walka_z_gobliniem(ekwipunek)
    
    if wygrana:
        print("Możesz iść dalej, drzwi do wyjścia stoją otworem. Wygrałeś!")
    else:
        hp -= 40
        print("Uciekłeś, ale goblin mocno Cię poturbował.")
        
    # Pokazujemy końcowy status
    pokaz_status(hp, ekwipunek)


# Uruchomienie gry
if __name__ == "__main__":
    gra()