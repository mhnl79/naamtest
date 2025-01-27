from name_function import get_formatted_name

def test_voornaam_achternaam():
    """Werken namen zoals Piet Dijk"""
    geformatteerde_naam = get_formatted_name('piet', 'dijk')
    assert geformatteerde_naam == 'Piet Dijk'

def test_voornaam_tussenvoegsel_achternaam():
    """Werken namen zoals Piet van Dijk?"""
    geformatteerde_naam = get_formatted_name('piet', 'dijk', 'van')
    assert geformatteerde_naam == 'Piet Van Dijk'
