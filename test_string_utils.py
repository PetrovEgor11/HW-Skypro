from HW4 import StringUtils

utils = StringUtils()

def test_capitilize(string: str) -> str:
    """
    Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
    Пример: capitilize("skypro") -> "Skypro"
    """
    result = utils.capitilize(string) # Передаем строку в функцию
    return result

# Тестируем функцию с разными входными данными
print(test_capitilize("hello"))
print(test_capitilize("привет"))
print(test_capitilize("SKYPRO"))
print(test_capitilize("123hello"))
print(test_capitilize("hELLO"))
print(test_capitilize("...hello"))
print(test_capitilize("   hello"))


def test_trim(string: str) -> str:
    """
    Принимает на вход текст и удаляет пробелы в начале строки.
    Пример: trim("   skypro") -> "skypro"
    """
    return string.lstrip()

print(test_trim("  Привет"))
print(test_trim(" Првиет"))
print(test_trim("                 Привет"))
print(test_trim("Привет      "))
print(test_trim("123Привет"))
print(test_trim(" П р и в е т "))

def test_to_list(string: str, delimeter=",") -> list:
    """
    Принимает на вход текст с разделителем и возвращает список строк.

    Параметры:
        string - строка для обработки
        delimeter - разделитель строк. По умолчанию запятая (",")

    Пример 1: to_list("a,b,c,d") -> ["a", "b", "c", "d"]
    Пример 2: to_list("1:2:3", ":") -> ["1", "2", "3"]
    """
    if not string:
        return []
    return string.split(delimeter)

print(test_to_list("a,b,v,g"))
print(test_to_list("a/b/v/g/d"))
print(test_to_list("a:b:v:g:d"))
print(test_to_list(", , , ,"))
print(test_to_list("1:2:3"))
print(test_to_list("a;b;v;d"))
print(test_to_list("a,,b,,v,,d"))
print(test_to_list("abv,gd"))


def test_contains(string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n 
        Параметры: \n 
            `string` - строка для обработки \n
            `symbol` - искомый символ \n
        Пример 1: `contains("SkyPro", "S") -> True`
        Пример 2: `contains("SkyPro", "U") -> False`
        """
        return symbol in string
print (test_contains("Hello", "H"))
print (test_contains("Hello", "X"))
print (test_contains("Hello", "L"))
print (test_contains("Hello", "ll"))
print (test_contains("Hello", "Hello"))
print (test_contains("Hello", "XXX"))
print (test_contains("Hello", " "))
print (test_contains("Hello", "1"))

class StringUtils:
    def test_delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки
        
        Параметры:
            string - строка для обработки
            symbol - искомый символ для удаления
            
        Пример 1: delete_symbol("SkyPro", "k") -> "SyPro"
        Пример 2: delete_symbol("SkyPro", "Pro") -> "Sky"
        """
        
        result_string = string.replace(symbol, "")
        return result_string

string_utils = StringUtils()

print(string_utils.test_delete_symbol("SkyPro", "k"))
print(string_utils.test_delete_symbol("Привет", "k"))
print(string_utils.test_delete_symbol("Привет", "ет"))
print(string_utils.test_delete_symbol("SkyPro123", "13"))
print(string_utils.test_delete_symbol("SkyPro ", " "))

def test_starts_with(string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка начинается с заданного символа и `False` - если нет \n 
        Параметры: \n 
            `string` - строка для обработки \n
            `symbol` - искомый символ \n
        Пример 1: `starts_with("SkyPro", "S") -> True`
        Пример 2: `starts_with("SkyPro", "P") -> False`
        """
        return string.startswith(symbol)
print(test_starts_with("SkyPro", "S"))
print(test_starts_with("SkyPro", "Sk"))
print(test_starts_with("1SkyPro", "1"))
print(test_starts_with(" SkyPro", " "))
print(test_starts_with("%SkyPro", "%"))
print(test_starts_with("SkyPro", "k"))
print(test_starts_with("SkyPro", "1"))

def test_end_with( string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет \n 
        Параметры: \n 
            `string` - строка для обработки \n
            `symbol` - искомый символ \n
        Пример 1: `end_with("SkyPro", "o") -> True`
        Пример 2: `end_with("SkyPro", "y") -> False`
        """
        return string.endswith(symbol)

print(test_end_with("SkyPro", "o"))
print(test_end_with("SkyPro", "ro"))
print(test_end_with("SkyPro1", "1"))
print(test_end_with("SkyPro ", " "))
print(test_end_with("SkyPro%", "%"))
print(test_end_with("SkyPro", "r"))
print(test_end_with("SkyPro", "1"))

def test_is_empty(self, string: str) -> bool:
        """
        Возвращает `True`, если строка пустая и `False` - если нет \n 
        Пример 1: `is_empty("") -> True`
        Пример 2: `is_empty(" ") -> True`
        Пример 3: `is_empty("SkyPro") -> False`
        
        """
        return not string.strip()

print(test_is_empty("is_empty", " "))
print(test_is_empty("is_empty", "y"))
print(test_is_empty("is_empty", ""))
print(test_is_empty("is_empty", "is_empty"))

def test_list_to_string(lst: list, joiner=", ") -> str:
        """
        Преобразует список элементов в строку с указанным разделителем \n 
        Параметры: \n 
            `lst` - список элементов \n
            `joiner` - разделитель элементов в строке. По умолчанию запятая (", ") \n
        Пример 1: `list_to_string([1,2,3,4]) -> "1, 2, 3, 4"`
        Пример 2: `list_to_string(["Sky", "Pro"]) -> "Sky, Pro"`
        Пример 3: `list_to_string(["Sky", "Pro"], "-") -> "Sky-Pro"`
        """
        string = ""
        length = len(lst)
        
        if length == 0: 
            return string 
        
        for i in range(0, length-1):
            string += str(lst[i]) + joiner
        
        return string + str(lst[-1])
print(test_list_to_string([1,2,3,4]))
print(test_list_to_string(["Sky", "Pro"]))
print(test_list_to_string(["Sky", "Pro"], "-"))












    

