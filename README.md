# Uitleg van het Python Project

Dit project is ontwikkeld als onderdeel van mijn opleiding en omvat enkele testcases voor het formatteren van namen met Python. Hier is een korte uitleg van de verschillende onderdelen en hoe ze functioneren.

## Bestanden in het project

1. **name_function.py**
    - Bevat de `formatteer_naam` functie die een volledige naam netjes formatteert met een optioneel tussenvoegsel.

2. **test_name_function.py**
    - Bevat testcases om te controleren of de `formatteer_naam` functie correct functioneert. Hier zijn twee belangrijke tests:
        - `test_voornaam_achternaam()`: Test of voor- en achternamen worden geformatteerd zoals "Piet Dijk".
        - `test_voornaam_tussenvoegsel_achternaam()`: Test of voor- en achternamen met tussenvoegsel worden geformatteerd zoals "Piet van Dijk".

3. **names.py**
    - Een interactief script waarmee gebruikers namen kunnen invoeren (voornaam, achternaam en optioneel tussenvoegsel). Deze input wordt vervolgens gebruikt om een geformatteerde naam weer te geven.

4. **requirements.txt**
    - Bevat alle benodigde Python-pakketten die met `pip` geïnstalleerd kunnen worden om het project werkend te krijgen.

## Gebruik en uitvoeren

Om het project te gebruiken, volg deze stappen:

# Clone de repository
git clone <repository_url>

# Ga naar de projectdirectory
cd <project_directory>

# Installeer de vereiste pakketten
pip install -r requirements.txt

# Voer de interactieve naamformatteerder uit
python names.py


Als je de testcases wilt uitvoeren, gebruik dan het volgende commando:
pytest

Je hoeft de bestandsnaam niet apart te vermelden, omdat pytest automatisch zoekt naar bestanden die beginnen met test_ of eindigen op _test.py. Pytest detecteert en voert alle testfuncties in deze bestanden uit.