import pytest

from pokemon import Pokemon


def test_pokemon_init():
    """Checks basic initialization of the Pokemon class"""
    pok = Pokemon("Pikachu", 123)
    assert pok.name == "Pikachu"
    assert pok.health == 123
    assert pok.level == 1


def test_invalid_pokemon_init():
    """Checks if the Pokemon class raises ValueError for invalid inputs"""
    with pytest.raises(ValueError):
        pok = Pokemon(123, 123)
    with pytest.raises(ValueError):
        pok = Pokemon("Pikachu", "123")
    with pytest.raises(ValueError):
        pok = Pokemon("Pikachu", -123)
    with pytest.raises(ValueError):
        pok = Pokemon("Pikachu", 0)

    # The following tests only make sure that your constructor
    # ONLY takes 2 positional arguments.
    with pytest.raises(TypeError):
        pok = Pokemon("Pikachu", 123, 2)
    with pytest.raises(TypeError):
        pok = Pokemon("Pikachu", 123, level=2)


def test_pokemon_level_up():
    """Checks if the level of the Pokemon increases by 1 when calling level_up"""
    pok = Pokemon("Pikachu", 123)
    pok.level_up()
    assert pok.level == 2
    pok.level_up()
    assert pok.level == 3
