from name_function import formatteer_naam

print("Vul de volgende gegevens in voor elke naam:")
print("Voornaam, achternaam, tussenvoegsel (optioneel)")

while True:
    print("Geef 'q' in om te stoppen.")
    voornaam = input("\nGeef me een voornaam: ").strip().title()
    if voornaam.lower() == 'q':
        break

    achternaam = input("Geef me een achternaam: ").strip().title()
    if achternaam.lower() == 'q':
        break

    tussenvoegsel = input("Wil je een tussenvoegsel toevoegen? Voer het nu in, of druk op Enter om over te slaan: ").strip().title()
    if tussenvoegsel.lower() == 'q':
        break
    
    geformatteerde_naam = formatteer_naam(voornaam, achternaam, tussenvoegsel)
    print(f"\tNetjes geformatteerde naam: {geformatteerde_naam}")


