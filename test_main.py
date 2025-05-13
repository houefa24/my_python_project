import pytest
import time
from main import hello


def test_hello():
    assert hello() == "Hello, GitHub Actions !"


def test_hello_custom_name():
    assert hello("EPSI") == "Hello, EPSI !"


# Scénario 1 : Vérification du type de données
def test_hello_type_error():
    with pytest.raises(TypeError):
        hello(123)


# Scénario 2 : Mesure de performance basique
def test_hello_performance():
    start = time.time()
    for _ in range(1000):
        hello("EPSI")
    duration = time.time() - start
    assert duration < 1


""" # Scénario 3 : Gestion d'erreur (en cas d'erreur volontaire)
def test_hello_error():
     with pytest.raises(ValueError):
         hello("Test") """


# Scénario 4 : Test avec plusieurs paramètres
def test_hello_full_name():
    assert hello("Jane", "Smith") == "Hello, Jane Smith !"