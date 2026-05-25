
hp = 100

print("Idziesz ciemnym korytarzem. Nagle widzisz dziurę w podłodze!")

wybor = input("Chcesz PRZESKOCZYĆ czy WRÓCIĆ? (wpisz: skacz / wracaj): ")


if wybor == "skacz":
    print("Udało się! Skaczesz bezpiecznie na drugą stronę.")
else:
    print("Wycofujesz się. Niestety, potykasz się o kamień!")
    hp = hp - 20  


print(f"Twoje punkty życia: {hp}")