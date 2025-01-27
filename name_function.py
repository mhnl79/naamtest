def formatteer_naam(voornaam, achternaam, tussenvoegsel=''):
    """Genereer een netjes geformatteerde volledige naam."""
    if tussenvoegsel:
        volledige_naam = f"{voornaam} {tussenvoegsel} {achternaam}"
    else:
        volledige_naam = f"{voornaam} {achternaam}"
    return volledige_naam.title()

