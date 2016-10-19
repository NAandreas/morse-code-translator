import pytest
from app.morse import to_morse


def test_to_morse():
    assert to_morse('A') == '.-'
    assert to_morse('a') == '.-'


def test_to_morse_sentence():
    assert to_morse('Hej fisk') == '.... . .--- / ..-. .. ... -.-'


def test_to_morse_with_missing_symbol():
    assert to_morse('a!b') == '.- -...'
