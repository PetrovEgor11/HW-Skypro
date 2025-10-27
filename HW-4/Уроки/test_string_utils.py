import pytest
from string_utils import StringUtils

@pytest.fixture
def utils():
    return StringUtils()

# Тесты для метода capitalize
def test_capitalize(utils):
    assert utils.capitalize('hello') == 'Hello'
    assert utils.capitalize('world') == 'World'
    assert utils.capitalize('python') == 'Python'
    assert utils.capitalize('123') == '123'  # Первая буква не алфавитная

# Тесты для метода trim
def test_trim(utils):
    assert utils.trim("   hello ") == "hello"
    assert utils.trim("\\t\\t python \\n") == "python"  # Использованы реальные символы
    assert utils.trim('no spaces') == 'no spaces'
    assert utils.trim('   ') == ''

# Тесты для метода to_list
def test_to_list(utils):
    assert utils.to_list('a,b,c') == ['a', 'b', 'c']  # Стандартный случай
    assert utils.to_list('1:2:3', ':') == ['1', '2', '3']  # Другой разделитель
    assert utils.to_list('', ',') == []  # Пустая строка
    assert utils.to_list(' ', ',') == []  # Строка с пробелом

# Тесты для метода contains
def test_contains(utils):
    assert utils.contains('SkyPro', 'S') == True
    assert utils.contains('SkyPro', 'K') == False
    assert utils.contains('SkyPro', '') == True  # Пустой символ всегда содержится
    assert utils.contains('SkyPro', 'Pro') == True

# Тесты для метода delete_symbol
def test_delete_symbol(utils):
    assert utils.delete_symbol('SkyPro', 'k') == 'SyPro'
    assert utils.delete_symbol('SkyPro', 'Pro') == 'Sky'
    assert utils.delete_symbol('abcdef', 'xyz') == 'abcdef'  # Нет символа для удаления
    assert utils.delete_symbol('Test', 'T') == 'est'

# Тесты для метода starts_with
def test_starts_with(utils):
    assert utils.starts_with('SkyPro', 'S') == True
    assert utils.starts_with('SkyPro', 'P') == False
    assert utils.starts_with('SkyPro', '') == True  # Пустой символ совпадает с началом
    assert utils.starts_with('SkyPro', 'Sk') == True

# Тесты для метода is_empty
def test_is_empty(utils):
    assert utils.is_empty('') == True
    assert utils.is_empty(' ') == True
    assert utils.is_empty("\\t\\n") == True  # Табуляция и перенос строки
    assert utils.is_empty('Text') == False
    assert utils.is_empty('  Text  ') == False
