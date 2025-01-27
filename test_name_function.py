from name_function import formatteer_naam

def test_voornaam_achternaam():
    """Werken namen zoals Piet Dijk"""
    geformatteerde_naam = formatteer_naam('piet', 'dijk')
    assert geformatteerde_naam == 'Piet Dijk'

def test_voornaam_tussenvoegsel_achternaam():
    """Werken namen zoals Piet van Dijk?"""
    geformatteerde_naam = formatteer_naam('piet', 'dijk', 'van')
    assert geformatteerde_naam == 'Piet Van Dijk'
