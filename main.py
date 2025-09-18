TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

UZIVATELE = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

delky_slov = {}

parametry = {
    "velka_na_zacatku": 0,
    "cela_velka": 0,
    "cela_mala": 0,
    "pocet_cisel": 0,
    "soucet_cisel": 0
}

print("-" * 60)
user = input("Zadej uživatelské jméno:")
password = input("Zadej uživatelské heslo:")
print("-" * 60)
if user in UZIVATELE and UZIVATELE[user] == password:
    print(f"Vítej v analyzátoru textů, {user}.")

    cislo_textu = input(f"Zadej číslo textu, který chceš analyzovat (mezi 1 a {len(TEXTS)}):")
    print("-" * 60)
    if cislo_textu.isdigit() and 1 <= int(cislo_textu) <= len(TEXTS):
        slova = TEXTS[int(cislo_textu) - 1].split()
        
        for slovo in slova:
            slovo = slovo.strip(",.?!:;")    
            
            if slovo.istitle():
                parametry["velka_na_zacatku"] += 1
            if slovo.isupper():
                parametry["cela_velka"] += 1
            if slovo.islower():
                parametry["cela_mala"] += 1
            if slovo.isdigit():
                parametry["pocet_cisel"] += 1
                parametry["soucet_cisel"] += int(slovo)

            l = len(slovo)
            if l in delky_slov:
                delky_slov[l] += 1
            else:
                delky_slov[l] = 1

        print(f"Počet slov v textu je: {len(slova)}")

        for k, v in parametry.items():
            if k is "soucet_cisel":
                print(f"Součet všech šísel je {parametry[k]}.")
            else:    
                print(f"V textu je {v} slov, splňující podmínku: {k}")
        print("-" * 60)
        print(f"Délka | Výskyt | Počet")
        print("-" * 60) 
        for delka in sorted(delky_slov):
            print(f"{delka:>2} |" + "*" * delky_slov[delka] + " " * (20 - delky_slov[delka]) + f"|{delky_slov[delka]}")


    else:
        print("Špatné číslo textu. Končím program!")
else:
    print("Špatné přihlašovací údaje. Končím program!")


"""
for idx, item in enumerate(TEXTS, start=1):
    print(f"{idx}. text je:\n{item}")

"""