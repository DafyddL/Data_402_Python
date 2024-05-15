from csv_intro import *


def test_valid_email():
    email1 = "abeeckx0@un.org"
    email2 = "jsmithatmail.com"
    assert valid_email(email1) == True
    assert valid_email(email2) == False
    return


john = Person("Mister", "John", "Smith", "Male", "jsmith@mail.com")
grace = Person("Dame", "Grace", "Jones", "Female", "gjones@mail.com")


def test_get_title():
    assert john.get_title() == "Mister"
    return


def test_get_first_name():
    assert john.get_first_name() == "John"
    return


def test_get_last_name():
    assert john.get_last_name() == "Smith"
    return


def test_get_gender():
    assert john.get_gender() == "Male"
    return


def test_get_email():
    assert john.get_email() == "jsmith@mail.com"
    return


def test_extract_names_and_email():
    actual = extract_names_and_email([john, grace])
    expected = [["John", "Smith", "jsmith@mail.com"],
                ["Grace", "Jones", "gjones@mail.com"]]

    assert actual == expected
